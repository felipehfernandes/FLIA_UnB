import os
import subprocess
import sys

DOMAIN_CONTENT = """(define (domain gripper-typed)
   (:requirements :typing)
   (:types room ball gripper)
   (:constants left right - gripper)
   (:predicates
    (at-robby ?r - room)
    (at ?b - ball ?r - room)
    (free ?g - gripper)
    (carry ?o - ball ?g - gripper))

   (:action move
       :parameters  (?from ?to - room)
       :precondition (at-robby ?from)
       :effect (and  (at-robby ?to)
             (not (at-robby ?from))))

   (:action pick
       :parameters (?obj - ball ?room - room ?gripper - gripper)
       :precondition (and (at ?obj ?room) (at-robby ?room) (free ?gripper))
       :effect (and (carry ?obj ?gripper)
            (not (at ?obj ?room))
            (not (free ?gripper))))

   (:action drop
       :parameters (?obj - ball ?room - room ?gripper - gripper)
       :precondition (and (carry ?obj ?gripper) (at-robby ?room))
       :effect (and (at ?obj ?room)
            (free ?gripper)
            (not (carry ?obj ?gripper)))))"""

def generate_problem_pddl(input_data):
    rooms = input_data[1].split()
    balls = [line.split() for line in input_data[2:]]
    return f"""(define (problem problemagarra)
  (:domain gripper-typed)
  (:objects
    {" ".join(rooms)} - room
    {" ".join(ball[0] for ball in balls)} - ball)
  (:init
    (at-robby {rooms[0]})
    (free left)
    (free right)
    {" ".join(f"(at {ball[0]} {ball[1]})" for ball in balls)}
  )
  (:goal (and
    {" ".join(f"(at {ball[0]} {ball[2]})" for ball in balls)}
  ))
)"""

def run_fast_downward(domain_file, problem_file):
    planner_path = "/tmp/dir/software/planners/downward-fdss23/fast-downward.py" #/tmp/dir = /home para rodar no chococino
    cmd = [
        "python3", planner_path,
        "--alias", "seq-opt-fdss-2023",
        "--plan-file", "plan",
        "--overall-time-limit", "20",
        domain_file,
        problem_file
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    with open("plan", "r") as plan_file:
        print(plan_file.read())
        return plan_file.read()

def main():
    input_data = sys.stdin.read().strip().split("\n")

    os.chdir("/tmp") # Retirar para rodar no chococino

    with open("domain.pddl", "w") as domain_file:
        domain_file.write(DOMAIN_CONTENT)
    with open("problem.pddl", "w") as problem_file:
        problem_file.write(generate_problem_pddl(input_data))

    try:
        run_fast_downward("domain.pddl", "problem.pddl")
    except subprocess.CalledProcessError as e:
        print("Erro ao executar o planejador:", e)

if __name__ == "__main__":
    main()