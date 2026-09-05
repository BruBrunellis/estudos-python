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
        if categoria in linha.values():
            total_cat += linha['valor']
            qtd_cat += 1
    vendas_cat['categoria'], vendas_cat['valor'] = categoria, total_cat
    qtd_vendas_cat['categoria'], qtd_vendas_cat['quantidade'] = categoria, qtd_cat

print(f"""Resumo de vendas:
Total de vendas: R${total_vendas:.2f} | Média: R${(total_vendas/len(vendas)):.2f}
Produto de maior venda: {maior_venda['produto']}
Categorias vendidas: {categorias}
Total vendido por categoria:
{vendas_cat}
Quantidade de vendas por categoria:
{qtd_vendas_cat}
\n""")