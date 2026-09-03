while True:
    entrada = input("Informe a quantidade de vendas a registrar: ")

    if not entrada.isdigit() or entrada == 0:
        print("Valor inválido! Informe pelo menos 1 venda a registrar.")
        continue
    break

contagem = int(entrada)
total = 0
cont_vendas = 0
cont_altas = 0

for i in range(1, contagem + 1):
    while True:
        venda = input(f"Insira o valor da {i}ª venda: ").replace(',','.')

        if venda.count('.') <= 1 and venda.replace('.','').isdigit() and venda != '' and float(venda) > 0:
            valor = float(venda)
            total += valor
            cont_vendas += 1
            if valor >= 1000:
                cont_altas += 1
            break
        else:
            print("Valor inválido! Tente novamente.")

media = total / cont_vendas

print(f"""Foram registradas {cont_vendas} vendas:
Valor total: R${total:.2f}
Vendas acima de $1000.00: {cont_altas}
Média: R${media:.2f}
\n""")