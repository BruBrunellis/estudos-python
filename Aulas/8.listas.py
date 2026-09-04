# Aula 8 — Listas
#
# Objetivo: criar, acessar, alterar e percorrer listas para organizar vários
# valores em uma única variável.
# Pré-requisitos: variáveis, tipos básicos, condicionais, while, for e range.

# Uma lista armazena vários valores em uma ordem definida.
# Seus itens ficam entre colchetes e são separados por vírgulas.
produtos = ["notebook", "mouse", "teclado"]
precos = [3500.00, 80.00, 150.00]

print(produtos)
print(precos)
print()

# Uma lista pode estar vazia e receber itens ao longo do programa.
vendas = []
print(f"Lista vazia: {vendas}")
print(f"Quantidade de vendas: {len(vendas)}\n")

# Cada item possui um índice. O primeiro índice é 0.
# Índices negativos contam a partir do final: -1 representa o último item.
print(f"Primeiro produto: {produtos[0]}")
print(f"Último produto: {produtos[-1]}")
print(f"Quantidade de produtos: {len(produtos)}\n")

# O fatiamento seleciona uma parte da lista.
# Assim como em range, o índice final não é incluído.
numeros = [10, 20, 30, 40, 50]
print(f"Do índice 1 ao 3: {numeros[1:4]}")
print(f"Os três primeiros: {numeros[:3]}")
print(f"Do terceiro até o final: {numeros[2:]}\n")

# Listas são mutáveis: podemos substituir seus itens.
produtos[1] = "mouse sem fio"
print(f"Lista alterada: {produtos}\n")

# Métodos comuns para adicionar itens:
# append adiciona um item ao final.
# insert adiciona um item em um índice específico.
# extend adiciona os itens de outra sequência.
produtos.append("monitor")
produtos.insert(1, "webcam")
produtos.extend(["headset", "microfone"])
print(f"Após as inclusões: {produtos}\n")

# Métodos comuns para remover itens:
# remove exclui a primeira ocorrência de um valor.
# pop exclui e devolve o item do índice informado; sem índice, usa o último.
produtos.remove("webcam")
produto_removido = produtos.pop()
print(f"Produto removido com pop: {produto_removido}")
print(f"Lista atual: {produtos}\n")

# Antes de usar remove, podemos verificar se o item existe com in.
produto_procurado = "monitor"

if produto_procurado in produtos:
    print(f"{produto_procurado} está cadastrado.")
else:
    print(f"{produto_procurado} não está cadastrado.")

print()

# O for percorre diretamente todos os itens de uma lista.
for produto in produtos:
    print(f"Produto: {produto}")

print()

# range e len permitem percorrer os índices quando precisamos da posição.
for indice in range(len(produtos)):
    print(f"Posição {indice}: {produtos[indice]}")

print()

# count informa quantas vezes um valor aparece.
# index informa o índice da primeira ocorrência, mas gera erro se não encontrar.
categorias = ["livros", "eletrônicos", "livros", "casa"]
print(f"Quantidade de 'livros': {categorias.count('livros')}")

if "eletrônicos" in categorias:
    print(f"Índice de 'eletrônicos': {categorias.index('eletrônicos')}\n")

# sort ordena a própria lista e, portanto, modifica o valor original.
# sorted cria uma nova lista ordenada e preserva a original.
valores = [420.00, 150.00, 890.00, 275.00]
valores_ordenados = sorted(valores)
print(f"Valores originais: {valores}")
print(f"Valores ordenados: {valores_ordenados}\n")

# Atenção à diferença entre referência e cópia.
# A atribuição abaixo faz as duas variáveis apontarem para a mesma lista.
lista_original = [10, 20, 30]
mesma_lista = lista_original
mesma_lista.append(40)
print(f"Original após alterar a referência: {lista_original}")

# copy cria uma lista independente.
copia = lista_original.copy()
copia.append(50)
print(f"Original preservada: {lista_original}")
print(f"Cópia alterada: {copia}\n")

# Ponte para análise de dados:
# Uma coluna pequena de uma tabela pode ser representada por uma lista.
# Com ela, calculamos medidas e selecionamos valores de interesse.
vendas = [850.00, 1200.00, 430.00, 1560.00, 960.00]
total_vendas = sum(vendas)
media_vendas = total_vendas / len(vendas)
menor_venda = min(vendas)
maior_venda = max(vendas)
vendas_altas = []

for venda in vendas:
    if venda >= 1000:
        vendas_altas.append(venda)

print(f"Total: R$ {total_vendas:.2f}")
print(f"Média: R$ {media_vendas:.2f}")
print(f"Menor venda: R$ {menor_venda:.2f}")
print(f"Maior venda: R$ {maior_venda:.2f}")
print(f"Vendas a partir de R$ 1.000,00: {vendas_altas}")

# Erros comuns:
# - tentar acessar um índice que não existe, causando IndexError;
# - esquecer que o primeiro índice é 0;
# - usar remove para um valor que não está na lista;
# - confundir append com extend: append inclui um item, extend inclui vários;
# - calcular uma média de lista vazia, causando divisão por zero;
# - usar lista_b = lista_a esperando uma cópia independente;
# - esquecer que sort altera a lista original e não devolve uma nova lista.

# Boas práticas:
# - use nomes no plural para listas, como vendas, nomes e produtos;
# - verifique se a lista está vazia antes de calcular média, mínimo ou máximo;
# - use in antes de remove ou index quando o valor pode não existir;
# - prefira percorrer os itens diretamente quando não precisar dos índices.
