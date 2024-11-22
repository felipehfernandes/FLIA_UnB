def generate_pddl():
    import sys
    input_data = sys.stdin.read().strip().split("\n")

    rooms = input_data[1].split()
    balls = [line.split() for line in input_data[2:]]

    pddl_output = [
        "(define (problem problemagarra)",
        "  (:domain gripper-typed)",
        "  (:objects",
        "    " + " ".join(rooms) + " - room",
        "    " + " ".join(ball[0] for ball in balls) + " - ball)",
        "  (:init",
        "    (at-robby " + rooms[0] + ")",
        "    (free left)",
        "    (free right)",
        "    " + " ".join(f"(at {ball[0]} {ball[1]})" for ball in balls),
        "  )",
        "  (:goal (and",
        "    " + " ".join(f"(at {ball[0]} {ball[2]})" for ball in balls),
        "  ))",
        ")"
    ]

    final_output = "\n".join(pddl_output).strip()
    print(final_output)


if __name__ == "__main__":
    generate_pddl()
