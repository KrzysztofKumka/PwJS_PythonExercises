import numpy as np

def matrix_sum(a, b):
    m = len(a)
    result = []

    for i in range(0, m):
        res_col = []
        for j in range(0,m):
            res_col.append(a[i][j] + b[i][j])
        result.append(res_col)

    return result

def rand_matrix():
    ti1 = []
    ti2 = []
    for i in range(0, 128):
        tj1 = []
        tj2 = []
        for j in range(0, 128):
            tj1.append(np.random.randint(0, 100))
            tj2.append(np.random.randint(0, 100))
        ti1.append(tj1)
        ti2.append(tj2)

    return ti1, ti2

def main():
    a, b = rand_matrix()
    c = matrix_sum(a, b)
    print(a)
    print(b)
    print(c)

if __name__ == '__main__':
    main()