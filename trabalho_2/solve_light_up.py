import subprocess

# Constants
WHITE_CELL = "-"
BLACK_CELL = "#"
NUMERIC_BLACK_CELL = "01234"


def read_grid():
    """Reads the grid input until EOF and returns it as a list of strings."""
    print("Reading grid input...")
    grid = []
    while True:
        try:
            line = input().strip()
            if line == "":
                break
            grid.append(line)
        except EOFError:
            break
    print("Grid read successfully:", grid)
    return grid


def generate_pddl_files(grid, domain_path, problem_path):
    """Generate PDDL domain and problem files based on the grid."""
    print("Generating PDDL files...")
    num_lines = len(grid)
    num_columns = len(grid[0])

    generate_domain(domain_path)
    print(f"Domain file generated at: {domain_path}")

    generate_problem(grid, num_lines, num_columns, problem_path)
    print(f"Problem file generated at: {problem_path}")


def generate_domain(domain_path):
    """Creates a PDDL domain file for Light Up."""
    with open(domain_path, 'w') as domain_file:
        domain_file.write("""
            (define (domain lightup)
            (:requirements :strips)
            (:types position)
            (:predicates
                (lamp ?x - position ?y - position)
                (lighted ?x - position ?y - position)
                (black ?x - position ?y - position)
                (reqLamps ?x - position ?y - position ?n - number)
                (next ?p1 - position ?p2 - position)
            )
            (:action placeLamp
                :parameters (?x - position ?y - position)
                :precondition (not (lamp ?x ?y))
                :effect (and
                    (lamp ?x ?y)
                    (forall (?px - position)
                        (when (and (next ?x ?px) (not (black ?px ?y)))
                              (lighted ?px ?y)))
                    (forall (?py - position)
                        (when (and (next ?y ?py) (not (black ?x ?py)))
                              (lighted ?x ?py)))
                )
            )
        )
        """)
    print("Domain file content written successfully.")


def generate_problem(grid, num_lines, num_columns, problem_path):
    """Creates a PDDL problem file based on the Light Up grid."""
    x_positions = [f"x{i + 1}" for i in range(num_lines)]
    y_positions = [f"y{j + 1}" for j in range(num_columns)]

    with open(problem_path, 'w') as problem_file:
        problem_file.write(f"""
            (define (problem lightup-instance)
                (:domain lightup)
                (:objects {" ".join(x_positions)} - position {" ".join(y_positions)} - position)
                (:init
                    {generate_next(num_lines, num_columns)}
                    {generate_init_conditions(grid, num_lines, num_columns)}
                )
                (:goal
                    (and
                        (forall (?x - position ?y - position)
                            (lighted ?x ?y)
                        )
                    )
                )
            )
        """)
    print("Problem file content written successfully.")


def generate_next(num_lines, num_columns):
    """Generate the next relations for positions."""
    next_x = [f"(next x{i} x{i + 1})" for i in range(1, num_lines)] if num_lines > 1 else []
    next_y = [f"(next y{j} y{j + 1})" for j in range(1, num_columns)] if num_columns > 1 else []
    return " ".join(next_x + next_y)


def generate_init_conditions(grid, num_lines, num_columns):
    """Generate initial conditions for PDDL problem file."""
    conditions = []
    for i in range(num_lines):
        for j in range(num_columns):
            cell = grid[i][j]
            if cell in NUMERIC_BLACK_CELL:
                conditions.append(f"(reqLamps x{i + 1} y{j + 1} {cell})")
                conditions.append(f"(black x{i + 1} y{j + 1})")
            elif cell == BLACK_CELL:
                conditions.append(f"(black x{i + 1} y{j + 1})")
    return " ".join(conditions)


def run_planner(domain_path, problem_path):
    """Executes the PDDL planner and returns the output."""
    print("Running planner...")
    command = f"/tmp/dir/software/planners/madagascar/M {domain_path} {problem_path}"
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        print("Planner executed successfully.")
        return result.splitlines()
    except subprocess.CalledProcessError as e:
        print("Planner failed to find a solution.")
        print(e.output)
        exit(120)


def parse_solution(planner_output):
    """Parses planner output to extract bulb placements."""
    print("Parsing planner output...")
    bulb_positions = []
    for line in planner_output:
        if "placeLamp" in line:
            parts = line.split()
            x = int(parts[1][1:]) - 1
            y = int(parts[2][1:]) - 1
            bulb_positions.append(f"(bulb {y} {x})")  # Note: switched back to match output format
    print("Parsed bulb positions:", bulb_positions)
    return bulb_positions


def main():
    print("Starting program...")
    grid = read_grid()
    domain_path, problem_path = "domain.pddl", "problem.pddl"
    generate_pddl_files(grid, domain_path, problem_path)
    planner_output = run_planner(domain_path, problem_path)
    bulb_positions = parse_solution(planner_output)

    if bulb_positions:
        print(";".join(bulb_positions))
    else:
        print("No solution found!")
        exit(120)


if __name__ == "__main__":
    main()
