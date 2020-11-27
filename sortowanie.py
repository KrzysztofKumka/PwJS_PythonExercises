import numpy as np

def sort_fun(t):
    n = len(t)
    for i in range(0, n-1):
        for j in range (1, n-1):
            if t[j-1] > t[j]:
                x = t[j]
                t[j] = t[j-1]
                t[j-1] = x

    return t

def main():
    t = []
    for i in range (0, 50):
        t.append(np.random.randint(0, 100))

    print(t)

    sorted_t = sort_fun(t)

    print(sorted_t)

if __name__ == '__main__':
    main()