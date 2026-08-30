print("Hello, World!\n")

resultado = 5 + 3
print("Resultado da soma:", resultado, "\n")

nome = input("Digite seu nome: ")
print("Olá, " + nome + "! Seja bem-vindo(a)!\n")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1 + n2
print(f"Resultado da soma de {n1} e {n2}: {soma}\n")

texto = input("Digite algo:")
print(
    f"Você digitou: {texto},\n Tipo primitivo: {type(texto)},\n",
    f"Alfabético: {texto.isalpha()},\n",
    f"Numérico: {texto.isnumeric()},\n",
    f"Alfanumérico: {texto.isalnum()},\n",
    f"Maiúsculo: {texto.isupper()},\n",
    f"Minúsculo: {texto.islower()},\n",
    f"Capitalizado: {texto.istitle()}\n"
)