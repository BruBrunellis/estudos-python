# Aula 11 — Funções: parâmetros e retorno
# Módulo 2 — Python aplicado a dados
#
# Objetivo: criar e chamar funções, receber dados por parâmetros e devolver
# resultados com return para reutilizar cálculos em diferentes situações.
# Pré-requisitos: variáveis, condicionais, laços, listas e dicionários.
#
# Como estudar: leia um bloco, preveja a saída e execute o arquivo.
# Depois, altere os argumentos das chamadas e observe o que muda.
# Reserve cerca de 20 minutos para os exemplos, 45 para a lista e 10 para revisar.

# -----------------------------------------------------------------------------
# 1. DEFINIR E CHAMAR UMA FUNÇÃO
# -----------------------------------------------------------------------------

# Você já usou funções prontas: print(), len(), sum() e input().
# Uma função reúne instruções sob um nome. Com def, criamos nossas próprias
# funções. O corpo usa indentação de quatro espaços e pode ter várias linhas.
# Definir a função NÃO executa seu corpo: precisamos chamá-la com parênteses.


def mostrar_abertura():
    print("Análise de vendas")
    print("Vamos transformar registros em informações.")


mostrar_abertura()
# Saída:
# Análise de vendas
# Vamos transformar registros em informações.

# Defina a função antes da linha que a chama ser executada.
# As linhas sem indentação abaixo da definição estão fora da função.

# -----------------------------------------------------------------------------
# 2. PARÂMETROS E ARGUMENTOS
# -----------------------------------------------------------------------------

# Parâmetro é o nome que recebe um dado na definição da função.
# Argumento é o valor fornecido na chamada.
# Aqui, nome é o parâmetro; "Ana" e "Bruno" são argumentos de duas chamadas.


def saudar_analista(nome):
    print(f"Olá, {nome}! Vamos analisar os dados.")


saudar_analista("Ana")
saudar_analista("Bruno")

# Cada chamada executa o mesmo corpo com os dados recebidos naquela vez.
# Uma função também pode receber vários parâmetros, separados por vírgulas.

# -----------------------------------------------------------------------------
# 3. RETURN: DEVOLVER UM RESULTADO
# -----------------------------------------------------------------------------


def calcular_receita(preco_unitario, quantidade):
    receita = preco_unitario * quantidade
    return receita


receita_cadernos = calcular_receita(25.0, 4)
receita_canetas = calcular_receita(5.0, 6)
print(f"Cadernos: R$ {receita_cadernos:.2f}")  # Cadernos: R$ 100.00
print(f"Receita conjunta: R$ {receita_cadernos + receita_canetas:.2f}")
# Receita conjunta: R$ 130.00

# Acompanhe a primeira chamada:
# 1. preco_unitario recebe 25.0 e quantidade recebe 4;
# 2. receita recebe 100.0;
# 3. return devolve 100.0 e encerra essa execução da função;
# 4. receita_cadernos recebe o resultado devolvido.
# A variável receita pertence à função. Use o retorno para obter seu valor
# fora dela. A próxima aula aprofundará esse assunto, chamado escopo.

# -----------------------------------------------------------------------------
# 4. PRINT E RETURN TÊM PAPÉIS DIFERENTES
# -----------------------------------------------------------------------------

# print mostra uma informação na tela.
# return entrega um valor ao código que chamou a função.
# Uma função que termina sem return explícito devolve None (ausência de valor).


def exibir_dobro(numero):
    print(numero * 2)


def calcular_dobro(numero):
    return numero * 2


resultado_exibido = exibir_dobro(7)  # Mostra 14 na tela.
print(resultado_exibido)  # None: exibir_dobro não devolveu o cálculo.

resultado_calculado = calcular_dobro(7)  # Devolve 14, sem imprimir.
print(resultado_calculado + 1)  # 15: podemos reutilizar o resultado.

# Prefira return em funções de cálculo. Faça a apresentação fora delas.
# Assim, o mesmo resultado poderá ser exibido, comparado ou salvo em arquivo.

# -----------------------------------------------------------------------------
# 5. ARGUMENTOS NOMEADOS E VALORES PADRÃO
# -----------------------------------------------------------------------------

# Chamadas posicionais associam argumentos aos parâmetros pela ordem.
# Chamadas nomeadas usam o nome do parâmetro, deixando a intenção explícita.
print(calcular_receita(12.0, 3))  # 36.0
print(calcular_receita(quantidade=3, preco_unitario=12.0))  # 36.0

# Um valor padrão é usado quando o argumento correspondente é omitido.
# Na sintaxe usada aqui, parâmetros obrigatórios vêm antes dos opcionais.


def calcular_preco_final(preco, desconto_percentual=0):
    return preco * (1 - desconto_percentual / 100)


print(calcular_preco_final(200))  # 200.0: desconto padrão de 0%.
print(calcular_preco_final(200, 10))  # 180.0: desconto de 10%.
print(calcular_preco_final(200, desconto_percentual=25))  # 150.0

# Neste exemplo, supomos preço não negativo e desconto entre 0 e 100.
# Validação e tratamento de entradas inválidas serão foco da Aula 12.

# -----------------------------------------------------------------------------
# 6. CONDICIONAIS E RETORNO ANTECIPADO
# -----------------------------------------------------------------------------

# return encerra a chamada imediatamente, mesmo dentro de um if ou de um laço.
# Por isso, instruções posteriores ao return não executam nessa chamada.


def calcular_media(valores):
    if len(valores) == 0:
        return None

    return sum(valores) / len(valores)


print(calcular_media([10, 20, 30]))  # 20.0
print(calcular_media([0, 0]))  # 0.0: existem dados e a média é zero.
print(calcular_media([]))  # None: não há dados para calcular a média.

# is None é a forma recomendada de verificar esse marcador.
media = calcular_media([])
if media is None:
    print("Sem dados para calcular a média.")
else:
    print(f"Média: {media:.2f}")

# Não use apenas "if media": uma média válida igual a zero também seria falsa.
# Neste contrato, a lista contém somente números. None dentro da lista não é
# tratado aqui; lidar com dados ausentes será aprofundado nas próximas aulas.

# -----------------------------------------------------------------------------
# 7. LISTAS, LAÇOS E DICIONÁRIOS EM FUNÇÕES
# -----------------------------------------------------------------------------

# Os parâmetros também podem receber coleções. A cada chamada, criamos uma
# lista nova para o resultado, preservando os dados da lista recebida.


def selecionar_acima(valores, limite):
    selecionados = []
    for valor in valores:
        if valor > limite:
            selecionados.append(valor)
    return selecionados


print(selecionar_acima([10, 30, 20, 40], 20))  # [30, 40]
print(selecionar_acima([], 20))  # []

# O return fica DEPOIS do for: precisamos percorrer todos os valores.
# Retornar de dentro do laço encerraria a função antes de concluir a seleção.

# Uma função pode chamar outra e devolver um dicionário com vários resultados.
# O dicionário continua sendo um único objeto retornado.


def resumir_valores(valores):
    return {
        "quantidade": len(valores),
        "total": sum(valores),
        "media": calcular_media(valores),
    }


resumo = resumir_valores([10, 20, 30])
print(resumo)  # {'quantidade': 3, 'total': 60, 'media': 20.0}
print(resumir_valores([]))  # {'quantidade': 0, 'total': 0, 'media': None}

# -----------------------------------------------------------------------------
# 8. PONTE PARA ANÁLISE DE DADOS
# -----------------------------------------------------------------------------

# Pergunta: qual foi a receita média por registro de venda?
# Fonte: registros fictícios abaixo, já preenchidos e com tipos corretos.
# Limpeza: não é necessária neste exemplo; assumimos dados válidos.
vendas = [
    {"produto": "Caderno", "preco": 25.0, "quantidade": 4},
    {"produto": "Caneta", "preco": 5.0, "quantidade": 6},
    {"produto": "Pasta", "preco": 10.0, "quantidade": 2},
]

# Reutilizamos uma função de cálculo para cada registro e outra para o resumo.
receitas = []
for venda in vendas:
    receitas.append(calcular_receita(venda["preco"], venda["quantidade"]))

resumo_vendas = resumir_valores(receitas)
print(f"Receita total: R$ {resumo_vendas['total']:.2f}")  # R$ 150.00
print(f"Receita média por registro: R$ {resumo_vendas['media']:.2f}")  # R$ 50.00

# Conclusão: nesses três registros, a receita média foi de R$ 50.00.
# Limitação: essa média é por registro, não por unidade nem por cliente.
# Apresentação: o resumo textual basta para esta pergunta; gráficos virão depois.
# No controle de gastos da Aula 10, o mesmo princípio permite separar cálculos
# do input e do relatório. Na lista, você praticará essa divisão.

# -----------------------------------------------------------------------------
# 9. ERROS COMUNS E BOAS PRÁTICAS
# -----------------------------------------------------------------------------

# Erros que impedem a execução:
# - esquecer os dois-pontos depois de def ou indentar incorretamente o corpo;
# - chamar uma função antes de executar sua definição;
# - omitir um argumento obrigatório ou escrever errado o nome de um parâmetro;
# - tentar somar ou formatar None como se fosse um número.
#
# Erros de lógica:
# - escrever mostrar_abertura sem () e esperar que ela execute;
# - usar print quando o cálculo precisa ser devolvido com return;
# - colocar return dentro do for quando precisa processar a coleção inteira.
#
# Boas práticas:
# - use nomes que descrevam a ação, como calcular_media;
# - mantenha cada função com uma responsabilidade clara;
# - receba os dados necessários por parâmetros;
# - documente as entradas esperadas e o comportamento para coleções vazias;
# - evite alterar listas recebidas quando a intenção for apenas analisá-las;
# - separe as definições com duas linhas em branco, seguindo a PEP 8.
#
# Revisão: explique com suas palavras a diferença entre definir e chamar,
# parâmetro e argumento, print e return. Depois, resolva a lista da Aula 11.
