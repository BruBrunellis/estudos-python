# Aula 6 — Laço while
#
# Objetivo: repetir blocos de código enquanto uma condição for verdadeira.
# Pré-requisitos: variáveis, operadores, input() e condicionais.

# Estrutura básica:
# while condicao:
#     bloco_repetido
#
# A condição é verificada antes de cada repetição. Quando ela se torna False,
# o laço termina.
contador = 1

while contador <= 5:
    print(f"Contagem: {contador}")
    contador += 1

print("Fim da contagem.\n")

# É essencial atualizar algo relacionado à condição. Sem `contador += 1`, por
# exemplo, este laço nunca terminaria: isso é um laço infinito.

# Acumuladores guardam um resultado que cresce ou muda a cada repetição.
numero = 1
soma = 0

while numero <= 5:
    soma += numero
    numero += 1

print(f"Soma de 1 até 5: {soma}\n")

# Um sentinela é um valor especial que indica quando parar. Neste exemplo,
# a palavra "sair" encerra o programa.
comando = ""

while comando != "sair":
    comando = input("Digite algo ou 'sair' para encerrar: ").strip().lower()

    if comando != "sair":
        print(f"Você digitou: {comando}")

print("Programa encerrado.\n")

# while também é útil para repetir uma pergunta até receber um valor válido.
idade = -1

while idade < 0:
    idade = int(input("Digite uma idade não negativa: "))

print(f"Idade registrada: {idade}\n")

# break interrompe imediatamente o laço. Use quando houver uma condição clara
# de encerramento; em outros casos, o sentinela costuma deixar o fluxo mais claro.
tentativa = 1

while tentativa <= 3:
    senha = input(f"Tentativa {tentativa}/3 — digite a senha: ")

    if senha == "python":
        print("Senha correta.")
        break

    print("Senha incorreta.")
    tentativa += 1
else:
    # O else do while roda somente se o laço terminar sem passar por break.
    print("Número máximo de tentativas atingido.")

# Ponte para análise de dados:
# Antes de usar arquivos e tabelas, podemos simular a coleta de valores até que
# uma pessoa informe "fim". O contador e o total representam métricas simples.
total_vendas = 0.0
quantidade_vendas = 0
entrada = ""

while entrada != "fim":
    entrada = input("Valor da venda ou 'fim': ").strip().lower()

    if entrada != "fim":
        valor = float(entrada)
        total_vendas += valor
        quantidade_vendas += 1

print(f"Foram registradas {quantidade_vendas} vendas.")
print(f"Total vendido: R$ {total_vendas:.2f}")

# Erros comuns:
# - esquecer de atualizar a variável da condição e criar um laço infinito;
# - usar while com uma condição que já começa como False sem perceber;
# - comparar um número com input() sem convertê-lo para int() ou float();
# - atualizar o contador no lugar errado e pular ou repetir valores;
# - usar break em excesso, deixando o fluxo difícil de entender.
