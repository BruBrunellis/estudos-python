# Aula 4 — Operadores relacionais e lógicos
#
# Objetivo: comparar valores e combinar condições para produzir True ou False.
# Pré-requisitos: variáveis, strings, números, operadores aritméticos e input().

# Comparações produzem valores booleanos: True (verdadeiro) ou False (falso).
idade = 20
print(idade == 20)  # True: igual a
print(idade != 18)  # True: diferente de
print(idade > 18)   # True: maior que
print(idade < 18)   # False: menor que
print(idade >= 20)  # True: maior ou igual a
print(idade <= 19)  # False: menor ou igual a

# Atenção: = atribui um valor; == compara dois valores.
nome = "Bruno"
print(nome == "Bruno")

# Comparações podem ser feitas entre strings. Python compara letras respeitando
# maiúsculas/minúsculas, por isso uma padronização pode ser importante.
estado = "SP"
print(estado == "sp")          # False
print(estado.lower() == "sp")  # True

# Operadores lógicos unem ou invertem condições.
# and: True apenas se TODAS as condições forem verdadeiras.
tem_idade_minima = idade >= 18
tem_documento = True
pode_entrar = tem_idade_minima and tem_documento
print(f"Pode entrar: {pode_entrar}")

# or: True se pelo menos UMA das condições for verdadeira.
tem_cupom = False
eh_cliente_vip = True
recebe_desconto = tem_cupom or eh_cliente_vip
print(f"Recebe desconto: {recebe_desconto}")

# not inverte um valor booleano.
produto_em_estoque = False
produto_indisponivel = not produto_em_estoque
print(f"Produto indisponível: {produto_indisponivel}")

# Tabela-resumo:
# A      B      A and B    A or B
# True   True   True       True
# True   False  False      True
# False  True   False      True
# False  False  False      False

# Parênteses deixam expressões longas mais fáceis de ler e evitam dúvidas.
nota = 8.5
frequencia = 80
esta_aprovado = (nota >= 7) and (frequencia >= 75)
print(f"Aprovado: {esta_aprovado}")

# Uma comparação encadeada é útil para verificar intervalos.
temperatura = 23
temperatura_agradavel = 18 <= temperatura <= 28
print(f"Temperatura agradável: {temperatura_agradavel}")

# `in` verifica se um elemento ou texto está contido em outro.
categorias_permitidas = ["alimentação", "transporte", "saúde"]
categoria = "saúde"
print(categoria in categorias_permitidas)
print("@" in "aluna@email.com")  # noqa: PLR0133

# Ponte para análise de dados:
# Comparações geram filtros. Por exemplo, identificar vendas com valor alto e
# pedidos de uma região específica antes de analisar esses registros.
valor_venda = 350.0
regiao = "Sudeste"
venda_relevante = (valor_venda >= 300) and (regiao == "Sudeste")
print(f"Venda relevante para o recorte: {venda_relevante}")

# Erros comuns:
# - usar = no lugar de == em uma comparação;
# - comparar input() diretamente com um número: input() sempre retorna str;
#   converta com int() ou float() antes;
# - escrever "True" entre aspas: isso é texto, não um booleano;
# - esquecer parênteses em condições grandes, dificultando a leitura.
