# Aula 10 — Revisão do Módulo 1
#
# Objetivo: integrar os fundamentos estudados nas aulas 1 a 9 para preparar a
# construção do primeiro mini-projeto.
# Pré-requisitos: variáveis, operadores, strings, condicionais, laços, listas,
# tuplas, conjuntos e dicionários.

# Nesta revisão, o foco não é conhecer uma nova sintaxe. O objetivo é combinar
# recursos já estudados para transformar dados de entrada em um resumo útil.

# -----------------------------------------------------------------------------
# 1. DECOMPONDO UM PROBLEMA
# -----------------------------------------------------------------------------

# Antes de programar, divida o problema em etapas:
# 1. entender quais dados entram;
# 2. validar e padronizar esses dados;
# 3. armazená-los em uma estrutura adequada;
# 4. processar cálculos e classificações;
# 5. apresentar um resultado compreensível.

# Exemplo de entrada já padronizada:
nome_produto = "  Monitor  ".strip().title()
preco_unitario = 1200.00
quantidade = 3
valor_total = preco_unitario * quantidade

print(f"Produto: {nome_produto}")
print(f"Valor total: R$ {valor_total:.2f}\n")

# -----------------------------------------------------------------------------
# 2. ESCOLHENDO A ESTRUTURA
# -----------------------------------------------------------------------------

# Uma tupla serve para valores fixos, como opções permitidas.
regioes_validas = ("norte", "sul", "leste", "oeste")

# Um conjunto reúne valores únicos.
clientes_unicos = set()

# Um dicionário representa um registro com campos identificados.
venda_exemplo = {
    "cliente": "Ana",
    "regiao": "sul",
    "valor": 850.00,
}

# Uma lista de dicionários representa vários registros, como linhas de tabela.
vendas = [
    {"cliente": "Ana", "regiao": "sul", "valor": 850.00},
    {"cliente": "Bruno", "regiao": "norte", "valor": 1250.00},
    {"cliente": "Ana", "regiao": "sul", "valor": 430.00},
    {"cliente": "Carla", "regiao": "leste", "valor": 1700.00},
]

print(f"Regiões válidas: {regioes_validas}")
print(f"Exemplo de registro: {venda_exemplo}")
print(f"Quantidade de vendas: {len(vendas)}\n")

# -----------------------------------------------------------------------------
# 3. PERCORRENDO E RESUMINDO DADOS
# -----------------------------------------------------------------------------

total_vendas = 0.0
maior_venda = vendas[0]
total_por_regiao = {}

for venda in vendas:
    total_vendas += venda["valor"]
    clientes_unicos.add(venda["cliente"])

    if venda["valor"] > maior_venda["valor"]:
        maior_venda = venda

    regiao = venda["regiao"]

    if regiao in total_por_regiao:
        total_por_regiao[regiao] += venda["valor"]
    else:
        total_por_regiao[regiao] = venda["valor"]

media_vendas = total_vendas / len(vendas)

print(f"Total das vendas: R$ {total_vendas:.2f}")
print(f"Média das vendas: R$ {media_vendas:.2f}")
print(f"Maior venda: {maior_venda['cliente']} — R$ {maior_venda['valor']:.2f}")
print(f"Clientes únicos: {len(clientes_unicos)}")
print(f"Total por região: {total_por_regiao}\n")

# -----------------------------------------------------------------------------
# 4. FILTRANDO E CLASSIFICANDO
# -----------------------------------------------------------------------------

vendas_acima_da_media = []

for venda in vendas:
    if venda["valor"] > media_vendas:
        vendas_acima_da_media.append(venda)

print("Vendas acima da média:")

for venda in vendas_acima_da_media:
    print(f"- {venda['cliente']}: R$ {venda['valor']:.2f}")

print()

# Condicionais também ajudam a interpretar o resultado.
meta = 4000.00

if total_vendas >= meta:
    print("A meta de vendas foi atingida.")
else:
    valor_faltante = meta - total_vendas
    print(f"Faltaram R$ {valor_faltante:.2f} para atingir a meta.")

# -----------------------------------------------------------------------------
# 5. TESTES DE MESA
# -----------------------------------------------------------------------------

# Antes de considerar um programa pronto, simule situações como:
# - valor igual a zero ou negativo;
# - texto vazio ou apenas com espaços;
# - letras maiúsculas e minúsculas no mesmo dado;
# - quantidade mínima permitida;
# - valor exatamente igual a um limite;
# - registros repetidos;
# - apenas um registro, para verificar média, maior e menor valor.

# Ponte para análise de dados:
# O fluxo usado aqui — coletar, limpar, armazenar, resumir e comunicar — é uma
# versão pequena do trabalho realizado por um analista. Nas próximas aulas,
# funções, arquivos, NumPy e pandas tornarão esse processo mais reutilizável e
# adequado a conjuntos de dados maiores.

# Erros comuns:
# - começar a codificar sem dividir o problema em etapas;
# - misturar coleta de dados, cálculos e impressão sem organização visual;
# - comparar textos sem antes padronizar espaços e letras;
# - dividir pela quantidade errada de registros;
# - usar uma lista quando o resultado solicitado é um dicionário;
# - calcular maior, menor ou média sem garantir que existam dados;
# - usar in quando a intenção é testar igualdade com ==.

# Boas práticas:
# - escolha nomes que revelem o significado dos dados;
# - mantenha cada bloco responsável por uma etapa do programa;
# - use constantes claras para limites e opções permitidas;
# - teste cada etapa antes de montar o programa completo;
# - confira se o tipo da estrutura final corresponde ao requisito.
