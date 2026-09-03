# Aula 7 — Lista de exercícios: for e range
# Use for sempre que a quantidade de repetições ou a sequência a percorrer for conhecida.

# 1. Use for e range para imprimir os números de 1 a 10, um por linha.

for numero in range(1,11):
    print(numero)

print()

# 2. Imprima os números pares de 0 até 20 usando range com passo 2.

for par in range(0,21,2):
    print(par)

print()

# 3. Imprima uma contagem regressiva de 10 até 1. Ao final, imprima "Fogo!".

print("Contagem regressiva...")
for contagem in range(10,0,-1):
    print(contagem)

print("Fogo!\n")

# 4. Peça um número inteiro positivo e mostre a tabuada dele, de 1 a 10,
# usando for e range.

while True:

    numero = int(input("Insira um número inteiro positivo: "))

    if numero <= 0:
        print("Número inválido. Tente novamente.")
        continue

    for multi in range(1,11):
        print(f"{numero} x {multi}: {numero * multi}")
    break

print()

# 5. Calcule e imprima a soma dos números inteiros de 1 até 100 usando for.

soma = 0

for i in range(1,101):
    soma += i

print(f"Soma de inteiros de 1 a 100: {soma}\n")

# 6. Peça uma palavra ao usuário e imprima cada caractere em uma linha.

palavra = input("Insira uma palavra: ")

for carac in palavra:
    print(carac)

print()

# 7. Peça uma frase e conte quantas letras "a" ela possui, sem diferenciar
# "a" de "A". Dica: padronize a frase com lower() antes do for.

frase = input("Insira uma frase: ").lower()
num_a = 0

for i in frase:
    if i == 'a':
        num_a += 1

print(f"A frase possui {num_a} letras 'a'.\n")

# 8. Peça um número inteiro positivo e calcule o fatorial dele. Por exemplo,
# 5! é igual a 5 * 4 * 3 * 2 * 1. Dica: comece o acumulador em 1.

while True:

    entrada = input("Insira um número inteiro positivo: ")

    if not entrada.isdigit() or int(entrada) <= 0:
        print("Número inválido! Tente novamente.")
        continue

    numero = int(entrada)
    fatorial = 1
    
    for i in range (1, numero + 1):
        fatorial *= i
    break

print(f"O resultado de {numero}! é: {fatorial}\n")

# 9. Peça um número inteiro e imprima todos os seus divisores positivos.
# Dica: teste os números de 1 até o próprio número com o operador %.

while True:

    entrada = input("Insira um número inteiro: ")

    if not entrada.isdigit():
        print("Número inválido! Tente novamente.")
        continue

    numero = int(entrada)
    print (f"Divisores positivos de {numero}:")    

    for i in range (1, numero + 1):
        if numero % i == 0:
            print(f"{i} | Resultado: {int(numero/i)}")
    break

print()

# 10. Imprima os números de 1 a 30. Para múltiplos de 3, imprima "Fizz" no
# lugar do número; para múltiplos de 5, imprima "Buzz"; e para múltiplos de
# ambos, imprima "FizzBuzz". Atenção à ordem dos ifs.

for i in range(1,31):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

print()
    
# 11. Peça cinco valores de vendas ao usuário. Calcule e exiba o total e a
# média. Dica: use um acumulador e range(1, 6).

total = 0

for i in range(1,6):
    while True:
        venda = input(f"Insira o valor da {i}ª venda: ").replace(',','.')

        if venda.count('.') <= 1 and venda.replace('.','').isdigit() and venda != '' and float(venda) > 0:
            valor = float(venda)
            total += valor
            break
        else:
            print("Valor inválido! Tente novamente.")

media = total / 5

print(f"5 vendas realizadas, no total de R${total:.2f} e média de R${media:.2f}\n")

# 12. Desafio — Análise simples de vendas:
# Peça a quantidade de vendas a registrar. Para cada venda, peça o valor e:
# - acumule o total;
# - conte quantas foram maiores ou iguais a R$ 1.000;
# - ao final, informe o total, a média e a quantidade de vendas altas.
# Se a quantidade informada for 0 ou negativa, informe que ela é inválida.

while True:
    entrada = input("Informe a quantidade de vendas a registrar: ")

    if not entrada.isdigit() or int(entrada) == 0 or int(entrada) < 0:
        print("Valor inválido! Informe pelo menos 1 venda a registrar.")
        continue
    break

contagem = int(entrada)
total = 0
cont_vendas = 0
cont_altas = 0

for i in range(1, contagem + 1):
    while True:
        venda = input(f"Insira o valor da {i}ª venda: ").replace(',','.')

        if venda.count('.') <= 1 and venda.replace('.','').isdigit() and venda != '' and float(venda) > 0:
            valor = float(venda)
            total += valor
            cont_vendas += 1
            if valor >= 1000:
                cont_altas += 1
            break
        else:
            print("Valor inválido! Tente novamente.")

media = total / cont_vendas

print(f"""Foram registradas {cont_vendas} vendas:
Valor total: R${total:.2f}
Vendas acima de $1.000,00: {cont_altas}
Média: R${media:.2f}
\n""")