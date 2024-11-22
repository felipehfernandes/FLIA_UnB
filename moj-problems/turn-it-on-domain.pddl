(define (domain fliaswitch)
   (:requirements :strips)
   (:predicates
      (switch-is-on)   ;; O interruptor está ligado
      (switch-is-off)) ;; O interruptor está desligado

   ;; Ação para ligar o interruptor
   (:action switch-on
       :parameters ()
       :precondition (switch-is-off)
       :effect (and (switch-is-on) (not (switch-is-off))))

   ;; Ação para desligar o interruptor
   (:action switch-off
       :parameters ()
       :precondition (switch-is-on)
       :effect (and (switch-is-off) (not (switch-is-on)))))