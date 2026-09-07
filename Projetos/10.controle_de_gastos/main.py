# Aula 10 — Mini-projeto: controle de gastos pessoais
#
# Leia todos os requisitos no README.md desta pasta antes de começar.
# Implemente o projeto abaixo deste comentário, dividindo o código em blocos:
#
# 1. entrada e validação;
# 2. cadastro dos gastos;
# 3. cálculos gerais;
# 4. resumos por categoria;
# 5. relatório final.
#
# Nesta primeira versão, use apenas os conteúdos estudados nas aulas 1 a 9.
# O programa será reorganizado com funções depois da Aula 11.

# 1. Entrada e validação

while True:
    entrada_orc = input("Informe o orçamento do mês: ").strip().replace(',','.')

    if (entrada_orc.count('.') <= 1 and
        entrada_orc.replace('.','').isdigit() and entrada_orc != '' and 
        float(entrada_orc) > 0):
        break
    print("Entrada inválida. Digite um valor positivo.")

orcamento = float(entrada_orc)

print()

# 2. Cadastro dos gastos

gastos = []

while True:

    while True:
        descricao = input("Informe a descrição do gasto ('fim' para encerrar): ").strip().lower()

        if (descricao.replace(',','.').replace('.','').replace('-','').replace(';','').isdigit() or descricao == ''):
            print("Descrição inválida! Não insira somente números ou valores nulos")
            continue
        break

    if descricao == 'fim':
        break
    
    while True:
        categoria = input("Informe a categoria do gasto: ").strip().lower()

        if (categoria.replace(',','.').replace('.','').replace('-','').replace(';','').isdigit() or categoria == ''):
            print("Categoria inválida! Não insira somente números ou valores nulos")
            continue
        break

    while True:
        valor = input("Informe o valor: ").strip().replace(',','.')

        if not (valor.count('.') <= 1 and valor.replace('.','').isdigit() and valor != '' and float(valor) > 0):
            print("Valor inválido! Insira um valor positivo.")
            continue

        valor = float(valor)
        break

    gasto = {'descricao': descricao, 'categoria': categoria, 'valor': valor}
    gastos.append(gasto)
    print(f"Gasto registrado: {gasto['descricao']} | {gasto['categoria']} | R${(gasto['valor']):.2f} \n")
    
# 3. Cálculos gerais e Resumos por categoria

if len(gastos) > 0:

    total_gasto = 0
    maior_gasto = gastos[0]
    menor_gasto = gastos[0]
    categorias = set()

    for gasto in gastos:

        total_gasto += gasto['valor']

        if gasto['valor'] > maior_gasto['valor']:
            maior_gasto = gasto

        if gasto['valor'] < menor_gasto['valor']:
            menor_gasto = gasto

        categorias.add(gasto['categoria'])

    media = total_gasto / len(gastos)

    # Resumos por categoria

    gasto_categoria = {}
    qtd_categoria = {}

    for gasto in gastos:
        cat = gasto['categoria']
        val = gasto['valor']

        if cat in gasto_categoria:
            gasto_categoria[cat] += val
            qtd_categoria[cat] += 1
        else:
            gasto_categoria[cat] = val
            qtd_categoria[cat] = 1

    maior_cat_valor = 0

    for valor in gasto_categoria.values():
        maior_cat_valor = max(maior_cat_valor, valor)

    maiores_categorias = []
    for categoria, valor in gasto_categoria.items():
        if valor == maior_cat_valor:
            maiores_categorias.append(categoria)

    maior_cat_share_gasto = (maior_cat_valor / total_gasto)*100
    maior_cat_share_orc = (maior_cat_valor/ orcamento)*100

    gastos_acima_media = []

    for gasto in gastos:

        if gasto['valor'] > media:
            gastos_acima_media.append(gasto)


    saldo = orcamento - total_gasto

    print(f"""Relatório de gastos no mês:
    Orçamento: R${orcamento:.2f}
    Qtd. Gastos registrados: {len(gastos)}

    Total gasto: R${total_gasto:.2f}
    Valor médio: R${media:.2f}

    Maior gasto: {maior_gasto['descricao']} | {maior_gasto['categoria']} | R${(maior_gasto['valor']):.2f}
    Menor gasto: {menor_gasto['descricao']} | {menor_gasto['categoria']} | R${(menor_gasto['valor']):.2f}
    \n""")

    print("Gasto por categoria:")
    for categoria, valor in gasto_categoria.items():
        print(f"{categoria}: R${valor:.2f}")
    print()

    print("Quantidade por categoria: ")
    for categoria, valor in qtd_categoria.items():
        print(f"{categoria}: {valor}")
    print()

    print(f"{len(gastos_acima_media)} Gastos acima da média:")
    for gasto in gastos_acima_media:
        print(f"{gasto['descricao']} | {gasto['categoria']} | R${(gasto['valor']):.2f}")
    print()

    nomes_categorias = ", ".join(maiores_categorias)

    if len(maiores_categorias) > 1:
        print(f"""Categorias de maior representatividade (Empate entre {len(maiores_categorias)}): {nomes_categorias}
    Valor de cada uma: R${maior_cat_valor:.2f}
    {maior_cat_share_gasto:.1f}% sobre o gasto total (cada)
    {maior_cat_share_orc:.1f}% sobre o orçamento (cada)
    \n""")
    else:
        print(f"""Categoria de maior representatividade: {nomes_categorias}
    Valor: R${maior_cat_valor:.2f}
    {maior_cat_share_gasto:.1f}% sobre o gasto total
    {maior_cat_share_orc:.1f}% sobre o orçamento
    \n""")

    if saldo >= 0:
        print(f"Saldo restante: R${saldo:.2f}\n")
    else:
        print(f"Gastos excederam o orçamento em R${(saldo*-1):.2f}\n")
else:
    print("Nenhum gasto registrado.")