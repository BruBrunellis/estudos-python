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