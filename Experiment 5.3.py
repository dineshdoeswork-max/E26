# 5.3 Function to read a matrix from a file (Module 4: File Handling)

def read_matrix(filename):
    matrix = []
    with open(filename, "r") as f:
        for line in f:
            row = [int(x) for x in line.split()]
            matrix.append(row)
    return matrix

matrix_a = read_matrix(r"E:\Xie Python\Experiments\Experiment 5.3\matrix1.txt")
matrix_b = read_matrix(r"E:\Xie Python\Experiments\Experiment 5.3\matrix2.txt")

print("Matrix A = ")
print(matrix_a[0])
print(matrix_a[1])

print("Matrix B = ")
print(matrix_b[0])
print(matrix_b[1])

rows = len(matrix_a)
cols = len(matrix_a[0])

result_add = []

for i in range(rows):
    new_row = []
    for j in range(cols):
        sum_val = matrix_a[i][j] + matrix_b[i][j]
        new_row.append(sum_val)
    result_add.append(new_row)


transpose = []

for j in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(matrix_a[i][j])
    transpose.append(new_row)


print("--- Matrix Addition ---")
for row in result_add:
    print(row)

print("\n--- Transpose of Matrix A ---")
for row in transpose:
    print(row)