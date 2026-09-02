# Aula 6 — Lista de exercícios: laço while
# Faça testes com valores de limite e confira se todos os laços terminam.

# 1. Use while para imprimir os números de 1 a 10, um por linha.

contagem = 1

while contagem <= 10:
    print(f"Contagem: {contagem}")
    contagem += 1

print("Contagem encerrada.\n")

# 2. Peça um número inteiro positivo e imprima uma contagem regressiva desse
# número até 0. Se o usuário informar um número negativo, peça novamente até
# receber um valor válido.

numero = -1

while True:
    numero = int(input("Insira um número inteiro positivo: "))
    if numero > 0:
        break
    print("Número inválido. Tente novamente.")

while numero >= 0:
    print(f"Contagem regressiva: {numero}")
    numero -= 1

print("Contagem regressiva encerrada.\n")

# 3. Use while para calcular e imprimir a soma dos números inteiros de 1 a 100.

soma = 0
numero = 1

while numero <= 100:
    soma += numero
    numero += 1

print(f"A soma dos inteiros de 1 a 100 é: {soma}\n")

# 4. Peça uma senha ao usuário enquanto ela for diferente de "python123".
# Quando a senha estiver correta, imprima uma mensagem de acesso liberado.

senha = input("Insira a senha: ")
tentativa = 1

while senha != 'python123':
    print("Senha incorreta.")
    tentativa +=1
    senha = input(f"Tentativa {tentativa}. Insira a senha: ")

print("Senha correta. Acesso liberado.\n")

# 5. Peça números ao usuário até ele digitar 0. Ao final, informe a soma de
# todos os números digitados antes do 0.

numero = 1
soma = 0

while numero != 0:
    numero = float(input("Digite um número, 0 para encerrar: "))
    soma += numero

print(f"Soma dos números antes de 0: {soma:.2f}\n")

# 6. Peça números ao usuário até ele digitar "fim". Converta os valores para
# float e informe, ao final, quantos números foram digitados e qual foi o total.

contagem = 0
soma = 0

while True:
    insert = input("Digite um número, 'fim' para encerrar: ").strip().lower()
    if insert == 'fim':
        break
    numero = float(insert)
    soma += numero
    contagem += 1

print(f"Foram digitados {contagem} números, totalizando {soma:.2f}\n")

# 7. Peça uma idade até que ela esteja entre 0 e 120, inclusive. Depois, exiba
# a idade registrada. Dica: use `while idade < 0 or idade > 120`.

while True:
    idade = int(input("Informe a idade: "))
    if 0 <= idade <= 120:
        break
    print("Idade fora do range, tente novamente.")

print(f"Idade correta registrada: {idade}\n")

# 8. Use while para mostrar apenas os números pares de 2 até 20.

par = 2

while par <= 20:
    print(f"{par}")
    par += 2

print("\n")

# 9. Peça um número inteiro positivo e mostre a tabuada dele, do 1 ao 10,
# usando while.

while True:
    numero = int(input("Insira um número inteiro positivo: "))
    if numero > 0:
        break
    print("Número inválido. Tente novamente.")

contagem = 1

while contagem <= 10:
    print(f"{numero} x {contagem}: {numero * contagem}")
    contagem += 1

print("\n")

# 10. Comece com saldo igual a R$ 1.000. Peça valores de saque enquanto o saldo
# for maior que 0. Não permita saques negativos nem maiores que o saldo. Encerre
# quando o usuário digitar 0 ou quando o saldo acabar, mostrando o saldo final.

saldo = 1000
contagem = 0
soma = 0

while saldo > 0:
    saque = float(input("Digite o valor do saque, 0 para encerrar: "))
    if saque == 0:
        print("Saques encerrados.")
        break

    if saque < 0 or saque > saldo:
        saque = 'invalido'
        print("Valor de saque inválido!")
    
    if saque != 'invalido':
        saldo -= saque
        soma += saque
        contagem += 1

print(f"""Foram realizados {contagem} saques.
Valor sacado: R${soma:.2f}
Saldo final: R${saldo:.2f}
\n""")

# 11. Crie um sistema com no máximo 3 tentativas de senha. Se o usuário digitar
# "dados2026", exiba "Acesso liberado" e encerre o laço. Caso use as 3 tentativas
# sem acertar, exiba "Acesso bloqueado". Dica: contador e break podem ajudar.

tentativa = 1

while True:
    senha = input(f"Tentativa {tentativa}/3. Digite a senha: ")
    if senha == 'dados2026':
        print("Senha correta. Acesso liberado.\n")
        break
    if tentativa >= 3:
        print("Muitas tentativas. Acesso bloqueado.\n")
        break
    print(f"Senha incorreta. {3-tentativa} tentativas restantes.")
    tentativa +=1

# 12. Desafio — Resumo de vendas:
# Peça valores de vendas até o usuário digitar "fim". Ao final, mostre:
# - quantidade de vendas;
# - total vendido;
# - média das vendas.
# Se nenhuma venda for registrada, não calcule a média: exiba uma mensagem clara.

contagem = 0
soma = 0

while True:
    insert = input("Digite o valor da venda: ").strip().lower()
    if insert == 'fim':
        print("Cadastro encerrado. Resultado:")
        break
    valor = float(insert)
    soma += valor
    contagem += 1

if contagem == 0:
    print("Nenhuma venda registrada.\n")
else:
    print(f"""Foram realizadas {contagem} vendas.
    Valor total: R${soma:.2f}
    Média: R${(soma/contagem):.2f}
    \n""")