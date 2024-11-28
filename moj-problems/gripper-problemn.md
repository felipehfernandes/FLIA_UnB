# Gripper - Problema 2 - Criar arquivo de problema
Bruno Ribas, baseado no domínio GRIPPER do IPC-1998

# Preâmbulo
Temos um cenário com um conjunto de salas, e dentro dessas salas podem existir bolas. Um robô está encarregado de mover as bolas entre as salas. O robô possui duas pinças: uma left (esquerda) e outra right (direita), que ele usa para segurar as bolas.

O objetivo dessa tarefa é transferir todas as bolas de uma sala inicial para uma sala destino. Para que isso seja feito, o robô usa suas duas pinças para pegar as bolas em uma sala e levá-las para outra sala, uma de cada vez.

Você deve escrever um programa que leia da Entrada padrão a descrição do mundo, contendo a quantidade de salas, quantidade de bolas, posição inicial de cada bola e onde cada bola deve terminar.

Assuma que as pinças left e right sempre iniciam livres e o robô inicia na primeira sala descrita.

# Entrada
A entrada é composta por um único caso de teste. A primeira linha, do caso de teste, possui dois números inteiros S e B, 2≤S<100 e 1≤B≤300, representando, respectivamente, o número de salas e o número de bolas existentes no problema.

A segunda linha, do caso de teste, possui S strings, de comprimento máximo de 100 caracteres, representando os nomes das salas do problema.

Depois existirão B linhas, cada uma contendo 3 strings, B_i S_i D_i, de comprimento máximo de 100 caracteres, representando, respectivamente, o nome da i-ésima bola, a sala em que a bola começa e a sala que a bola deve terminar.

# Saída
A saída do seu programa deverá ser um arquivo PDDL, gerado na saída padrão, representando, o arquivo de problema específico definido na entrada.

Observação: Certifique-se de que seu arquivo de problema é funcional, executando um planejador PDDL com o domínio e problema definidos.

Observação2: Você pode testar o seu exemplo diretamente pelo sistema https://plan-editor.naquadah.com.br/

Domínio
Abaixo está o arquivo de domínio que define a infraestrutura básica do sistema:

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

# Exemplos de Entrada e Saída
## Exemplo de Entrada
2 4
salaA salaB
bola1 salaA salaB
bola2 salaA salaB
bola3 salaA salaB
bola4 salaA salaB

## Saída para exemplo de entrada acima
(define (problem problemagarra)
  (:domain gripper-typed)
  (:objects
salaA salaB - room
bola1 bola2 bola3 bola4  - ball)
 (:init (at-robby salaA)
    (free left)
    (free right)
(at bola1 salaA) (at bola2 salaA) (at bola3 salaA) (at bola4 salaA)  )
 (:goal (and (at bola1 salaB) (at bola2 salaB) (at bola3 salaB) (at bola4 salaB)  )))