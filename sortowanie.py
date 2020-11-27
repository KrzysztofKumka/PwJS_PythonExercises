import numpy as np

def sort_fun(tab):
    n = len(tab)
    for i in range(0, n-1):
        for j in range (1, n-1):
            if tab[j-1] > tab[j]:
                x = tab[j]
                tab[j] = tab[j-1]
                tab[j-1] = x

    return tab

def main():
    t = []
    for i in range (0, 50):
        t.append(np.random.randint(0, 100))

    print(t)

    sorted_t = sort_fun(t)

    print(sorted_t)

if __name__ == '__main__':
    main()