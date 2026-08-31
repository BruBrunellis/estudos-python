# Aula 3 — Strings e formatação
#
# Objetivo: criar, acessar, transformar e formatar textos em Python.
# Pré-requisitos: variáveis, tipos básicos, operadores e input().

# Uma string (str) é uma sequência de caracteres: letras, números, espaços e
# símbolos. Ela pode ser criada com aspas simples ou duplas.
nome = "Marina"
cidade = 'São Paulo'
print(nome)
print(cidade)

# Escolha aspas que evitem escapes desnecessários.
frase_com_aspas = 'Ela disse: "Olá!"'
print(frase_com_aspas)

# Caracteres especiais começam com barra invertida.
mensagem = "Olá, Marina!\nBem-vinda à Aula 3."
print(mensagem)

# Concatenação (+) junta textos e repetição (*) repete uma string.
primeiro_nome = "Ana"
sobrenome = "Silva"
nome_completo = primeiro_nome + " " + sobrenome
print(nome_completo)
print("-" * 30)

# Para misturar texto e variáveis, prefira f-strings.
idade = 24
apresentacao = f"Meu nome é {nome_completo} e tenho {idade} anos."
print(apresentacao)

# F-strings também permitem formatar números.
preco = 19.9
quantidade = 3
print(f"Total: R$ {preco * quantidade:.2f}")

# len() informa a quantidade de caracteres, incluindo espaços.
produto = "Caderno"
print(f"'{produto}' possui {len(produto)} caracteres.")

# Índices começam em 0. Índices negativos contam a partir do final.
codigo = "PYTHON-2026"
print(codigo[0])   # P
print(codigo[3])   # H
print(codigo[-1])  # 6

# Fatiamento (slicing) seleciona partes de uma string: texto[inicio:fim].
# O caractere da posição 'fim' não é incluído.
print(codigo[0:6])  # PYTHON
print(codigo[7:])   # 2026
print(codigo[:6])   # PYTHON

# Strings são imutáveis: não se altera um caractere diretamente.
# codigo[0] = "p"  # Isso geraria erro.
# Em vez disso, crie uma nova string.
codigo_minusculo = codigo.lower()
print(codigo_minusculo)

# Métodos comuns devolvem uma nova string transformada.
texto = "  análise de dados com python  "
print(texto.upper())
print(texto.title())
print(texto.strip())  # Remove espaços no começo e no fim.
print(texto.strip().replace("python", "Python"))

# split() separa um texto em uma lista; join() une itens com um separador.
categorias = "alimentação,transporte,lazer"
lista_categorias = categorias.split(",")
print(lista_categorias)
print(" | ".join(lista_categorias))

# Verificações úteis retornam True ou False.
email = "aluna@email.com"
print(email.endswith(".com"))
print("@" in email)

# Ponte para análise de dados:
# Dados de texto quase sempre precisam ser padronizados antes da análise.
cliente_bruto = "  maria da silva  "
cliente_padronizado = cliente_bruto.strip().title()
print(f"Cliente padronizado: {cliente_padronizado}")

# Erros comuns:
# - Somar texto e número diretamente: "Idade: " + 20 gera TypeError.
#   Use f"Idade: {20}" ou converta o número com str(20).
# - Pedir uma posição que não existe: "oi"[5] gera IndexError.
# - Esquecer que upper(), lower() e replace() não modificam a variável original.
# - Usar + para muitas partes de texto; f-strings geralmente ficam mais legíveis.
