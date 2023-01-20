def processar_amortecimento_acumulado(tabela):
    tamanho = len(tabela['amort. acum.'])
    for i in range(tamanho):
        tabela['amort. acum.'][
            i] = tabela['ano'][i] * tabela['amortecimento'][i]


def aplicar_amortecimento_ao_valor(tabela):
    tamanho = len(tabela['valor'])
    for i in range(1, tamanho):  # pulando a primeira interação
        tabela['valor'][i] = tabela['valor'][i] - tabela['amort. acum.'][i - 1]


def concluir_valor_final(tabela):
    tamanho = len(tabela['final'])
    for i in range(tamanho):
        tabela['final'][i] = tabela['valor'][i] - tabela['amort. acum.'][i]


def imprimir_em_tabela(tabela):

    tamanho = len(tabela['ano'])

    for coluna in tabela.keys():
        print(coluna, end='\t')

    print()
    print('================================================')

    for linha in range(tamanho):
        for coluna in tabela.keys():
            tamanho_palavra_coluna = len(coluna)
            separator = ' ' * tamanho_palavra_coluna
            print(tabela[coluna][linha], end=separator)
        print()


# inicialização da tabela
dados = dict()
quantidade = 5
valor_base = 2000
amortecimento = 400
dados['ano'] = []
dados['valor'] = [valor_base] * quantidade
dados['amortecimento'] = [amortecimento] * quantidade
dados['amort. acum.'] = [amortecimento] * quantidade
dados['final'] = [valor_base] * quantidade

for i in range(1, quantidade + 1):
    dados['ano'].append(i)

processar_amortecimento_acumulado(dados)
aplicar_amortecimento_ao_valor(dados)
concluir_valor_final(dados)
imprimir_em_tabela(dados)
