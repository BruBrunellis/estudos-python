# Aula 12 — Lista de exercícios: escopo, erros e validação
#
# Escreva as respostas abaixo de cada enunciado. Não há soluções neste arquivo.
# Use os conteúdos estudados até aqui, sem bibliotecas externas e sem global.
# Nos exercícios 1 a 8, use chamadas com dados definidos no código.
# Nos exercícios 9 e 10, haverá interação por input.
# Capture exceções específicas e mantenha suas explicações em comentários.
# Para os exercícios com texto, considere que o argumento recebido é string.

# 1. ESCOPO LOCAL E GLOBAL
# Antes de executar, preveja as duas saídas do trecho abaixo em comentários.
# Depois, copie o trecho para código executável e confira a previsão:
# categoria = "geral"
# def definir_categoria():
#     categoria = "alimentação"
#     return categoria
# print(definir_categoria())
# print(categoria)
# Explique por que a atribuição dentro da função não modifica o nome externo.

# Saída:
# alimentação
# geral
# Isso acontece pois categoria fora da função é global, enquanto a variável de mesmo nome dentro da função é local
# Há uma diferença de escopo.

categoria = "geral"
def definir_categoria():
     categoria = "alimentação"
     return categoria
print(definir_categoria())
print(categoria)
print()

# 2. DADOS ENTRAM POR PARÂMETROS
# Crie atualizar_saldo(saldo_atual, valor_gasto), que devolva o novo saldo.
# Considere argumentos numéricos válidos; o saldo resultante pode ser negativo.
# Fora da função, comece com saldo = 200. Faça duas chamadas sucessivas,
# descontando 50 e depois 30, sempre guardando o retorno na variável externa.
# Mostre os saldos 150 e 120. A função não deve ler a variável global saldo.
# Explique o que aconteceria se você chamasse a função sem guardar o retorno.

def atualizar_saldo(saldo_atual, valor_gasto):
    try:
        novo_saldo = saldo_atual - valor_gasto
    except ValueError:
        return
    if float(valor_gasto) < 0:
        print("Valor gasto inválido! Não pode ser negativo.")
        return
    return novo_saldo

try:
    saldo = atualizar_saldo(200, 50)
    print(f"Saldo: R${saldo:.2f}")
    saldo = atualizar_saldo(saldo, 30)
    print(f"Saldo: R${saldo:.2f}")
except TypeError:
    print("Valor inválido na função interrompeu o cálculo. Revise os argumentos.")

# O Python executa o cálculo do novo saldo, devolve o valor pelo return,
# mas como a chamada não está atribuida a uma variável,
# esse valor retornado é descartado da memória.

saldo = 200
atualizar_saldo(saldo,50)
print(saldo)
print()

# 3. CAPTURANDO UMA CONVERSÃO INVÁLIDA
# Percorra os textos ["12", "abc", "", "-4", "3.5", "0"].
# Para cada texto, tente convertê-lo diretamente com int dentro de try.
# Capture ValueError e mostre "Inteiro inválido" quando a conversão falhar.
# Use else para mostrar o resultado quando a conversão funcionar.
# Nesta etapa, negativos são aceitos. O programa deve chegar ao último texto.
# Conversões esperadas: 12, -4 e 0; três entradas devem ser rejeitadas.

entradas = ["12", "abc", "", "-4", "3.5", "0", " 012 "]

for entrada in entradas:
    try:
          saida = int(entrada)
    except ValueError as erro:
         print(f"Inteiro inválido! {erro}")
    else:
         print(f"Valor registrado: {saida}")
print()

# 4. OUTRO TIPO DE EXCEÇÃO
# Percorra os pares [(10, 2), (5, 0), (0, 4), (-6, 3)].
# Use try/except ZeroDivisionError para calcular numerador / denominador.
# Se o denominador for zero, mostre "Não é possível dividir por zero".
# Nos outros casos, mostre o resultado. Não substitua a falha pelo número zero.
# Resultados válidos esperados: 5.0, 0.0 e -2.0.

pares = [(10, 2), (5, 0), (0, 4), (-6, 3)]

for par in pares:
    try:
         divisao = par[0]/par[1]
         print(f"{divisao}")
    except ZeroDivisionError:
        print("Não é possível dividir por zero.")
print()

# 5. CONVERTER NÃO É O MESMO QUE VALIDAR
# Crie converter_estoque(texto), que converta uma string diretamente com int.
# Retorne o inteiro quando ele for maior ou igual a zero.
# Se o inteiro for negativo, lance ValueError com uma mensagem explicativa.
# Deixe o ValueError da conversão chegar ao código que chama a função.
# Fora dela, teste as entradas com try/except ValueError e mostre o resultado
# ou uma mensagem de erro. A função não deve imprimir nem pedir entrada.
# Casos: " 8 " -> 8; "0" -> 0; "-2", "2.5", "abc" e "" -> ValueError.

def converter_estoque(texto):
    try:
        conversao = int(texto)  
    except ValueError:
        raise ValueError(f"Str não converte em type(int): {texto}")
    if conversao < 0:
        raise ValueError(f"Não é aceito valor negativo: {conversao}")
    return conversao

testes = ['8','0','-2','-1','6','2.5','abc','']

for teste in testes:
    try:
        estoque = converter_estoque(teste)
        print(f"Estoque convertido: {estoque}")
    except ValueError as erro:
        print(f"Valor inválido! {erro}")
print()

# 6. TEXTO OBRIGATÓRIO
# Crie validar_descricao(texto), que retire espaços das extremidades e retorne
# a descrição, preservando maiúsculas e minúsculas.
# Se o resultado ficar vazio, lance ValueError com uma mensagem explicativa.
# Não crie outras restrições: descrições como "Compra 2" são permitidas.
# Teste: "  Mercado  " -> "Mercado"; "Compra 2" -> "Compra 2";
# "" e "   " -> ValueError. Capture a exceção fora da função.

def validar_descricao(texto):
    descricao = texto.strip()

    if descricao == '':
        raise ValueError("Descição vazia!")
    return descricao

testes = [' Casa', ' escola ', 'Prefeitura', ' CIDADE   ', '   ', '']

for teste in testes:
    try:
        descricao = validar_descricao(teste)
        print(f"Texto formatado: {descricao}")
    except ValueError as erro:
        print(erro)
print()

# 7. NÚMERO DECIMAL E INTERVALO
# Crie converter_nota(texto), que aceite ponto ou vírgula decimal e espaços
# nas extremidades, sem separador de milhar. Converta com float.
# Retorne a nota somente se ela pertencer ao intervalo de 0 a 10, inclusive.
# Caso contrário, lance ValueError. Entradas não numéricas também devem gerar
# ValueError, sem devolver None, zero ou mensagens no lugar de uma nota.
# A função não deve usar input nem print.
# Teste: " 7,5 " -> 7.5; "0" -> 0.0; "10" -> 10.0; "8.25" -> 8.25;
# "-1", "11", "abc", "", "nan" e "inf" -> ValueError.
# Lembre-se da condição de pertencimento ao intervalo apresentada na aula.

def converter_nota(texto):
    try:
        texto_limpo = texto.strip().replace(',','.')
        nota = float(texto_limpo)
        if (0<= nota <=10):
            return nota
    except ValueError:
        pass
    raise ValueError

testes = ['0',' 2.5',' 6.7  ',' 12',' 3.8 ', '10', '-6',' 0.5', '', 'nan', 'inf', 'abc']

for teste in testes:
    try:
        nota = converter_nota(teste)
        print(nota)
    except ValueError:
        print("Nota inválida!")
print()

# 8. ANÁLISE COM ENTRADAS REJEITADAS
# Use converter_nota para processar esta lista, preservando-a:
# entradas = ["7,5", "", "dez", "10", "-1", "0"]
# Crie analisar_notas(entradas), que retorne um dicionário com:
# - "notas": nova lista com as notas válidas na ordem original;
# - "rejeitadas": nova lista com os textos originais que geraram ValueError;
# - "media": média apenas das notas válidas ou None se não houver nenhuma.
# Capture ValueError por entrada, para continuar após uma rejeição.
# Fora da função, imprima o resumo. Mostre a média com duas casas decimais
# quando existir; caso contrário, mostre "Sem notas válidas".
# Caso principal: notas [7.5, 10.0, 0.0], rejeitadas ["", "dez", "-1"],
# média exibida 5.83. O zero deve participar do cálculo.
# Teste também [] e ["erro", ""]: notas [], média None.
# Explique por que substituir cada nota inválida por zero distorceria a média.

def analisar_notas(entradas):
    
    notas = []
    rejeitadas = []

    for entrada in entradas:
        try:
            nota = converter_nota(entrada)
            notas.append(nota)
        except ValueError:
            rejeitadas.append(entrada)
    media = round(sum(notas) / len(notas),2) if notas else None

    return {'notas': notas, 
            'rejeitadas': rejeitadas, 
            'media': media}

testes = [["7,5", "", "dez", "10", "-1", "0"],[],['erro',''],['10','6.4','-1.8','0'], ['0','0.00','0.0']]

for teste in testes:
    resumo = analisar_notas(teste)
    if resumo['media'] != None:
        print(f"""Resumo das notas:
Notas registradas: {resumo['notas']}
Registros inválidos: {resumo['rejeitadas']}
Média das notas: {(resumo['media']):.2f}
\n""")
    else:
        print(f"""Resumo das notas:
Notas registradas: {resumo['notas']}
Registros inválidos: {resumo['rejeitadas']}
Média das notas: Sem notas válidas.
\n""")

# Se converter valores rejeitados em 0 e adicioná-los à lista de notas para análise,
# distorceria a média, pois a média divide a soma de n pela contagem de n, desse modo, a média seria
# enviezada para baixo.

# 9. REPETIR ATÉ OBTER UMA NOTA VÁLIDA
# Crie ler_nota(), usando while, input e a função converter_nota.
# Capture ValueError, mostre uma orientação e peça novamente.
# Quando a entrada for válida, retorne a nota, encerrando o laço e a função.
# Chame ler_nota e imprima o resultado fora dela.
# Teste digitando, nesta ordem: abc, -1, 11 e 7,5.
# As três primeiras tentativas devem ser recusadas; a última deve retornar 7.5.
# Em outra execução, teste 0: ele deve ser aceito imediatamente.

def ler_nota():
    while True:
        texto = input("Insira uma nota: ")

        try:
            nota = converter_nota(texto)
        except ValueError:
            print('Nota inválida!')
            continue
        break
    return nota

testes = ['abc','-1','11','7,5']

nota = ler_nota()
print(f"Nota registrada: {nota}")
print()

# 10. DESAFIO — CADASTRO DE NOTAS COM ENCERRAMENTO
# Crie coletar_notas(), que peça notas até a pessoa digitar "fim".
# Reconheça também " FIM " e outras variações de caixa e espaços externos.
# Verifique a opção de encerramento antes de tentar converter a entrada.
# Reutilize converter_nota. Se ocorrer ValueError, avise e continue pedindo.
# Guarde apenas notas válidas em uma lista local e retorne-a ao encerrar.
# Fora da função, exiba quantidade, maior, menor e média das notas.
# Se a lista estiver vazia, exiba "Nenhuma nota registrada" e evite os cálculos.
# Não use uma lista global para armazenar os dados.
# Testes manuais:
# - fim imediatamente -> nenhuma nota registrada;
# - 8, abc, 12, 6, fim -> 2 notas, maior 8, menor 6, média 7;
# - 0, FIM -> 1 nota, maior 0, menor 0, média 0;
# - 7,5, 10, " FIM " -> 2 notas, maior 10, menor 7.5, média 8.75.
# Nos testes acima, cada item separado por vírgula e espaço é uma digitação;
# 7,5 representa uma única entrada decimal. Não digite as aspas de " FIM ".

def coletar_notas():
    notas = []
    while True:
        texto = input("Insira a nota ('fim' para encerrar): ").strip().lower()
        if texto == 'fim':
            return notas
        try:
            nota = converter_nota(texto)
            notas.append(nota)
        except ValueError:
            print("Nota inválida!")
            continue

notas = coletar_notas()
if len(notas) > 0:
    qtd_notas = len(notas)
    maior_nota = max(notas)
    menor_nota = min(notas)
    media = sum(notas)/qtd_notas
    print(f"""Resumo das notas:
{qtd_notas} Notas registradas.
Maior nota: {maior_nota}
Menor nota: {menor_nota}
Média das notas: {media:.2f}
\n""")
else:
    print("Nenhuma nota registrada.\n")

# AUTOAVALIAÇÃO
# - Sei explicar por que uma atribuição local não muda uma variável global?
# - Consigo distinguir conversão inválida de valor fora da regra?
# - Capturei somente as exceções esperadas, no lugar apropriado?
# - Minhas funções de validação retornam dados válidos ou lançam ValueError?
# - Testei zero, negativos, vazios e os limites exatos do intervalo?
# - Um erro de digitação permite tentar novamente sem perder os dados válidos?
