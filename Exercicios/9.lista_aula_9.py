# Aula 9 — Lista de exercícios: tuplas, conjuntos e dicionários
# Resolva os exercícios usando os conteúdos estudados até esta aula.

# 1. Crie uma tupla com os nomes dos cinco primeiros meses do ano. Imprima o
# primeiro mês, o último mês e a quantidade de itens da tupla.

cinco_meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio')

print(f"""1º Mês: {cinco_meses[0]}
Último Mês: {cinco_meses[-1]}
Quantidade de meses: {len(cinco_meses)}
\n""")

# 2. Crie a tupla ("Notebook", 3500.00, 8). Desempacote seus valores em três
# variáveis e exiba uma frase com o nome, o preço e a quantidade em estoque.

produto = ('Notebook', 3500.00, 8)
nome, preco, estoque = produto
print(f"Você escolheu {nome}, com valor R${preco:.2f}. Estoque disponível: {estoque}\n")

# 3. Crie uma tupla com cinco notas. Exiba a maior nota, a menor nota e a média.
# Depois, converta a tupla em lista, acrescente uma nova nota e exiba a lista.

notas = (2.5, 6.0, 7.8, 9.9, 5.0)

maior_nota = max(notas)
menor_nota = min(notas)
media_notas = sum(notas) / len(notas)

notas_lista = list(notas)
notas_lista.append(4.5)

print(f"""Resultado do semestre:
Notas registradas: {notas}
Maior nota: {maior_nota}
Menor nota: {menor_nota}
Média das notas: {media_notas:.1f}
Uma nota foi registrada, nova lista:
{notas_lista}
\n""")

# 4. Dada a lista ["SP", "RJ", "SP", "MG", "RJ", "BA"], crie um conjunto a
# partir dela. Exiba os estados únicos e a quantidade de estados diferentes.

estados = ["SP", "RJ", "SP", "MG", "RJ", "BA"]
estados_conj = set(estados)

print(f"""Estados únicos: {estados_conj}
Número de estados únicos: {len(estados_conj)}
\n""")

# 5. Considere os conjuntos abaixo:
# clientes_janeiro = {"Ana", "Bruno", "Carlos", "Daniela"}
# clientes_fevereiro = {"Bruno", "Carlos", "Eduardo", "Fernanda"}
# Exiba:
# - todos os clientes, sem repetição;
# - os clientes presentes nos dois meses;
# - os clientes que aparecem somente em janeiro.

clientes_janeiro = {"Ana", "Bruno", "Carlos", "Daniela"}
clientes_fevereiro = {"Bruno", "Carlos", "Eduardo", "Fernanda"}

clientes_unicos = clientes_janeiro | clientes_fevereiro
ambos_clientes = clientes_janeiro & clientes_fevereiro
jan_clientes = clientes_janeiro - clientes_fevereiro

print(f"""Clientes únicos: {clientes_unicos}
Clientes em ambos os meses: {ambos_clientes}
Clientes de Janeiro: {jan_clientes}
\n""")

# 6. Peça nomes de categorias ao usuário até que ele digite "fim". Armazene
# as categorias em um conjunto, ignorando maiúsculas, minúsculas e espaços nas
# extremidades. Ao final, exiba as categorias únicas e sua quantidade. Não
# adicione uma entrada vazia ao conjunto.

categorias = set()

while True:
    categoria = input("Informe uma categoria ('fim' para encerrar): ").strip().lower()

    if categoria.replace(',','.').replace('.','').replace('-','').replace(';','').isdigit() or categoria == '':
        print("Categoria inválida! Não informe números ou valores nulos.")
        continue

    if categoria == 'fim':
        break

    categorias.add(categoria)

if len(categorias) == 0:
    print("Nenhuma categoria registrada.\n")
else:
    print(f"{len(categorias)} Categorias registradas: {categorias}\n")

# 7. Crie um dicionário que represente um produto com as chaves "nome",
# "preco" e "estoque". Exiba cada informação usando sua respectiva chave.

inventario = {
    'nome': 'Café', 'preco': 45.50, 'estoque': 15
}

print(f"""Inventário:
Produto: {inventario['nome']}
Preço unitário: R${inventario['preco']:.2f}
Em estoque: {inventario['estoque']}
\n""")

# 8. Usando o dicionário do exercício anterior:
# - altere o preço;
# - adicione a chave "categoria";
# - remova a chave "estoque" com pop e guarde o valor removido;
# - exiba o dicionário atualizado e o estoque removido.

inventario['preco'] = 40.99
inventario['categoria'] = 'Alimentício'
chave_removida = inventario.pop('estoque')

print(f"""Inventário atualizado:
Estoque removido: {chave_removida}
Novo inventário: {inventario}
\n""")

# 9. Crie um dicionário com três categorias e seus respectivos totais de vendas.
# Percorra o dicionário com items e imprima uma linha para cada par no formato:
# "Categoria: livros | Total: R$ 1500.00".

vendas = {'livros': 2350.00, 'canetas': 810.30, 'papel': 930.00}

for chave, valor in vendas.items():
    print(f"Categoria: {chave} | Total: R${valor:.2f}")

print()

# 10. Dada a lista abaixo, conte quantas vendas existem em cada categoria e
# armazene o resultado em um dicionário. Não informe antecipadamente quais
# categorias existem; construa o contador durante o laço.
# categorias = ["livros", "casa", "livros", "eletrônicos", "casa", "livros"]

categorias = ["livros", "casa", "livros", "eletrônicos", "casa", "livros"]
vendido = {}

for item in categorias:
    if item in vendido:
        vendido[item] += 1
    else:
        vendido[item] = 1

print(f"""Vendas realizadas por categoria:
{vendido}
\n""")

# 11. Considere a lista de dicionários abaixo:
# produtos = [
#     {"nome": "Notebook", "preco": 3500.00, "estoque": 5},
#     {"nome": "Mouse", "preco": 80.00, "estoque": 20},
#     {"nome": "Monitor", "preco": 1200.00, "estoque": 8},
# ]
# Para cada produto, calcule preco * estoque. Exiba o nome e o valor total em
# estoque. Ao final, exiba a soma do valor em estoque de todos os produtos.

produtos = [
     {"nome": "Notebook", "preco": 3500.00, "estoque": 5},
     {"nome": "Mouse", "preco": 80.00, "estoque": 20},
     {"nome": "Monitor", "preco": 1200.00, "estoque": 8},
]

total_estoque = 0

for linha in produtos:
    valor_total = linha['preco'] * linha['estoque']
    print(f"{linha['nome']}: R${valor_total:.2f} em estoque.")
    total_estoque += valor_total

print(f"Valor total em estoque: R${total_estoque:.2f}\n")

# 12. Desafio — Resumo de vendas por categoria:
# Use a lista de dicionários abaixo:
# vendas = [
#     {"produto": "Notebook", "categoria": "eletrônicos", "valor": 3500.00},
#     {"produto": "Livro Python", "categoria": "livros", "valor": 120.00},
#     {"produto": "Monitor", "categoria": "eletrônicos", "valor": 1400.00},
#     {"produto": "Cadeira", "categoria": "móveis", "valor": 850.00},
#     {"produto": "Livro SQL", "categoria": "livros", "valor": 100.00},
# ]
# Produza um resumo contendo:
# - o total geral e a média das vendas;
# - o produto com o maior valor de venda;
# - um conjunto com as categorias presentes;
# - um dicionário com o total vendido por categoria;
# - a quantidade de vendas de cada categoria em outro dicionário.
# Construa os resultados percorrendo a lista. Não escreva antecipadamente os
# nomes das categorias nos dicionários de resumo.

vendas = [
     {"produto": "Notebook", "categoria": "eletrônicos", "valor": 3500.00},
     {"produto": "Livro Python", "categoria": "livros", "valor": 120.00},
     {"produto": "Monitor", "categoria": "eletrônicos", "valor": 1400.00},
     {"produto": "Cadeira", "categoria": "móveis", "valor": 850.00},
     {"produto": "Livro SQL", "categoria": "livros", "valor": 100.00},
]

total_vendas = 0
categorias = set()

for linha in vendas:
    total_vendas += linha['valor']
    categorias.add(linha['categoria'])

maior_venda = vendas[0]

for venda in vendas:
    if venda['valor'] > maior_venda['valor']:
        maior_venda = venda

vendas_cat = {}
qtd_vendas_cat = {}

for categoria in categorias:
    total_cat = 0
    qtd_cat = 0
    for linha in vendas:
        if categoria == linha['categoria']:
            total_cat += linha['valor']
            qtd_cat += 1
    vendas_cat[categoria] = total_cat
    qtd_vendas_cat[categoria] = qtd_cat

print(f"""Resumo de vendas:
Total de vendas: R${total_vendas:.2f} | Média: R${(total_vendas/len(vendas)):.2f}
Produto de maior venda: {maior_venda['produto']}
Categorias vendidas: {categorias}
Total vendido por categoria:
{vendas_cat}
Quantidade de vendas por categoria:
{qtd_vendas_cat}
\n""")