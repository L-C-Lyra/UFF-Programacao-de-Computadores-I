def read_matrices(num_rows, num_columns):
    matrix = []
    for _ in range(num_rows):
        row = list(map(int, input().split()))
        assert len(row) == num_columns, 'Incorrect amount of values in the line.'
        matrix.append(row)
    return matrix
    # raise NotImplementedError


def transposed_matrices(matrix, num_rows, num_columns):
    transposed_matrix = [None] * num_columns
    for row in range(num_columns):
        transposed_matrix[row] = [None] * num_rows
    for row in range(num_columns):
        for col in range(num_rows):
            transposed_matrix[row][col] = matrix[col][row]
    return transposed_matrix
    # raise NotImplementedError


def write_matrices(matrix, num_rows, num_columns):
    for row in range(num_rows):
        for col in range(num_columns - 1):
            print(matrix[row][col], end=" ")
        print(matrix[row][-1])
    # raise NotImplementedError


def main():
    order = int(input())
    matrix = read_matrices(order, order)
    transposed_matrix = transposed_matrices(matrix, order, order)
    write_matrices(matrix, order, order)
    write_matrices(transposed_matrix, order, order)


if __name__ == '__main__':
    main()
