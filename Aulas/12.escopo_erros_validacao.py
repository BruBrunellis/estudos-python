# Aula 12 — Escopo, tratamento de erros e validação
# Módulo 2 — Python aplicado a dados
#
# Objetivo: entender variáveis locais, tratar exceções específicas e validar
# entradas para que erros esperados não encerrem o programa.
# Pré-requisitos: funções, parâmetros, return, condicionais, while e coleções.
#
# Como estudar: preveja a saída de cada bloco antes de executar o arquivo.
# Os exemplos rodam sem digitação. Ao final, há uma prática interativa opcional.
# Sugestão: 20 minutos de exemplos, 45 de exercícios e 10 de revisão.

# -----------------------------------------------------------------------------
# 1. ESCOPO: ONDE UM NOME PODE SER USADO
# -----------------------------------------------------------------------------

# Variáveis criadas fora de funções pertencem ao escopo global do módulo.
# Parâmetros e variáveis atribuídas dentro da função são locais à chamada.
# Nomes iguais podem representar variáveis diferentes nesses dois escopos.
mensagem = "Relatório geral"


def criar_mensagem(nome):
    mensagem = f"Relatório de {nome}"
    return mensagem


print(criar_mensagem("Ana"))  # Relatório de Ana
print(mensagem)  # Relatório geral: a atribuição local não alterou a global.


def calcular_area(largura, altura):
    area_calculada = largura * altura
    return area_calculada


area = calcular_area(3, 4)
print(area)  # 12
# print(area_calculada) causaria NameError: esse nome é local à função.
# O return permite receber o resultado fora dela, com o nome que escolhermos.
# if e for não criam um novo escopo de função: variáveis atribuídas nesses
# blocos continuam pertencendo à função ou ao módulo que contém o bloco.

# -----------------------------------------------------------------------------
# 2. EVITANDO DEPENDÊNCIA DE VARIÁVEIS GLOBAIS
# -----------------------------------------------------------------------------

# Uma função pode ler uma variável global, mas receber dados por parâmetros
# torna suas dependências explícitas e facilita testar chamadas diferentes.
# Atribuir a um nome dentro da função normalmente faz dele um nome local.
# Por isso, ler esse nome antes da atribuição pode gerar UnboundLocalError.
# Exemplo de problema (comentado para não interromper a aula):
# contador = 0
# def incrementar():
#     contador += 1
# incrementar()
#
# Existe a palavra global para permitir reatribuições globais, mas nesta aula
# prefira passar o valor e devolver o resultado:


def incrementar(valor):
    return valor + 1


contador = 0
contador = incrementar(contador)
print(contador)  # 1

# Atenção: escopo local não significa cópia automática de uma lista recebida.
# append em um parâmetro que referencia uma lista altera esse mesmo objeto.
# Para produzir uma lista independente de números, podemos fazer uma cópia:


def incluir_medicao(medicoes, nova_medicao):
    novas_medicoes = medicoes.copy()
    novas_medicoes.append(nova_medicao)
    return novas_medicoes


originais = [18, 20]
atualizadas = incluir_medicao(originais, 22)
print(originais)  # [18, 20]
print(atualizadas)  # [18, 20, 22]
# copy cria uma cópia superficial: listas ou dicionários internos ainda seriam
# compartilhados. Aqui os elementos são números, e isso atende ao objetivo.

# -----------------------------------------------------------------------------
# 3. EXCEÇÕES E LEITURA DE ERROS
# -----------------------------------------------------------------------------

# Uma exceção sinaliza um problema durante a execução. Se não for tratada,
# interrompe o fluxo normal e pode encerrar o programa.
# No traceback, leia o tipo e a mensagem na última linha, depois localize a
# linha do seu código indicada acima dela.
#
# Exemplos frequentes:
# ValueError: int("abc") — o texto não representa um inteiro.
# TypeError: len(10) — esse tipo não suporta a operação.
# ZeroDivisionError: 10 / 0 — divisão por zero.
# NameError: usar um nome que não foi definido no escopo acessível.
# KeyError: acessar uma chave ausente usando dicionario["chave"].
#
# Na Aula 11, omitir um argumento obrigatório gerava TypeError ANTES de entrar
# no corpo da função. Corrija a chamada; não tente esconder esse erro.

# -----------------------------------------------------------------------------
# 4. TRY E EXCEPT: TRATAR UMA FALHA ESPERADA
# -----------------------------------------------------------------------------

texto_quantidade = "três"
try:
    quantidade = int(texto_quantidade)
except ValueError:
    print("Quantidade inválida: digite um número inteiro.")

print("O programa continuou após a tentativa de conversão.")

# try executa a operação que pode falhar. Se ocorrer ValueError, Python pula
# o restante desse try e executa o except correspondente.
# Um except ValueError não captura TypeError nem qualquer outro tipo de erro.
# Mantenha o try pequeno para ficar claro qual operação está sendo protegida.

texto_quantidade = "12"
try:
    quantidade = int(texto_quantidade)
except ValueError:
    print("Quantidade inválida.")
else:
    print(f"Quantidade convertida: {quantidade}")  # Quantidade convertida: 12

# else é opcional e roda quando o try termina sem exceção.
# Aqui, só usamos quantidade após uma conversão bem-sucedida.
# Não confunda esse else com o else de um if: observe a indentação.

# -----------------------------------------------------------------------------
# 5. CONVERSÃO E REGRA DE VALIDAÇÃO
# -----------------------------------------------------------------------------

# Conseguir converter não garante que o valor seja permitido.
# int("-3") funciona, mas uma quantidade de participantes não pode ser negativa.
# A regra deste exemplo permite zero: nenhum participante registrado.
entradas_quantidade = ["8", "-3", "abc", "", "0", "2.5"]

for entrada in entradas_quantidade:
    try:
        quantidade = int(entrada)
    except ValueError:
        print(f"{entrada!r}: não representa um inteiro.")
        continue

    if quantidade < 0:
        print(f"{entrada!r}: quantidade não pode ser negativa.")
        continue

    print(f"{entrada!r}: aceito -> {quantidade}")

# !r mostra a representação do texto, incluindo aspas, para enxergar o vazio.
# Entradas aceitas: "8" e "0". int("2.5") não aceita casas decimais.
# Evite int(float(texto)) para validar inteiros: isso truncaria valores como 2.5.

# -----------------------------------------------------------------------------
# 6. RAISE: SINALIZANDO UM VALOR INVÁLIDO EM UMA FUNÇÃO
# -----------------------------------------------------------------------------

# Uma função pode lançar ValueError quando um valor viola seu contrato.
# raise interrompe o fluxo normal da função e passa a exceção para quem chama.
# O código que chama pode capturá-la com except e decidir como responder.
# Contrato do exemplo: receber string, aceitar vírgula ou ponto decimal,
# sem separador de milhar, e permitir temperatura de -50 a 60 graus inclusive.


def converter_temperatura(texto):
    texto_limpo = texto.strip().replace(",", ".")
    temperatura = float(texto_limpo)

    if not (-50 <= temperatura <= 60):
        raise ValueError("A temperatura deve estar entre -50 e 60 °C.")

    return temperatura


entradas_temperatura = [" 23,5 ", "-10", "0", "80", "calor", ""]
for entrada in entradas_temperatura:
    try:
        temperatura = converter_temperatura(entrada)
    except ValueError as erro:
        print(f"Temperatura {entrada!r} rejeitada: {erro}")
    else:
        print(f"Temperatura aceita: {temperatura:.1f} °C")

# as erro permite acessar a mensagem da exceção.
# float pode gerar ValueError na conversão; nossa função também pode gerar
# ValueError pela regra do intervalo. Ambos chegam ao except da chamada.
# Curiosidade útil para dados: float aceita "nan" e "inf" como valores especiais.
# A condição de pertencimento ao intervalo acima também rejeita esses valores.
# Apenas testar temperatura < -50 or temperatura > 60 não rejeitaria NaN.

# -----------------------------------------------------------------------------
# 7. WHILE: PEDIR NOVAMENTE ATÉ RECEBER UMA ENTRADA VÁLIDA
# -----------------------------------------------------------------------------


def ler_temperatura():
    while True:
        entrada = input("Temperatura de -50 a 60 °C: ")
        try:
            temperatura = converter_temperatura(entrada)
        except ValueError:
            print("Digite um número entre -50 e 60. Exemplo: 23,5.")
        else:
            return temperatura


# A função de conversão não usa input nem print. A função de interação cuida
# da conversa com a pessoa. Isso permite reutilizar a conversão em outros fluxos.
# No except, o laço repete. No else, return encerra a função e o laço.
# Para experimentar, mude a variável abaixo para True e execute no terminal.
executar_pratica_interativa = True
if executar_pratica_interativa:
    temperatura_lida = ler_temperatura()
    print(f"Registro confirmado: {temperatura_lida:.1f} °C")

# -----------------------------------------------------------------------------
# 8. PONTE PARA ANÁLISE DE DADOS: MANTER REGISTROS DAS REJEIÇÕES
# -----------------------------------------------------------------------------

# Pergunta: qual a média das medições válidas deste pequeno conjunto?
# Fonte: strings fictícias de um sensor, preservadas na lista original.
# Limpeza: padronizar decimal, converter e aplicar o intervalo permitido.
dados_brutos = ["20", "22,5", "erro", "", "80", "17,5"]
medicoes_validas = []
rejeitados = []

for entrada in dados_brutos:
    try:
        medicao = converter_temperatura(entrada)
    except ValueError:
        rejeitados.append(entrada)
    else:
        medicoes_validas.append(medicao)

print(f"Medições válidas: {medicoes_validas}")  # [20.0, 22.5, 17.5]
print(f"Registros rejeitados: {rejeitados}")  # ['erro', '', '80']
if len(medicoes_validas) > 0:
    media = sum(medicoes_validas) / len(medicoes_validas)
    print(f"Média das medições válidas: {media:.1f} °C")  # 20.0 °C
else:
    print("Não há medições válidas para calcular a média.")

# Conclusão: a média dos três registros aceitos é 20.0 °C.
# Limitação: metade dos registros foi rejeitada. Essa média descreve somente
# as medições aceitas; seria necessário investigar as rejeições antes de usá-la
# como representação de todas as medições do sensor.
# Apresentação: um resumo textual basta aqui; não precisamos de gráfico.
# Nunca transforme uma entrada inválida em zero silenciosamente: isso altera
# totais e médias. Preserve a fonte e deixe explícito o que foi excluído.

# -----------------------------------------------------------------------------
# 9. ERROS COMUNS E BOAS PRÁTICAS
# -----------------------------------------------------------------------------

# Erros de execução:
# - tentar acessar uma variável local fora da função;
# - usar o resultado de uma conversão que falhou;
# - esquecer de capturar uma exceção esperada na interação com a pessoa.
#
# Erros de lógica:
# - aceitar um número só porque float ou int conseguiu convertê-lo;
# - devolver texto em um caminho e número em outro sem um contrato explícito;
# - colocar return antes da validação e tornar a validação inalcançável;
# - substituir dados inválidos por zero e alterar o significado da análise.
#
# Boas práticas:
# - capture tipos específicos; evite except: ou except Exception sem motivo;
# - não use except para esconder defeitos no seu próprio código;
# - prefira parâmetros e retorno a reatribuições globais;
# - defina se zero, negativos e extremos do intervalo são aceitos;
# - teste conversão inválida e valor fora da faixa separadamente;
# - mantenha separadas conversão/validação, interação e apresentação.
#
# Na Aula 13, aplicaremos esses cuidados à leitura e à escrita de arquivos.
