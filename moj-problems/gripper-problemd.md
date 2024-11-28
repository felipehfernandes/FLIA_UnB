#  Gripper - Problema 3 - Criar e rodar problema
Bruno Ribas, baseado no domínio GRIPPER do IPC-1998

# Preâmbulo
Temos um cenário com um conjunto de salas, e dentro dessas salas podem existir bolas. Um robô está encarregado de mover as bolas entre as salas. O robô possui duas pinças: uma left (esquerda) e outra right (direita), que ele usa para segurar as bolas.

O objetivo dessa tarefa é transferir todas as bolas de uma sala inicial para uma sala destino. Para que isso seja feito, o robô usa suas duas pinças para pegar as bolas em uma sala e levá-las para outra sala, uma de cada vez.

Você deve escrever um programa que leia da Entrada padrão a descrição do mundo, contendo a quantidade de salas, quantidade de bolas, posição inicial de cada bola e onde cada bola deve terminar.

Assuma que as pinças left e right sempre iniciam livres e o robô inicia na primeira sala descrita, note que elas são :constants do domínio e não precisam ser declaradas no arquivo de problema.

# Entrada
A entrada é composta por um único caso de teste. A primeira linha, do caso de teste, possui dois números inteiros S e B, 2≤S<100 e 1≤B≤300, representando, respectivamente, o número de salas e o número de bolas existentes no problema.

A segunda linha, do caso de teste, possui S strings, de comprimento máximo de 100 caracteres, representando os nomes das salas do problema.

Depois existirão B linhas, cada uma contendo 3 strings, B_i S_i D_i, de comprimento máximo de 100 caracteres, representando, respectivamente, o nome da i-ésima bola, a sala em que a bola começa e a sala que a bola deve terminar.

# Saída
A Saída do seu programa deve ser o plano de execução do problema descrito.

# Tarefa
- Escreva um programa que:
1. Leia a descrição do problema conforme o formato da entrada.
2. Gere o arquivo de problema /tmp/problem.pddl conforme o padrão PDDL (Planning Domain Definition Language).
3. Salve o arquivo de domínio em /tmp/domain.pddl. O conteúdo do arquivo de domínio já está definido e deve ser incluído no código fonte.
- Depois de gerar os arquivos, o programa deverá executar o planejador fast-downward utilizando a seguinte configuração:
    - Caminho do planejador: /tmp/dir/software/planners/downward-fdss23/fast-downward.py
    - Algoritmo a ser usado: seq-opt-fdss-2023.
- A saída do programa será o plano gerado pelo planejador, que deve ser impresso diretamente na saída padrão.

> DICA: Mude o working directory do seu programa para /tmp, pois o fast-downward gera um conjunto de arquivos no diretório local e não funcionará por padrão. Em C/C++ veja a função chdir(2)

# Domínio
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
(pick bola3 salaa left)
(pick bola4 salaa right)
(move salaa salab)
(drop bola3 salab left)
(drop bola4 salab right)
(move salab salaa)
(pick bola1 salaa left)
(pick bola2 salaa right)
(move salaa salab)
(drop bola1 salab left)
(drop bola2 salab right)
; cost = 11 (unit cost)

## Exemplo de Entrada
3 4
salaA salaB salaC
bola1 salaA salaC
bola2 salaB salaC
bola3 salaC salaA
bola4 salaB salaA

## Saída para exemplo de entrada acima
(move salaa salab)
(pick bola2 salab left)
(pick bola4 salab right)
(move salab salaa)
(drop bola4 salaa right)
(pick bola1 salaa right)
(move salaa salac)
(drop bola2 salac left)
(drop bola1 salac right)
(pick bola3 salac left)
(move salac salaa)
(drop bola3 salaa left)
; cost = 12 (unit cost)