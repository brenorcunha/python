m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
o = []

# Check if matrices have equal sizes:
def add_matrices(m, n):
    if (len(m) == len(n)) and (len(m[0]) == len(n[0])):
        for i in range(len(m)):
            # Create rows for O, otherwise they won't exist for the operations.
            row = [0] * len(m[0])
            o.append(row)
            for j in range(len(m[0])):
                o[i][j] = m[i][j] + n[i][j]
    else:
        print("Matrices do not have the same size.")
    return o

# Create a zero matrix to be filled later by the transpose method
def zero_matrix(num_rows, num_columns):
    m_zero = []
    for i in range(num_rows):
        row = [0] * num_columns
        m_zero.append(row)
    return m_zero

def transpose_matrix(n):
    num_rows = len(n)
    num_columns = len(n[0])
    # Create a zero matrix with transposed dimensions
    t = zero_matrix(num_columns, num_rows)
    for i in range(num_rows):
        for j in range(num_columns):
            t[j][i] = n[i][j]
    return t

def print_matrix(x):
    for i in x:
        # Why j in i? Because each i receives an element from the rows of m.
        for j in i:
            print(j, end=' ')
        print("\n")

"""
print("Matrix M:")
print_matrix(m)
print("Matrix N:")
print_matrix(n)
add_matrices(m, n)
print("Matrix O:")
print_matrix(o)
"""
print("Transposed Matrix N:")
print_matrix(transpose_matrix(n))
