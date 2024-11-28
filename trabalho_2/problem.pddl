
            (define (problem lightup-instance)
                (:domain lightup)
                (:objects x1 x2 x3 x4 x5 x6 x7 - position y1 y2 y3 y4 y5 y6 y7 - position)
                (:init
                    (next x1 x2) (next x2 x3) (next x3 x4) (next x4 x5) (next x5 x6) (next x6 x7) (next y1 y2) (next y2 y3) (next y3 y4) (next y4 y5) (next y5 y6) (next y6 y7)
                    (black x1 y3) (reqLamps x2 y2 1) (black x2 y2) (reqLamps x2 y6 3) (black x2 y6) (black x3 y7) (reqLamps x5 y1 2) (black x5 y1) (reqLamps x6 y2 3) (black x6 y2) (reqLamps x6 y6 1) (black x6 y6) (reqLamps x7 y5 0) (black x7 y5)
                )
                (:goal
                    (and
                        (forall (?x - position ?y - position)
                            (lighted ?x ?y)
                        )
                    )
                )
            )
        