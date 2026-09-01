ano = int(input("Informe um ano: "))

if ((ano % 4) == 0) and ((ano % 100) != 0) or ((ano % 400) == 0):
    print("Ano é bissexto.\n")
else:
    print("Ano não é bissexto.\n")