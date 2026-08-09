# Write your solution here

def transpose(matrix: list):

    transposed = []

    for c in range(len(matrix[0])):
        new_row= []
        for r in range(len(matrix)):
            new_row.append(matrix[r][c])
        transposed.append(new_row)

    matrix[:] = transposed


if __name__ == "__main__":
    matrix = [[10, 100], [10, 100]]
    transpose(matrix)
    print("after")
    print(matrix)