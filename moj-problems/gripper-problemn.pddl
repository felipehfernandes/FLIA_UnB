(define (problem problemagarra)
  (:domain gripper-typed)
  (:objects
    salaA salaB - room
    bola1 bola2 bola3 bola4 - ball
  )
  (:init
    (at-robby salaA)
    (free left)
    (free right)
    (at bola1 salaA)
    (at bola2 salaA)
    (at bola3 salaA)
    (at bola4 salaA)
  )
  (:goal
    (and
      (at bola1 salaB)
      (at bola2 salaB)
      (at bola3 salaB)
      (at bola4 salaB)
    )
  )
)