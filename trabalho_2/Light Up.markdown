Light Up

# Descrição do jogo
Light Up, também conhecido como Akari, é um quebra-cabeça lógico de determinação binária publicado pela Nikoli, uma editora japonesa especializada em jogos e, especialmente, em quebra-cabeças lógicos. A Nikoli foi fundada em 1980 e ganhou destaque mundial com a popularidade do egrégio Sudoku. Até 2011, três livros compostos inteiramente por quebra-cabeças Light Up foram publicados pela Nikoli.

Light Up é jogado em uma grade retangular de células brancas e pretas. O jogador coloca lâmpadas em células brancas de forma que nenhuma lâmpada ilumine outra diretamente, até que toda a grade esteja iluminada. Uma lâmpada emite raios de luz horizontal e verticalmente, iluminando todas as células de mesma linha e coluna, a menos que a luz seja bloqueada por uma célula preta. Uma célula preta pode ter um número de 0 a 4, indicando quantas lâmpadas devem ser colocadas adjacentes aos seus quatro lados; por exemplo, uma célula com o número 4 deve ter quatro lâmpadas ao seu redor, uma de cada lado, e uma célula com 0 não pode ter lâmpadas em nenhum de seus lados. Uma célula preta sem número pode ter qualquer quantidade de lâmpadas adjacentes a ela, inclusive nenhuma. Ademais, lâmpadas colocadas na diagonal de uma célula numerada não contribuem para a contagem de lâmpadas.

# Descrição do problema
Você deve desenvolver um programa que leia a especificação do desafio, via stdin, obtenha o plano para a conclusão do mapa lido, e gere uma saída, via stdout, no formato especificado na descrição do trabalho. Caso não encontre um plano, encerre seu programa com um exit(120).

## Ferramentas e auxiliares
Esta seção descreve as várias ferramentas auxiliares disponíveis para resolver o problema do jogo Akari. As ferramentas estão organizadas em categorias: planejadores PDDL, planejadores HDDL, SAT-solvers e bibliotecas auxiliares. A localização e a forma de chamada de cada ferramenta estão descritas a seguir.

### Planejadores PDDL
Para utilizar dos planejadores PDDL, você precisará de um modelo PDDL do jogo Akari, crie os arquivos de domínio e problema PDDL correspondentes, chame o planejador selecionado com os parâmetros corretos. Aqui estão os planejadores PDDL disponíveis:

1. Planejadores Madagascar (M, Mp, MpC):
    - Localização: /tmp/dir/software/planners/madagascar/{M,Mp,MpC}.
2. Fast Downward:
    - Localização: /tmp/dir/software/planners/downward/fast-downward.py.
    - Localização: /tmp/dir/software/planners/downward-fdss23/fast-downward.py.
    - Localização: /tmp/dir/software/planners/scorpion-maidu/fast-downward.py.
3. Planejador em Julia:
    - Localização: /tmp/dir/software/planners/julia/planner.jl.

### Planejadores HDDL
Para utilizar dos planejadores HDDL, você precisará de um modelo HDDL do jogo Akari, crie os arquivos de domínio e problema HDDL correspondentes, chame o planejador selecionado com os parâmetros corretos. Aqui estão os planejadores HDDL disponíveis:

1. Panda:
    - Localização: /tmp/dir/software/planners/panda/panda.jar.
2. PandaPI:
    - Localização: /tmp/dir/software/planners/pandaPI/pandasolver.

### SAT-solvers
Para utilizar dos SAT-solvers, você precisará de uma formulação do problema Akari em forma de CNF (Conjunctive Normal Form). Aqui estão os SAT-solvers disponíveis e como utilizá-los:

1. Clasp:
    - Localização: /usr/bin/clasp.
2. CryptoMiniSat:
    - Localização: /usr/bin/cryptominisat.
3. MiniSat:
    - Localização: /usr/bin/minisat.
4. MiniSat+:
    - Localização: /usr/bin/minisat+.
5. PackUp:
    - Localização: /usr/bin/packup.
6. PicoSAT:
    - Localização: /usr/bin/picosat.
7. SAT4J:
    - Localização: /usr/bin/sat4j.
8. Python-SAT:
    - https://pysathq.github.io/docs/html.
9. Z3
    - Localização: /usr/bin/z3

# Como classificar nesta modalidade
Nesta modalidade de classificação, o problema é dividido em três categorias: AGILE, SATISFICING e OPTIMAL. A pontuação é computada da seguinte forma:

1. Categoria AGILE:
    - A pontuação é obtida pela fórmula: log(TempoDeExecucao)/log(30)
    - Se o tempo de execução for menor ou igual a 1 segundo, a pontuação é 1.
    - A track tem um time limit de 30s.
2. Categoria SATISFICING:
    - A pontuação é calculada pela fórmula C*/C, onde C* é a quantidade de passos do plano de referência e C é a quantidade de passos do plano encontrado.
    - Quanto menor for a quantidade de passos do plano encontrado em relação ao plano de referência, melhor será a pontuação.
    - A track tem um time limit de 180s.
3. Categoria OPTIMAL:
    - O objetivo é responder o plano ótimo.
    - O desempenho é avaliado pela corretude do plano e não pela pontuação.
    - A track tem um time limit de 180s.

O vencedor será determinado com base na soma dos pontos obtidos em todas as categorias.

# Entrada
A entrada é composta com um conjunto de linhas, e deverão ser lidas da entrada padrão. As linhas, da entrada, representam a matriz do jogo, você descobrirá as dimensões conforme faz a leitura. A entrada termina em EOF.

Cada célula é representada por um caractere, conforme a descrição abaixo:

    - "-" representa uma célula braca;
    - "#" representa uma célula preta;
    - 0 representa uma célula preta, que não deve ter nenhuma lâmpada adjacente;
    - 1 representa uma célula preta, que deve ter exatamente uma lâmpada adjacente;
    - 2 representa uma célula preta, que deve ter exatamente duas lâmpada adjacente;
    - 3 representa uma célula preta, que deve ter exatamente três lâmpada adjacente;
    - 4 representa uma célula preta, que deve ter exatamente quatro lâmpada adjacente

# Saída
A saída é composta por uma única linha contendo as coordenadas das células, nas quais lâmpadas forma acessas, a fim de iluminar todas as células do tabuleiro. Cada clique é representado pelo plano cartesiano (y, x), sendo y a linha, iniciando em 0, e x a coluna, iniciando em 0, e separados pelo caractere ; , exceto pelo último, que deverá possuir apenas uma quebra de linha.

# Exemplo
## Exemplo de entrada

 ` ` `
--#----
-1---3-
------#
-------
2------
-3---1-
----0--
 ` ` `

## Saída para o exemplo de entrada acima
(bulb 0 1);(bulb 0 5);(bulb 1 4);(bulb 1 6);(bulb 2 3);(bulb 3 0);(bulb 4 5);(bulb 5 0);(bulb 5 2);(bulb 6 1);(bulb 6 6)
