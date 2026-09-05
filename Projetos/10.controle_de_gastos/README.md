# Aula 10 — Mini-projeto: controle de gastos pessoais

## Objetivo

Construir um programa de terminal que registre gastos pessoais e produza um
resumo financeiro. O projeto consolida os conteúdos das aulas 1 a 9 sem usar
funções, arquivos externos ou bibliotecas.

## Resultado esperado

O programa deve coletar um orçamento e vários gastos, armazenar cada gasto como
um dicionário dentro de uma lista e, ao final, apresentar informações que ajudem
o usuário a compreender para onde foi o dinheiro.

Cada registro deverá conter os campos:

- `descricao`: texto que identifica o gasto;
- `categoria`: texto padronizado;
- `valor`: número maior que zero.

## Requisitos obrigatórios

1. Solicite o orçamento disponível e aceite somente um número maior que zero.
2. Solicite a quantidade de gastos e aceite somente um inteiro maior que zero.
3. Para cada gasto, solicite descrição, categoria e valor.
4. Não aceite descrição ou categoria vazia.
5. Remova espaços das extremidades e padronize o texto das categorias.
6. Aceite somente valores de gasto maiores que zero.
7. Armazene todos os registros em uma lista de dicionários.
8. Calcule o total, a média, o menor gasto e o maior gasto.
9. Crie um conjunto com as categorias registradas.
10. Crie um dicionário com o total gasto por categoria.
11. Crie outro dicionário com a quantidade de gastos por categoria.
12. Crie uma lista com os gastos acima da média.
13. Informe o saldo restante ou quanto o orçamento foi ultrapassado.
14. Apresente um relatório final legível, com valores monetários formatados.

## Etapas sugeridas

### Etapa 1 — Entrada e validação

Implemente primeiro a leitura do orçamento e da quantidade. Teste entradas como
zero, números negativos, texto vazio e letras.

### Etapa 2 — Cadastro

Monte o laço que coleta os gastos. Depois de cada cadastro, confira no terminal
se a lista contém um dicionário com os três campos esperados.

### Etapa 3 — Resumo geral

Calcule total, média, menor e maior gasto. Para o menor e o maior, preserve o
registro completo para poder exibir também sua descrição e categoria.

### Etapa 4 — Resumo por categoria

Percorra os registros e construa os dois dicionários de resumo. Os nomes das
categorias não devem ser escritos antecipadamente no código.

### Etapa 5 — Relatório

Organize a saída em blocos: visão geral, orçamento, categorias e gastos acima
da média. Confira se os números apresentados correspondem aos registros.

## Casos de teste

Execute pelo menos estes cenários:

- orçamento de `1000`, com gastos de `400` e `350`: deve restar saldo;
- orçamento de `500`, com gastos de `300` e `250`: deve indicar excesso;
- gasto exatamente igual ao orçamento: o saldo deve ser zero;
- duas categorias escritas com diferenças de maiúsculas ou espaços: devem ser
  tratadas como a mesma categoria;
- apenas um gasto: média, menor e maior devem funcionar;
- tentativas com quantidade zero, valor negativo e texto vazio: devem ser
  recusadas sem encerrar o programa.

## Critérios de avaliação

- atendimento a todos os requisitos;
- cálculos corretos e coerentes com a quantidade de registros;
- uso adequado de lista, conjunto e dicionários;
- validação dos casos de borda;
- nomes claros e organização em blocos;
- relatório final fácil de interpretar.

## Desafios opcionais

- permitir que o usuário cadastre gastos até digitar `fim`, em vez de informar
  previamente uma quantidade;
- informar qual categoria representa a maior parcela do total;
- comparar cada categoria com uma meta definida pelo usuário;
- criar um menu para cadastrar, listar, resumir e encerrar.

Implemente sua resposta em `main.py`. Não consulte uma solução pronta: avance
por etapas e teste cada bloco antes de começar o próximo.
