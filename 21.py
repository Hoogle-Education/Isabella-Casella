def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()


def sum_matrix(matrix):
    soma = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            soma = soma + matrix[i][j]

    return soma


matrix = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]

print_matrix(matrix)
soma_total = sum_matrix(matrix)
print(soma_total)

# matriz[i][j] | i: linha, j: coluna

