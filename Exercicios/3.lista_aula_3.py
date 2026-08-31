# Aula 3 — Lista de exercícios: strings e formatação
# Resolva cada exercício abaixo. Teste seu programa com valores diferentes.

# 1. Crie uma variável chamada nome com seu nome e imprima uma mensagem de boas-vindas.

nome = 'Bruno'

print(f"Olá, {nome}! Seja bem-vindo!\n")

# 2. Crie as variáveis primeiro_nome e sobrenome. Una-as em uma variável
# chamada nome_completo e exiba o resultado.

primeiro_nome = 'Bruno'
sobrenome = 'Brunelli'

nome_completo = primeiro_nome + ' ' + sobrenome

print(f"Nome completo: {nome_completo}\n")

# 3. Crie uma variável com o nome de uma cidade. Mostre:
#    a) a cidade toda em letras maiúsculas;
#    b) a cidade toda em letras minúsculas;
#    c) quantos caracteres ela possui.

cidade = 'São Paulo'

print(cidade.upper())
print(cidade.lower())
print(f"{cidade} possui {len(cidade)} caracteres.\n")

# 4. Peça o nome do usuário com input() e exiba: "Olá, <nome>!" usando f-string.

user = input("Qual seu nome?: ")

print(f"Olá, {user}!\n")

# 5. Peça uma frase e informe a quantidade de caracteres dela usando len().
# Dica: espaços também contam como caracteres.

frase = input("Escreva uma frase: ")

print(f"A frase possui {len(frase)} caracteres.\n")

# 6. Crie a string "Python para Dados" e imprima:
#    a) o primeiro caractere;
#    b) o último caractere;
#    c) a palavra "Python" usando fatiamento.

string = 'Python para Dados'

print(string[0])
print(string[-1])
print(f"{string[:6]}\n")

# 7. Peça um nome completo e exiba somente o primeiro nome.
# Dica: use split().

nome = input("Digite seu nome completo: ")

nome_list = nome.split()

print(f"Seu primeiro nome é {nome_list[0]}")

# 8. Uma pessoa digitou seu nome com espaços extras: "  joão da silva  ".
# Crie uma variável com esse texto e gere outra variável contendo o nome sem
# espaços nas pontas e com iniciais maiúsculas.

nome = ' joão da silva '

nome_padrao = nome.strip().title()

print(f"{nome_padrao}\n")

# 9. Peça o nome de um produto, seu preço e a quantidade comprada. Exiba uma
# mensagem bem formatada contendo o produto e o total em reais com duas casas.

produto = input("Informe o produto: ")
preco = float(input("Informe o preço em R$0.00: "))
quantidade = int(input("Informe a quantidade: "))
valor_total = preco * quantidade

print(f"Você adquiriu {quantidade} unidades de {produto}, totalizando R${valor_total:.2f}\n")

# 10. Crie uma variável com três categorias separadas por vírgula, por exemplo:
# "alimentação,transporte,lazer". Transforme-a em uma lista e imprima cada
# categoria em uma linha usando um for.

categorias = 'imóveis,ações,aposentadoria'
categorias_list = categorias.split(',')

for index, item in enumerate(categorias_list):
    print(f"{index + 1}ª categoria: {item}")

print("\n")


# 11. Peça um endereço de e-mail e informe se ele termina com ".com".
# Dica: use endswith().

email = input("Informe seu email: ")

check = email.strip().endswith('.com')

if check:
    print("Endereço de e-mail válido!\n")
else:
    print("Endereço de e-mail incorreto, verifique erros.\n")

# 12. Desafio — Padronização de dados:
# Crie uma lista com os valores ["  ANA", "bruno  ", " CaRLa "]. Percorra a
# lista e crie uma nova lista em que todos os nomes estejam sem espaços extras
# e com apenas as iniciais em maiúsculas. Ao final, imprima a nova lista.

lista = ["  ANA", "bruno  ", " CaRLa "]
lista_formatada = []

for item in lista:
    item_formatado = item.strip().lower().title()
    lista_formatada.append(item_formatado)

print(lista_formatada)