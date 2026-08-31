# Crie duas variáveis com números e mostre a soma, subtração, multiplicação e divisão entre elas.

var1 = 10
var2 = 5

soma = var1 + var2
subtracao = var1 - var2
multiplicacao = var1 * var2
divisao = var1 / var2

print(f"Resultado das operações entre {var1} e {var2}:\n",
      f"Soma: {soma}, {type(soma)}\n",
      f"Subtração: {subtracao}, {type(subtracao)}\n",
      f"Multiplicação: {multiplicacao}, {type(multiplicacao)}\n",
      f"Divisão: {divisao}, {type(divisao)}\n"
)

# Peça dois números ao usuário e mostre o resultado da potência do primeiro elevado ao segundo.

var1 = int(input("Insira um número: "))
var2 = int(input("Insira outro número: "))

exp = var1 ** var2

print(f"Resultado de {var1} elevando à {var2}: {exp}\n")

# Peça a idade de uma pessoa e calcule em que ano ela nasceu, considerando o ano atual como 2026.

idade = int(input("Digite sua idade: "))

nascimento = 2026 - idade

print(f"Seu ano de nascimento é: {nascimento}\n")

# Peça o preço de um produto e sua quantidade. Mostre o valor total da compra.

preco = float(input("Digite o valor do produto 0.00: "))
quantidade = int(input("Digite a quantidade: "))

valor_total = preco * quantidade

print(f"O valor total da compra é de R${valor_total:.2f}\n")

# Peça uma quantidade de minutos e informe quantas horas completas existem e quantos minutos restam.

minutos = int(input("Digite uma quantidade de minutos: "))

hora_int = minutos // 60

mins_rest = minutos % 60

print(f"{minutos} minutos equivalem à {hora_int} horas e {mins_rest} minutos.\n")

# Peça um número inteiro e informe se ele é par ou ímpar.

var1 = int(input("Digite um número inteiro: "))

if var1 % 2 == 0:
    resultado = "par"
else:
    resultado = "ímpar"

print(f"O número {var1} é {resultado}.\n")

# Peça a temperatura em graus Celsius e converta para Fahrenheit:

celsius = float(input("Digite uma temperatura em celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius} ºC equivalem à {fahrenheit} fahrenheit.\n")

# Peça a largura e a altura de um retângulo. Calcule sua área e seu perímetro.

altura = int(input("Digite a altura do retângulo: "))
largura = int(input("Digite a largura retângulo: "))

area = altura * largura
perimetro = altura * 2 + largura * 2

print(f"O retângulo {largura}x{altura} possui área de {area} u e perímetro de {perimetro} u\n")

# Peça peso e altura de uma pessoa e calcule o IMC.

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

if imc > 24.9:
    diagnostico = "Você está acima do peso."
elif 18.5 <= imc <= 24.9:
    diagnostico = "Você está no peso ideal."
else:
    diagnostico = "Você está abaixo do peso."

print(f"""Seu IMC é: {imc:.2f}
{diagnostico}\n""")

# Uma loja oferece 10% de desconto. Peça o preço do produto e exiba o preço final.

preco = float(input("Insira o preço do produto (0.00): "))

preco_descontado = preco * (1-0.1)

print(f"O preço com 10% de desconto é: R${preco_descontado:.2f}\n")

# Peça o valor total de uma conta e a quantidade de pessoas que irão pagar. Informe quanto cada pessoa deve pagar.

valor_total = float(input("Informe o valor da conta (0.00): "))
pessoas = int(input("Informe quantas pessoas vão pagar: "))

if pessoas == 0:
    print("Informe pelo menos 1 pessoa para pagar")
else:

    particao = valor_total / pessoas

    print(f"Cada pessoa irá pagar R${particao:.2f}\n")

# Desafio: peça uma quantidade de segundos e converta para horas, minutos e segundos restantes usando // e %.

segundos = int(input("Digite uma quantidade de segundos: "))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_rest = (segundos % 3600) % 60

print(f"{segundos} segundos equivalem à {horas}h:{minutos}min e {segundos_rest} segundos.\n")