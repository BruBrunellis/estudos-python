# Exibe uma mensagem inicial. \n cria uma linha em branco após o texto.
print("Hello, World!\n")

# Armazena a soma de dois números na variável resultado e a exibe na tela.
resultado = 5 + 3
print("Resultado da soma:", resultado, "\n")

# Solicita o nome do usuário e monta uma mensagem de boas-vindas.
nome = input("Digite seu nome: ")
print("Olá, " + nome + "! Seja bem-vindo(a)!\n")

# input() retorna texto; int() converte as respostas para números inteiros
# antes de somá-las.
# f strings permitem a interpolação de variáveis dentro de strings.
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1 + n2
print(f"Resultado da soma de {n1} e {n2}: {soma}\n")

# Lê um texto e usa métodos de string para identificar suas características.
# Para que print() seja codado em múltiplas linhas, é preciso repetir as aspas e vírgulas.
texto = input("Digite algo:")
print(
    f"Você digitou: {texto},\n Tipo primitivo: {type(texto)},\n",
    f"Alfabético: {texto.isalpha()},\n Numérico: {texto.isnumeric()},\n",
    f"Alfanumérico: {texto.isalnum()},\n",
    f"Maiúsculo: {texto.isupper()},\n Minúsculo: {texto.islower()},\n",
    f"Capitalizado: {texto.istitle()}\n"
)
