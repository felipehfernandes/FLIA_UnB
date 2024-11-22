(define (domain gripper-typed)
   (:requirements :typing)
   (:types room ball gripper)
   (:constants left right - gripper)
   (:predicates
    (at-robby ?r - room)            ;; O robô está em uma sala
      (at ?b - ball ?r - room)        ;; Uma bola está em uma sala
    (free ?g - gripper)             ;; A pinça está livre
      (carry ?o - ball ?g - gripper)) ;; Uma pinça está segurando uma bola

   ;; Ação de mover o robô entre salas
   (:action move
       :parameters  (?from ?to - room)
       :precondition (at-robby ?from)
       :effect (and  (at-robby ?to)
             (not (at-robby ?from))))

   ;; Ação de pegar uma bola com uma das pinças, em uma determinada sala
   (:action pick
       :parameters (?obj - ball ?room - room ?gripper - gripper)
       :precondition (and (at ?obj ?room) (at-robby ?room) (free ?gripper))
       :effect (and (carry ?obj ?gripper)
            (not (at ?obj ?room))
            (not (free ?gripper))))

   ;; Ação de soltar uma bola de uma pinça em uma sala específica
   (:action drop
       :parameters (?obj - ball ?room - room ?gripper - gripper)
       :precondition (and (carry ?obj ?gripper) (at-robby ?room))
       :effect (and (at ?obj ?room)
            (free ?gripper)
            (not (carry ?obj ?gripper)))))