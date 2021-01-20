def scalar_product(a, b):
    n = len(a)
    m = len(b)
    c = []

    for i in range (0, n):
        x = 0
        x = a[i]*b[i]
        c.append(x)

    result = sum(c)

    return result

def main():
    a = [1, 2, 12, 4]
    b = [2, 4, 2, 8]
    y = 0

    print(a)
    print(b)

    if len(a) == len(b):
        y = scalar_product(a, b)

    print(y)

if __name__ == '__main__':
    main()