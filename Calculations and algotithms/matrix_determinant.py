import numpy as np

def rand_matrix(n):
    ti1 = []
    for i in range(0, n):
        tj1 = []
        for j in range(0, n):
            tj1.append(np.random.randint(0, 10))
        ti1.append(tj1)

    return ti1

def matrix_determinant(matrix):
    return np.linalg.det(matrix)

def main():
    n = np.random.randint(0, 7)
    matrix = rand_matrix(4)
    print(matrix)

    determinant = matrix_determinant(matrix)
    print(determinant)


if __name__ == '__main__':
    main()