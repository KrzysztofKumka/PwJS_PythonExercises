import numpy as np

class Calculator(object):
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        return(self.num + num2.num)

    def __sub__(self, num2):
        return(self.num - num2.num)

    def __mul__(self, num2):
        return(self.num*num2.num)

    def __div__(self, num2):
        return(self.num/num2.num)

    def __sqrt__(self):
        return(np.sqrt(self.num))

    def __ret__(self):
        return str(self)


def equation(x1, eq, x2):
    if eq == '+':
        res = x1.__add__(x2)
        print('= ' + str(res))
        return res

    if eq == '-':
        res = x1.__sub__(x2)
        print('= ' + str(res))
        return res

    if eq == '*':
        res = x1.__mul__(x2)
        print('= ' + str(res))
        return res

    if eq == '/':
        res = x1.__div__(x2)
        print('= ' + str(res))
        return res


if __name__ == "__main__":
    i = 0
    #n = 0
    while (i < 10):
        x1, eq, x2 = map(str, input().split())
        n1 = Calculator(int(x1))
        n2 = Calculator(int(x2))
        n = equation(n1, eq, n2)
