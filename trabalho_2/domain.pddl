
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
        