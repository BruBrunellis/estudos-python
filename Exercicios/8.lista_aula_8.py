# Aula 8 — Lista de exercícios: listas
# Resolva os exercícios usando os conteúdos estudados até esta aula.

# 1. Crie uma lista com cinco nomes de produtos e imprima a lista completa.

produtos = ['Café', 'Leite Condensado', 'Maionese', 'Achocolatado', 'Manteiga']
print(f"Produtos em estoque: {produtos}\n")

# 2. Crie uma lista com cinco números. Imprima o primeiro item, o terceiro item
# e o último item usando índices.

numeros = [23, 9, 17, 45, 80]

print(numeros[0])
print(numeros[2])
print(numeros[-1])
print()

# 3. Crie a lista [10, 20, 30, 40, 50] e imprima, por fatiamento:
# - os três primeiros valores;
# - os três últimos valores;
# - os valores 20, 30 e 40.

lista = [10, 20, 30, 40, 50]

print(lista[:3])
print(lista[2:])
print(lista[1:4])
print()

# 4. Crie uma lista com três cidades. Substitua a segunda cidade por outra,
# adicione uma cidade ao final e insira uma cidade no início. Exiba o resultado.

cidades = ['São Paulo', 'Paris', 'Nova Iorque']
cidades[1] = 'Roma'
cidades.append('Praga')
cidades.insert(0, 'Moscow')
print(cidades)
print()

# 5. Crie uma lista de tarefas com quatro itens. Remova um item pelo seu valor
# e remova o último com pop. Exiba também o item devolvido por pop.

tarefas = ['Lavar louça', 'Varrer o chão', 'Estender roupas', 'Fazer almoço']
tarefas.remove('Varrer o chão')
realizado = tarefas.pop()

print(f"""Tarefa realizada: {realizado}.
Tarefas pendentes: {tarefas}
\n""")

# 6. Peça ao usuário o nome de um produto. Informe se ele está cadastrado na
# lista ["notebook", "mouse", "teclado", "monitor"]. Ignore maiúsculas e
# minúsculas na pesquisa.

estoque = ['notebook', 'mouse', 'teclado', 'monitor']
produto = input("Informe o produto desejado: ").strip().lower()

if produto in estoque:
    print("Produto em estoque!\n")
else:
    print("Produto fora de estoque!\n")

# 7. Dada a lista de notas [7.5, 8.0, 6.5, 9.0, 8.0], percorra todos os itens
# e imprima cada nota. Depois, informe quantas vezes a nota 8.0 aparece.

notas = [7.5, 8.0, 6.5, 9.0, 8.0]
nota_oito = 0

for i in notas:
    print(i)
    if i == 8.0:
        nota_oito += 1

print(f"A nota 8.0 aparece {nota_oito} vezes.\n")

# 8. Dada a lista de vendas [450.0, 1250.0, 890.0, 2100.0, 670.0], calcule e
# exiba o total, a média, a menor venda e a maior venda.

vendas = [450.0, 1250.0, 890.0, 2100.0, 670.0]
total = sum(vendas)
media = total / len(vendas)
menor = min(vendas)
maior = max(vendas)

print(f"""Resultado das vendas:
{len(vendas)} realizadas.
Valor total: R${total:.2f}
Média: R${media:.2f}
Menor venda: R${menor:.2f}
Maior venda: R${maior:.2f}
\n""")

# 9. Peça cinco números ao usuário e armazene todos em uma lista. Depois,
# exiba a lista na ordem informada e em ordem crescente. Preserve a lista
# original ao fazer a ordenação.

numeros = []

for i in range(5):
    while True:
        numero = input("Insira um número: ").replace(',','.')
        if (numero.count('.') <= 1 and
            numero.count('-') <= 1 and
            numero.find('-') <= 0 and
            numero.replace('.','').replace('-','').isdigit() and numero != ''):
            numeros.append(float(numero))
            break
        else:
            print("Valor inválido! Insira um número.")

numeros_ord = sorted(numeros)

print(f"""Lista original: {numeros}
Lista ordenada: {numeros_ord}
\n""")

# 10. Dada a lista de vendas [850.0, 1200.0, 430.0, 1560.0, 960.0], crie uma
# nova lista somente com as vendas maiores ou iguais a R$ 1.000,00. Faça isso
# usando for, if e append. Exiba as duas listas.

vendas = [850.0, 1200.0, 430.0, 1560.0, 960.0]

vendas_maior = []

for i in vendas:
    if i >= 1000:
        vendas_maior.append(i)

print(f"""Lista completa de vendas: {vendas}
Vendas de pelo menos R$1.000,00: {vendas_maior}
\n""")

# 11. Peça ao usuário a quantidade de notas que serão registradas. Valide para
# aceitar somente uma quantidade inteira maior que zero. Depois, leia cada
# nota, armazene-a em uma lista e exiba a média. Aceite somente notas entre
# 0 e 10.

while not ((qtd_notas := input("Informe a quantidade de notas a registrar: ")).isdigit() and int(qtd_notas) > 0):
    print("Valor inválido! Digite um número.")

qtd_notas = int(qtd_notas)
notas = []

for i in range(qtd_notas):
    while not ((nota := input("Informe a nota (0 a 10): ").replace(',','.')).count('.') <= 1 and
               nota.replace('.','').isdigit() and nota != '' and
               0 <= float(nota) <=10):
        print("Valor inválido! Digite uma nota (0 a 10).")
    nota = float(nota)
    notas.append(nota)

media_notas = sum(notas) / qtd_notas

print(f"""{qtd_notas} notas registradas:
{notas}
Média das notas: {media_notas:.2f}
\n""")

# 12. Desafio — Análise simples de vendas:
# Peça a quantidade de vendas que será registrada e valide para aceitar somente
# um número inteiro maior que zero. Armazene cada valor em uma lista e, ao final:
# - exiba a lista completa;
# - calcule total, média, menor e maior venda;
# - crie e exiba uma nova lista com as vendas acima da média;
# - informe quantas vendas foram maiores ou iguais a R$ 1.000,00;
# - exiba os valores em ordem decrescente sem alterar a lista original.
# Considere válidos apenas valores de venda maiores que zero.

while not ((qtd_vendas := input("Informe a quantidade vendas a registrar: ")).isdigit() and int(qtd_vendas) > 0):
    print("Valor inválido! Informe pelo menos uma venda a ser registrada.")

qtd_vendas = int(qtd_vendas)
vendas = []

for i in range(qtd_vendas):
    while not ((venda := input("Informe a venda em R$: ").replace(',','.')).count('.') <= 1 and
                   venda.replace('.','').isdigit() and venda != '' and
                   float(venda) > 0):
        print("Valor inválido! Informe o valor em R$, acima de 0.")
    venda = float(venda)
    vendas.append(venda)

total_vendas = sum(vendas)
media_vendas = total_vendas / len(vendas)
maior_venda = max(vendas)
menor_venda = min(vendas)

acima_media = []

for i in vendas:
    if i > media_vendas:
        acima_media.append(i)

top_vendas = []

for i in vendas:
    if i >= 1000:
        top_vendas.append(i)

vendas_ord = sorted(vendas, reverse = True)

print(f"""Resultado das vendas:
{qtd_vendas} vendas registradas: {vendas}
Valor total: R${total_vendas:.2f}
Média das vendas: R${media_vendas:.2f}
Maior venda: R${maior_venda:.2f} | Menor venda: R${menor_venda:.2f}
Vendas acima da média: {acima_media}
Nº de vendas de pelo menos R$1.000,00 : {len(top_vendas)}
Vendas em ordem decrescente: {vendas_ord}
\n""")