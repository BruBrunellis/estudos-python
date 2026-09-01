# Aula 5 — Lista de exercícios: if, elif e else
# Resolva cada exercício e teste também casos de borda, como 0 e valores limites.

# 1. Peça a idade de uma pessoa e exiba "Maior de idade" se ela tiver 18 anos
# ou mais. Caso contrário, exiba "Menor de idade".

idade = int(input("Informe sua idade: "))

if idade >= 18:
    print("Maior de idade.\n")
else:
    print("Menor de idade.\n")

# 2. Peça um número inteiro e informe se ele é positivo, negativo ou zero.

numero = int(input("Digite um número: "))

if numero > 0:
    print("Número positivo.\n")
elif numero == 0:
    print("Número igual à zero.\n")
else:
    print("Número negativo.\n")

# 3. Peça duas notas, calcule a média e informe se o aluno foi aprovado
# (média maior ou igual a 7) ou reprovado.

nota_1 = float(input("Informe a 1ª nota (0 a 10): "))
nota_2 = float(input("Informe a 2ª nota (0 a 10): "))

media = (nota_1 + nota_2) / 2

if media >= 7:
    print("Aprovado.\n")
else:
    print("Reprovado.\n")

# 4. Peça a temperatura em Celsius e classifique-a assim:
# abaixo de 15: "Frio";
# de 15 até 29: "Agradável";
# 30 ou mais: "Quente".

temp = float(input("Informe a temperatura em Celsius: "))

if temp < 15:
    print("Frio\n")
elif 15 <= temp <=29:
    print("Agradável\n")
else:
    print("Quente\n")

# 5. Peça o preço de um produto. Se o preço for maior que R$ 100, aplique 10%
# de desconto; caso contrário, aplique 5%. Exiba o valor final com duas casas.

preco = float(input("Informe o preço em R$0.00: "))

if preco > 100:
    desconto = 0.9
else:
    desconto = 0.95

preco_com_desconto = preco * desconto 

print(f"O preço do produto com desconto é: R${preco_com_desconto:.2f}\n")

# 6. Peça um ano e informe se ele é bissexto. Considere bissexto todo ano
# divisível por 4. (A regra completa será vista como desafio no exercício 12.)

ano = int(input("Informe um ano: "))

if (ano % 4) == 0:
    print("Ano é bissexto.\n")
else:
    print("Ano não é bissexto.\n")

# 7. Peça um nome de usuário. Se ele tiver menos de 3 caracteres após remover
# espaços das pontas, informe que é inválido; caso contrário, informe que é válido.

usuario = input("Informe seu nome de usuário: ")

if len(usuario.strip()) < 3:
    print("Usuário inválido! Insira nome com pelo menos 3 caracteres.\n")
else:
    print("Nome de usuário válido!\n")

# 8. Peça uma sigla de região. Se for "N", "NE", "CO", "SE" ou "S", informe
# "Região válida"; caso contrário, informe "Região inválida". Ignore diferenças
# entre maiúsculas e minúsculas.

regioes_validas = ["N", "NE", "CO", "SE", "S"]

regiao = input("Informe uma região (ex. CO): ").strip().upper()

if regiao in regioes_validas:
    print("Região válida\n")
else:
    print("Região inválida!\n")

# 9. Peça o valor de uma venda e classifique-a em:
# "Baixa" para valores menores que 500;
# "Média" para valores de 500 até menos de 1000;
# "Alta" para valores de 1000 ou mais.

venda = float(input("Insira o valor da venda em R$0.00: "))

if venda <500:
    print("Baixa\n")
elif 500 <= venda < 1000:
    print("Média\n")
else:
    print("Alta\n")

# 10. Peça um e-mail. Se ele contiver "@" E terminar com ".com", exiba
# "E-mail com formato aceito"; caso contrário, exiba "E-mail com formato inválido".
# Atenção: isto é uma validação simples, não completa.

email = input("Informe seu endereço de e-mail: ").strip()

if '@' in email and email.endswith('.com'):
    print("E-mail com formato aceito.\n")
else:
    print("E-mail com formato inválido.\n")

# 11. Peça a idade e informe se a pessoa pode receber uma gratuidade:
# menores de 6 anos e pessoas com 60 anos ou mais recebem gratuidade;
# os demais não recebem. Não aceite idades negativas.

idade = int(input("Informe sua idade: "))

if idade < 0:
    print("Idade inválida!\n")
elif idade < 6 or idade >= 60:
    print("Pode receber gratuidade!\n")
else:
    print("Não pode receber gratuidade.\n")

# 12. Desafio — Ano bissexto completo:
# Um ano é bissexto se for divisível por 4, exceto os divisíveis por 100;
# porém, os divisíveis por 400 continuam sendo bissextos. Peça um ano e informe
# se ele é bissexto. Dica: use %, and, or e parênteses para organizar a regra.

ano = int(input("Informe um ano: "))

if ((ano % 4) == 0) and ((ano % 100) != 0) or ((ano % 400) == 0):
    print("Ano é bissexto.\n")
else:
    print("Ano não é bissexto.\n")