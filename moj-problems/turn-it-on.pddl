(define (problem turn-it-on)
    (:domain fliaswitch)

    ;; Estado inicial
    (:init
        (switch-is-off) ;; O interruptor está desligado
    )

    ;; Objetivo
    (:goal
        (switch-is-on) ;; O interruptor deve estar ligado
    )
)
