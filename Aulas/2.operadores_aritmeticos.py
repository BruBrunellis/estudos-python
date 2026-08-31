# Exemplos práticos de operadores aritméticos em Python
# Soma e multiplicação
preco = 49.90
quantidade = 3
frete = 12.50

total = preco * quantidade + frete
print(f"Total a pagar: R$ {total:.2f}\n")

# Divisão comum
total_alunos = 30
grupos = 5

alunos_por_grupo = total_alunos / grupos
print(f"Cada grupo terá {alunos_por_grupo:.0f} alunos.\n")

# Divisão inteira
minutos = 135
horas_completas = minutos // 60
print(f"Total de horas completas: {horas_completas}h\n")

# Resto da divisão
numero = 17
resto = numero % 2
print(f"O número {numero} é {'par' if resto == 0 else 'ímpar'}.\n")

# Potenciação
lado = 4
area = lado ** 2
print(f"A área do quadrado é: {area} unidades quadradas.\n")

# Raiz quadrada usando potenciação
numero = 16
raiz_quadrada = numero ** 0.5
print(f"A raiz quadrada de {numero} é: {raiz_quadrada}\n")

#Ordem de precedência dos operadores

# 1. Parênteses ()
# 2. Exponenciação **
# Multiplicação, divisão, divisão inteira e resto da divisão (*, /, //, %)
# 3. Adição e subtração (+, -)

resultado_1 = 2 + 3 * 4
print(f"Resultado de 2 + 3 * 4: {resultado_1}\n")  # Resultado: 14

resultado_2 = (2 + 3) * 4
print(f"Resultado de (2 + 3) * 4: {resultado_2}\n")  # Resultado: 20

# Operadores com atribuição
# Facilitam atualizar o valor de uma variável com base em seu valor atual.

saldo = 100
saldo += 50  # Equivalente a saldo = saldo + 50
print(f"Saldo após depósito: R$ {saldo:.2f}\n")

saldo -= 20  # Equivalente a saldo = saldo - 20
print(f"Saldo após saque: R$ {saldo:.2f}\n")

saldo *= 2 # Equivalente a saldo = saldo * 2
print(f"Saldo após dobrar: R$ {saldo:.2f}\n")

saldo /= 5 # Equivalente a saldo = saldo / 5
print(f"Saldo após dividir por 5: R$ {saldo:.2f}\n")

print (f"Saldo final: R$ {saldo:.2f}\n")

# Convertendo dados recebidos com input()

idade = int(input("Digite sua idade: "))
ano_nascimento = 2026 - idade
print(f"Você nasceu em {ano_nascimento}.\n")

# Para float

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    diagnostico = "Você está abaixo do peso ideal."
elif 18.5 <= imc < 24.9:
    diagnostico = "Você está com o peso ideal."
else:
    diagnostico = "Você está acima do peso ideal."

print(f"Seu IMC é: {imc:.2f}\n{diagnostico}\n")