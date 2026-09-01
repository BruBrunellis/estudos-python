# Aula 5 — Condicionais: if, elif e else
#
# Objetivo: executar blocos de código diferentes conforme uma condição.
# Pré-requisitos: operadores relacionais e lógicos, input() e conversão de tipos.

# if executa um bloco apenas quando a condição é True.
idade = 20

if idade >= 18:
    print("Você atingiu a maioridade.")

# A indentação (quatro espaços) indica quais linhas pertencem ao bloco.
# Python não usa chaves {} para delimitar blocos como algumas outras linguagens.

# else executa quando a condição do if é False.
saldo = 50
valor_compra = 80

if saldo >= valor_compra:
    print("Compra aprovada.")
else:
    print("Saldo insuficiente.")

# elif permite testar outra condição quando a anterior foi False.
nota = 7.5

if nota >= 9:
    conceito = "A"
elif nota >= 7:
    conceito = "B"
elif nota >= 5:
    conceito = "C"
else:
    conceito = "D"

print(f"Nota: {nota} | Conceito: {conceito}")

# A ordem das condições importa. Python executa somente o primeiro bloco
# verdadeiro em uma sequência if/elif/else.
temperatura = 31

if temperatura >= 30:
    print("Está quente.")
elif temperatura >= 20:
    print("A temperatura está agradável.")
else:
    print("Está frio.")

# Condições podem combinar operadores lógicos estudados na Aula 4.
idade = 17
tem_autorizacao = True

if idade >= 18 or tem_autorizacao:
    print("Entrada permitida.")
else:
    print("Entrada não permitida.")

# `in` facilita comparar uma opção com várias possibilidades.
regiao = "Sul"

if regiao in ["Sul", "Sudeste"]:
    print("Região atendida.")
else:
    print("Região ainda não atendida.")

# Validação simples: verifique primeiro dados que não fazem sentido.
quantidade = -2

if quantidade < 0:
    print("Quantidade inválida.")
elif quantidade == 0:
    print("Nenhum item informado.")
else:
    print(f"Quantidade válida: {quantidade}")

# Ponte para análise de dados:
# Em dados reais, condicionais ajudam a classificar registros e marcar valores
# que precisam de revisão. Mais adiante, faremos isso para tabelas inteiras.
valor_venda = 1200

if valor_venda >= 1000:
    faixa_venda = "alta"
elif valor_venda >= 500:
    faixa_venda = "média"
else:
    faixa_venda = "baixa"

print(f"Faixa da venda: {faixa_venda}")

# Erros comuns:
# - esquecer os dois-pontos (:) após if, elif ou else;
# - usar = em vez de == ao comparar valores;
# - usar indentação diferente dentro do mesmo bloco;
# - colocar uma condição mais ampla antes de uma mais específica;
# - comparar números recebidos por input() sem converter com int() ou float().
