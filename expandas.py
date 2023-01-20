# import numpy as np
# import pandas as pd

# dados = []

# for i in range(1, 6):
#     dados.append([i] * 5)

# colunas = ['ano', 'valor', 'amort.', 'amort. acum.', 'final']

# df = pd.DataFrame(dados, columns=colunas)

# df['valor'] = 2000
# df['amort.'] = 400
# df['amort. acum.'] = df['amort.'] * df['ano']
# df['amort. acum.'] = df['amort.'] * df['ano']
# df['valor'] = df['valor'] - df['amort. acum.'].shift()

# print(df)
