# Aula 11 — Lista de exercícios: funções
#
# Resolva usando os conteúdos estudados até aqui, sem bibliotecas externas.
# Escreva as funções e suas chamadas abaixo de cada enunciado.
# Nos exercícios de cálculo, use return e imprima o resultado fora da função.
# Use dados definidos no código: input não é necessário nesta lista.
# Salvo indicação contrária, considere entradas com os tipos corretos.
# Confira os casos sugeridos e tente prever os resultados antes de executar.

# 1. PRIMEIRA FUNÇÃO
# Crie mostrar_menu(), sem parâmetros, que imprima três opções:
# "1 - Registrar", "2 - Resumir" e "3 - Sair".
# Chame a função duas vezes. Explique em um comentário por que apenas definir
# a função não mostra o menu na tela.

def mostrar_menu():
    print("""1 - Registrar
2 - Resumir
3 - Sair
    \n""")

mostrar_menu()
mostrar_menu()

'A definição da função estabele cálculos, prints e loops a serem feitos. Simplesmente definir e rodar o script não gera saída,'
'pois a função deve ser executada, ou "chamada".'

# 2. UM PARÂMETRO
# Crie apresentar_produto(nome), que imprima "Produto selecionado: <nome>".
# Chame a mesma função para dois produtos diferentes.
# Em um comentário, identifique o parâmetro e um argumento das suas chamadas.

def apresentar_produto(nome):
    print(f"Produto selecionado: {nome}")

apresentar_produto('Notebook')
apresentar_produto('Tablet')
print()

# O parâmetro da função é um molde que assume o valor inserido na chamada entre (), chamado argumento, como no 1º caso: "Notebook"

# 3. DEVOLVENDO UM CÁLCULO
# Crie calcular_saldo(orcamento, total_gasto), que retorne o saldo disponível.
# Guarde o retorno em uma variável e imprima-o com duas casas decimais.
# Teste: (1000, 750) -> 250; (1000, 1000) -> 0; (1000, 1200) -> -200.
# Saldo negativo indica que os gastos ultrapassaram o orçamento.

def calcular_saldo(orcamento, total_gasto):
    saldo = orcamento - total_gasto
    return saldo

saldo = calcular_saldo(1000, 750)
print(f"Saldo: R${saldo:.2f}")

saldo = calcular_saldo(1000, 1000)
print(f"Saldo: R${saldo:.2f}")

saldo = calcular_saldo(1000, 1200)
print(f"Saldo: R${saldo:.2f}")
print()

# 4. PRINT OU RETURN?
# Analise este trecho, sem copiá-lo como sua resposta:
# def calcular_triplo(numero):
#     print(numero * 3)
# resultado = calcular_triplo(4)
# Explique em comentários o que aparece na tela e o que fica em resultado.
# Depois, escreva uma versão que devolva o triplo. Guarde o retorno de uma
# chamada com 4, some 2 fora da função e imprima o resultado final (14).

def calcular_triplo(numero):
    return (numero * 3)

resultado = calcular_triplo(4) + 2

print(f"{resultado}\n")

# Dessa forma a função somente imprime 4*3 = 12, a variável "resultado" assume None por padrão.
# Se eu tentar somar 2 fora da função, resulta em erro. Para funcionar, é preciso utilizar "return",
# return (numero * 3). Assim, resultado = calcular_triplo(4) + 2 atribui 14 à variável.
# Ou print(f"{calcular_triplo(4)+2}") exibe 14 diretamente no terminal

# 5. PARÂMETRO OPCIONAL E CHAMADA NOMEADA
# Crie calcular_entrega(valor_compra, frete=15), que retorne o total a pagar.
# Considere valores não negativos.
# Faça uma chamada omitindo o frete e outra informando frete=0.
# Faça também uma chamada com os dois argumentos nomeados em ordem invertida.
# Teste: compra de 80 com frete padrão -> 95; com frete zero -> 80.

def calcular_entrega(valor_compra, frete=15):
    if valor_compra < 0 or frete < 0:
        print("Valor inválido! Não insira valores negativos no argumento da função.")
    else:
        return (valor_compra + frete)

print(calcular_entrega(80)) #função assume frete padrão 15
print(calcular_entrega(80, 0)) #função assume frete 0
# print(calcular_entrega()) dá erro pois python gera TypeError antes de executar ao omitir argumento obrigatório.
print(calcular_entrega(frete=15, valor_compra=80)) #função como esperado pois mesmo com posições invertidas, os parâmetros foram referenciados nos argumentos.
print(calcular_entrega(80, frete=0)) #função assume frete 0
print(calcular_entrega(0)) # retorna 15
print()

# 6. CONDICIONAIS E RETORNO
# Crie classificar_saldo(saldo), que retorne:
# - "disponível" quando saldo for positivo;
# - "esgotado" quando saldo for zero;
# - "excedido" quando saldo for negativo.
# Teste os três casos. Depois, use calcular_saldo, do exercício 3, e passe seu
# resultado para classificar_saldo. Imprima o saldo e a classificação.

def classificar_saldo(saldo=0):
    if saldo > 0:
        return 'disponível'
    elif saldo == 0:
        return 'esgotado'
    else:
        return 'excedido'

print(classificar_saldo(1000))
print(classificar_saldo())
print(classificar_saldo(-250))

saldo = calcular_saldo(1000, 300)
status = classificar_saldo(saldo)

print(f"Resultado do exercício: R${saldo:.2f} | Saldo {status}\n")

# 7. PERCORRENDO UMA LISTA
# Crie contar_positivos(valores), que retorne a quantidade de números maiores
# que zero. Use um laço e um contador dentro da função.
# Teste: [-2, 0, 5, 8] -> 2; [] -> 0; [-3, -1] -> 0; [5] -> 1.
# Verifique se sua função percorre todos os itens antes de retornar.

def contar_positivos(valores):
    positivos = 0
    for valor in valores:
        if valor > 0:
            positivos += 1
    return positivos

valores = [0, -3, 4, 8, 22, -12]
positivos = contar_positivos(valores)

print(f"Número de valores positivos: {positivos}\n")

# 8. COLEÇÃO VAZIA
# Crie obter_maior(valores), que retorne o maior número de uma lista.
# Se a lista estiver vazia, retorne None.
# Você pode usar max após verificar se há elementos.
# Fora da função, mostre "Sem valores" se o retorno for None.
# Teste: [4, 9, 2] -> 9; [-8, -3] -> -3; [0] -> 0; [] -> None.

def obter_maior(valores):
    if len(valores) > 0:
        maior = max(valores)
        return maior
    return None

testes = [[4, 9, 2], [-8, -3], [0], []]

for index, teste in enumerate(testes):
    maior = obter_maior(teste)
    if maior is not None:
        print(f"{index+1}º teste: {maior}")
    else:
        print(f"{index+1}º teste: Sem valores.")

print()

# 9. RETORNANDO UMA NOVA LISTA
# Crie padronizar_categorias(categorias), que receba uma lista de strings.
# Retorne uma nova lista com os textos sem espaços nas extremidades e em
# minúsculas. Ignore textos que ficarem vazios e mantenha as repetições.
# Preserve a ordem dos itens restantes e não altere a lista original.
# Teste: [" Mercado ", "", "   ", "LAZER", "mercado"]
# Resultado esperado: ["mercado", "lazer", "mercado"].
# Teste também uma lista vazia. Imprima a original após a chamada para conferir.

def padronizar_categorias(categorias):
    padrao = []
    if len(categorias) > 0:
        for categoria in categorias:
            texto = categoria.strip().lower()
            if texto != '':
                padrao.append(texto)
    return padrao

testes = [[' Mercado ', '', '   ', 'LAZER', 'mercado'], ['CAsa', ' apartamentO', 'fazenda  ',''], ['animal','PLANTA', '   ','funGO'],[]]

for index, teste in enumerate(testes):
    padrao = padronizar_categorias(teste)
    print(f"""{index+1}º teste:
Lista original: {teste}
Padronizada: {padrao}
""")

print()

# 10. DESAFIO — FUNÇÕES PARA O CONTROLE DE GASTOS
# Nesta lista, crie funções que poderiam ser usadas no projeto da Aula 10.
# Use os dados fictícios abaixo (copie-os para código executável):
# gastos = [
#     {"descricao": "Mercado", "categoria": "alimentação", "valor": 120.0},
#     {"descricao": "Ônibus", "categoria": "transporte", "valor": 30.0},
#     {"descricao": "Almoço", "categoria": "alimentação", "valor": 50.0},
# ]
# Considere todos os registros completos, com valores numéricos positivos.
#
# a) Crie totalizar_gastos(gastos), que retorne a soma dos valores.
#    Para uma lista vazia, retorne 0.
# b) Crie totalizar_categoria(gastos, categoria), que retorne o total apenas
#    da categoria informada. Use textos já padronizados e comparação exata.
#    Para uma categoria ausente ou lista vazia, retorne 0.
# c) Crie resumir_orcamento(gastos, orcamento), que retorne um dicionário com
#    as chaves "quantidade", "total", "saldo" e "situacao".
#    Reutilize totalizar_gastos, calcular_saldo e classificar_saldo.
# d) Fora das funções, imprima o resumo e o total de alimentação.
#    As funções devem receber os dados por parâmetros e preservar a lista.
#
# Casos para conferir:
# - dados acima: total 200, alimentação 170, transporte 30 e lazer 0;
# - orçamento 300: quantidade 3, total 200, saldo 100, situação "disponível";
# - orçamento 200: saldo 0 e situação "esgotado";
# - orçamento 150: saldo -50 e situação "excedido";
# - lista vazia e orçamento 300: quantidade 0, total 0, saldo 300;
# - apenas o gasto de ônibus e orçamento 100: total 30 e saldo 70.

gastos = [
{"descricao": "Mercado", "categoria": "alimentação", "valor": 120.0},
{"descricao": "Ônibus", "categoria": "transporte", "valor": 30.0},
{"descricao": "Almoço", "categoria": "alimentação", "valor": 50.0},
]

def totalizar_gastos(gastos):
    total_gasto = 0
    for gasto in gastos:
        total_gasto += gasto['valor']
    return total_gasto

def totalizar_categoria(gastos, categoria):
    total_cat = 0
    if len(gastos) > 0:
        for gasto in gastos:
            if categoria == gasto['categoria']:
                total_cat += gasto['valor']
        return total_cat
    return total_cat

def resumir_orcamento(gastos, orcamento):
    resumo_orc = {}
    qtd_gastos = len(gastos)
    total_gasto = totalizar_gastos(gastos)
    saldo = calcular_saldo(orcamento, total_gasto)
    situacao = classificar_saldo(saldo)
    resumo_orc.update(quantidade = qtd_gastos, total = total_gasto, saldo = saldo, situacao = situacao)
    return resumo_orc

testes = [{'orcamento': 300,
           'gastos': gastos,
           'categorias': ['alimentação', 'transporte', 'lazer']},
           {'orcamento': 200,
           'gastos': gastos,
           'categorias': ['alimentação', 'transporte', 'lazer']},
           {'orcamento': 150,
           'gastos': gastos,
           'categorias': ['alimentação', 'transporte', 'lazer']},
           {'orcamento': 300,
           'gastos': [],
           'categorias': ['alimentação', 'transporte', 'lazer']},
           {'orcamento': 100,
           'gastos': [{"descricao": "Ônibus", "categoria": "transporte", "valor": 30.0}],
           'categorias': ['transporte']}
           ]

for index, teste in enumerate(testes):
    resumo_orc = resumir_orcamento(teste['gastos'], teste['orcamento'])

    print(f"""{index+1}º Relatório de gastos:
Orçamento: R${teste['orcamento']:.2f}, Total: R${resumo_orc['total']:.2f}, {resumo_orc['quantidade']} gastos
Saldo: R${resumo_orc['saldo']:.2f}, saldo {resumo_orc['situacao']}
Gasto por categoria:""")
    
    resumo_cat = {}
    for categoria in teste['categorias']:
        resumo_cat[categoria] = totalizar_categoria(teste['gastos'],categoria)
    for chave, valor in resumo_cat.items():
        print(f"{chave}: R${valor:.2f}")
    print()

# AUTOAVALIAÇÃO
# - Consigo explicar a diferença entre print e return?
# - Consigo chamar a mesma função com dados diferentes?
# - Testei listas vazias, zero e valores negativos quando faziam sentido?
# - Minhas funções usam os parâmetros em vez de depender dos dados externos?
# - Consigo explicar como as funções do desafio trabalham juntas?