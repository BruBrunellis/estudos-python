# Aula 9 — Tuplas, conjuntos e dicionários
#
# Objetivo: escolher e usar a estrutura adequada para diferentes tipos de
# informação: sequências fixas, valores únicos e registros com chave e valor.
# Pré-requisitos: listas, índices, condicionais e laços for e while.

# RESUMO DAS ESTRUTURAS
#
# lista:      ordenada, mutável e permite valores repetidos;
# tupla:      ordenada, imutável e permite valores repetidos;
# conjunto:   não mantém uma posição fixa e não permite valores repetidos;
# dicionário: armazena pares formados por chave e valor.

# -----------------------------------------------------------------------------
# 1. TUPLAS
# -----------------------------------------------------------------------------

# Uma tupla é escrita com valores separados por vírgulas, normalmente entre
# parênteses. Ela é indicada quando os valores não devem ser alterados.
meses_trimestre = ("janeiro", "fevereiro", "março")
print(meses_trimestre)
print(f"Primeiro mês: {meses_trimestre[0]}")
print(f"Último mês: {meses_trimestre[-1]}")
print(f"Primeiros dois meses: {meses_trimestre[:2]}\n")

# Tuplas podem ser percorridas da mesma maneira que listas.
for mes in meses_trimestre:
    print(mes)

print()

# Uma tupla com apenas um item precisa de uma vírgula.
tupla_com_um_item = ("dados",)
print(f"Tipo de ('dados',): {type(tupla_com_um_item)}\n")

# Desempacotamento distribui os valores da tupla entre variáveis.
produto = ("Notebook", 3500.00, 8)
nome, preco, estoque = produto
print(f"Produto: {nome}")
print(f"Preço: R$ {preco:.2f}")
print(f"Estoque: {estoque}\n")

# Tuplas são imutáveis. Uma instrução como produto[1] = 3400 causaria
# TypeError. Quando uma alteração for necessária, use uma lista ou converta.
produto_lista = list(produto)
produto_lista[1] = 3400.00
produto_atualizado = tuple(produto_lista)
print(f"Tupla original: {produto}")
print(f"Nova tupla: {produto_atualizado}\n")

# -----------------------------------------------------------------------------
# 2. CONJUNTOS (SETS)
# -----------------------------------------------------------------------------

# Um conjunto armazena somente valores únicos.
# A ordem exibida pode variar, portanto não devemos depender das posições.
categorias = {"livros", "eletrônicos", "casa", "livros"}
print(f"Categorias sem repetição: {categorias}")

# set() cria um conjunto vazio. {} cria um dicionário vazio.
clientes_unicos = set()
clientes_unicos.add("Ana")
clientes_unicos.add("Bruno")
clientes_unicos.add("Ana")
print(f"Clientes únicos: {clientes_unicos}")
print(f"Quantidade de clientes únicos: {len(clientes_unicos)}\n")

# remove gera erro quando o valor não existe; discard não gera esse erro.
clientes_unicos.discard("Carlos")
clientes_unicos.remove("Bruno")
print(f"Após as remoções: {clientes_unicos}\n")

# Operações entre conjuntos são úteis para comparar grupos.
clientes_janeiro = {"Ana", "Bruno", "Carlos"}
clientes_fevereiro = {"Bruno", "Carlos", "Daniela"}

todos_clientes = clientes_janeiro | clientes_fevereiro # '|' união
clientes_nos_dois_meses = clientes_janeiro & clientes_fevereiro # '&' intersecção
somente_em_janeiro = clientes_janeiro - clientes_fevereiro # '-' diferença

print(f"União: {todos_clientes}")
print(f"Interseção: {clientes_nos_dois_meses}")
print(f"Diferença: {somente_em_janeiro}\n")

# Uma lista pode ser convertida em conjunto para eliminar duplicidades.
cidades = ["SP", "RJ", "SP", "MG", "RJ"]
cidades_unicas = set(cidades)
print(f"Cidades registradas: {cidades}")
print(f"Cidades únicas: {cidades_unicas}\n")

# -----------------------------------------------------------------------------
# 3. DICIONÁRIOS
# -----------------------------------------------------------------------------

# Um dicionário associa cada chave a um valor.
# As chaves devem ser únicas e descrevem o significado dos dados.
venda = {
    "produto": "Notebook",
    "quantidade": 2,
    "preco_unitario": 3500.00,
}

print(venda)
print(f"Produto vendido: {venda['produto']}")
print(f"Quantidade: {venda['quantidade']}\n")

# Atribuir um valor a uma chave existente atualiza o dado.
# Atribuir a uma chave nova adiciona essa informação ao dicionário.
venda["quantidade"] = 3
venda["vendedor"] = "Marina"
print(f"Venda atualizada: {venda}\n")

# Acesso com [] gera KeyError se a chave não existir.
# get permite fornecer um valor padrão e evita esse erro.
desconto = venda.get("desconto", 0.0)
print(f"Desconto: R$ {desconto:.2f}\n")

# in verifica a existência de uma chave no dicionário.
if "vendedor" in venda:
    print(f"Vendedor encontrado: {venda['vendedor']}\n")

# pop remove uma chave e devolve o valor associado a ela.
vendedor_removido = venda.pop("vendedor")
print(f"Vendedor removido: {vendedor_removido}")
print(f"Dicionário atual: {venda}\n")

# keys retorna as chaves, values retorna os valores e items retorna os pares.
produto = {
    "nome": "Monitor",
    "preco": 1200.00,
    "estoque": 15,
}

print(f"Chaves: {list(produto.keys())}")
print(f"Valores: {list(produto.values())}")

for chave, valor in produto.items():
    print(f"{chave}: {valor}")

print()

# Um dicionário também pode funcionar como contador de ocorrências.
categorias_vendidas = ["livros", "casa", "livros", "eletrônicos", "livros"]
contagem_categorias = {}

for categoria in categorias_vendidas:
    if categoria in contagem_categorias:
        contagem_categorias[categoria] += 1
    else:
        contagem_categorias[categoria] = 1

print(f"Contagem por categoria: {contagem_categorias}\n")

# -----------------------------------------------------------------------------
# PONTE PARA ANÁLISE DE DADOS
# -----------------------------------------------------------------------------

# Uma lista de dicionários pode representar uma tabela:
# cada dicionário é uma linha e cada chave representa uma coluna.
vendas = [
    {"produto": "Notebook", "categoria": "eletrônicos", "valor": 3500.00},
    {"produto": "Livro Python", "categoria": "livros", "valor": 120.00},
    {"produto": "Monitor", "categoria": "eletrônicos", "valor": 1400.00},
]

total_vendas = 0.0
categorias_presentes = set()

for registro in vendas:
    total_vendas += registro["valor"]
    categorias_presentes.add(registro["categoria"])

print(f"Total das vendas: R$ {total_vendas:.2f}")
print(f"Categorias presentes: {categorias_presentes}")

# Mais adiante, um DataFrame do pandas organizará dados de maneira semelhante,
# porém com ferramentas próprias para filtrar, agrupar e resumir tabelas.

# Erros comuns:
# - tentar alterar um item de uma tupla;
# - esquecer a vírgula ao criar uma tupla com apenas um item;
# - tentar acessar um conjunto por índice;
# - usar {} esperando criar um conjunto vazio;
# - usar remove em um conjunto sem verificar se o valor existe;
# - acessar uma chave inexistente com [] e causar KeyError;
# - confundir a chave com o valor ao percorrer um dicionário.

# Boas práticas:
# - use tuplas para dados ordenados que não devem mudar;
# - use conjuntos para eliminar duplicidades e comparar grupos;
# - use dicionários para representar dados identificados por nomes;
# - prefira nomes claros e consistentes para as chaves dos dicionários;
# - use get quando a chave puder estar ausente.
