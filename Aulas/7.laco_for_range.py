# Aula 7 — Laço for e range
#
# Objetivo: percorrer sequências e repetir ações uma quantidade definida de vezes.
# Pré-requisitos: variáveis, condicionais, strings e laço while.

# O for percorre, um item por vez, uma sequência de valores.
# range(fim) cria números de 0 até fim - 1.
for numero in range(5):
    print(numero)

print()

# range(inicio, fim) começa em inicio e termina antes de fim.
for numero in range(1, 6):
    print(f"Número: {numero}")

print()

# range(inicio, fim, passo) controla de quanto em quanto o contador avança.
for par in range(2, 11, 2):
    print(par)

print()

# Um passo negativo permite uma contagem regressiva.
for contagem in range(5, 0, -1):
    print(contagem)

print("Fim da contagem.\n")

# O for também percorre strings, caractere por caractere.
palavra = "dados"

for letra in palavra:
    print(letra.upper())

print()

# Podemos usar condições dentro do laço para contar ou acumular valores.
soma_pares = 0

for numero in range(1, 11):
    if numero % 2 == 0:
        soma_pares += numero

print(f"Soma dos pares de 1 a 10: {soma_pares}\n")

# Uma variável de controle pode contar ocorrências.
frase = "analise de dados"
quantidade_a = 0

for caractere in frase:
    if caractere == "a":
        quantidade_a += 1

print(f"Quantidade de letras 'a': {quantidade_a}\n")

# break interrompe o for assim que uma condição é atendida.
for numero in range(1, 11):
    if numero == 6:
        break
    print(numero)

print()

# continue ignora somente a repetição atual e segue para a próxima.
for numero in range(1, 8):
    if numero % 2 != 0:
        continue
    print(f"Par: {numero}")

# Ponte para análise de dados:
# É comum percorrer registros para calcular uma métrica. Mais adiante, pandas
# fará isso para tabelas inteiras, mas compreender o processo é importante.
total_vendas = 0.0

for venda in range(1, 6):
    valor = venda * 100.0
    total_vendas += valor

print(f"Total de vendas simuladas: R$ {total_vendas:.2f}")

# Erros comuns:
# - esperar que range(5) inclua o 5: ele termina no 4;
# - esquecer que o fim de range nunca é incluído;
# - usar um passo positivo em uma contagem regressiva;
# - alterar manualmente a variável do for: o for a atualiza automaticamente;
# - usar while quando já se sabe quantas repetições serão necessárias.
