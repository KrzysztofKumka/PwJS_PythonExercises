import numpy as np

def matrix_product(a, b):
    m = len(a)
    n = len(a[0])
    result = []

    for i in range(0,m):
        tj1 = []
        for j in range(0, m):
            tj1.append(0)
        result.append(tj1)

    #print(result)

    for i in range(0, m):
        for j in range(0, n):
            for k in range(0, m):
                result[i][j] += a[i][k]*b[k][j]
    return result

def rand_matrix():
    ti1 = []
    ti2 = []
    for i in range(0,8):
        tj1 = []
        tj2 = []
        for j in range(0, 8):
            tj1.append(np.random.randint(0, 5))
            tj2.append(np.random.randint(0, 5))
        ti1.append(tj1)
        ti2.append(tj2)

    return ti1, ti2

def main():
    a, b = rand_matrix()
    c = matrix_product(b, a)
    print(a)
    print(b)
    print("=")
    print(c)

if __name__ == '__main__':
    main()