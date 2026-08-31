# Aula 4 — Lista de exercícios: operadores relacionais e lógicos
# Resolva os exercícios imprimindo o resultado de cada comparação ou expressão.
# Nesta aula, ainda não use if/elif/else: eles serão estudados na próxima aula.

# 1. Crie duas variáveis numéricas, numero_1 e numero_2. Exiba o resultado de:
#    a) numero_1 é maior que numero_2;
#    b) numero_1 é igual a numero_2;
#    c) numero_1 é diferente de numero_2.

numero_1 = 10
numero_2 = 13

print(numero_1 > numero_2)
print(numero_1 == numero_2)
print(f"{numero_1 != numero_2}\n")

# 2. Crie uma variável idade e verifique se a pessoa tem 18 anos ou mais.

idade = 16

maioridade = idade >= 18

print(f"Pessoa atingiu maioridade: {maioridade}\n")

# 3. Peça duas notas ao usuário e crie uma variável chamada media. Exiba se a
# média é maior ou igual a 7.

nota_1 = float(input("Informe a 1ª Nota (0 a 10): "))
nota_2 = float(input("Informe a 2ª Nota (0 a 10): "))

media = (nota_1 + nota_2) / 2

aprovado = media >= 7

print(f"O aluno foi aprovado: {aprovado}\n")

# 4. Peça uma temperatura em graus Celsius e exiba se ela está no intervalo de
# 18 a 28 graus, inclusive. Use uma comparação encadeada.

celsius = float(input("Informe a temperatura em celsius: "))

agradavel = 18 <= celsius <= 28

print(f"A temperatura está agradável: {agradavel}\n")

# 5. Crie as variáveis tem_ingresso e tem_documento, com valores True ou False.
# Crie uma terceira variável que seja True somente quando a pessoa tiver ambos.

tem_ingresso = True
tem_documento = False

pode_entrar = tem_ingresso and tem_documento

print(f"A pessoa pode entrar no evento: {pode_entrar}\n")

# 6. Uma loja dá desconto a quem possui cupom OU é cliente VIP. Crie as
# variáveis tem_cupom e cliente_vip e calcule uma variável recebe_desconto.

tem_cupom = True
cliente_vip = False

recebe_desconto = tem_cupom or cliente_vip

print(f"Cliente receberá desconto: {recebe_desconto}\n")

# 7. Crie a variável produto_em_estoque. Use not para gerar e imprimir a
# variável produto_indisponivel.

produto_em_estoque = True
produto_indisponivel = not produto_em_estoque

print(f"O produto está indisponível: {produto_indisponivel}\n")

# 8. Peça uma sigla de estado ao usuário. Compare-a com "SP" sem diferenciar
# letras maiúsculas e minúsculas.

sigla = input("Digite uma sigla de estado (ex: BA): ")

print(sigla.upper() == 'SP')
print(f"{sigla.lower() == 'sp'}\n")

# 9. Crie uma lista com as categorias "alimentação", "transporte" e "saúde".
# Peça uma categoria ao usuário e exiba se ela pertence à lista.

categorias = ['alimentação', 'transporte', 'saúde']

prompt = input("Informe uma categoria (ex. compras): ").strip().lower()

check = prompt in categorias

print(f"A categoria está na lista: {check}\n")

# 10. Peça um e-mail e crie uma variável que seja True apenas quando ele tiver
# "@" E terminar com ".com". Remova espaços nas pontas antes de verificar.

email = input("Informe seu endereço de e-mail: ").strip()

check = '@' in email and email.endswith('.com')

print(f"O endereço de e-mail é válido: {check}\n")

# 11. Uma pessoa será considerada apta a um curso se tiver pelo menos 16 anos
# E possuir ensino médio concluído. Peça a idade e crie uma variável booleana
# chamada ensino_medio_concluido para montar essa expressão lógica.

idade = int(input("Informe sua idade: "))

ensino_medio_completo = True
apto = (idade >= 16) and ensino_medio_completo

print(f"O aluno está apto para o curso: {apto}\n")

# 12. Desafio — Filtro de vendas:
# Crie as variáveis valor_venda, regiao e pagamento_confirmado. Uma venda é
# relevante quando vale pelo menos R$ 500, ocorreu na região "Sudeste" OU
# "Sul", e tem pagamento confirmado. Monte e imprima essa expressão usando
# parênteses para deixá-la clara.

valor_venda = 150.00
regiao = 'Sul'
pagamento_confirmado = True

relevante = (valor_venda >= 500) and (regiao in ('Sudeste', 'Sul')) and pagamento_confirmado

print(f"""A venda é relevante: {relevante}
Valor da venda: R${valor_venda:.2f},
Região: {regiao},
Pagamento confirmado: {pagamento_confirmado}
\n""")