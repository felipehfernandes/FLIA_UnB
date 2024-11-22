(define (problem gripper-problem1)
    (:domain gripper-typed)

    ;; Declaração dos objetos
    (:objects
        rooma roomb - room
        ball1 ball2 ball3 ball4 - ball
    )

    ;; Estado inicial
    (:init
        ;; O robô começa na sala rooma
        (at-robby rooma)

        ;; Todas as bolas começam na sala rooma
        (at ball1 rooma)
        (at ball2 rooma)
        (at ball3 rooma)
        (at ball4 rooma)

        ;; Ambas as pinças estão livres
        (free left)
        (free right)
    )

    ;; Objetivo
    (:goal
        (and
            ;; Todas as bolas devem estar na sala roomb
            (at ball1 roomb)
            (at ball2 roomb)
            (at ball3 roomb)
            (at ball4 roomb)
        )
    )
)