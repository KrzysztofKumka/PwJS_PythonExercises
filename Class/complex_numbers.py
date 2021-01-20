class Complex_number(object):
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, num2):
        return Complex_number(self.real + num2.real, self.imag + num2.imag)

    def __sub__(self, num2):
        return Complex_number(self.real - num2.real, self.imag - num2.imag)

    def __mul__(self, num2):
        return Complex_number(self.real*num2.real + self.imag*num2.imag*(-1), self.real*num2.imag + self.imag*num2.real)

    def __cou__(self):
        return Complex_number(self.real, (-1)*self.imag)

    def __div__(self, num2):
        num2.cou_real = num2.real
        num2.cou_imag = num2.imag * (-1)
        x = self.real*num2.real - self.imag*num2.cou_imag
        y = self.real*num2.cou_imag + self.imag*num2.real

        z = num2.real*num2.real + num2.cou_imag*num2.cou_imag

        self.new_real = x/z
        self.new_imag = y/z
        result = Complex_number(self.new_real, self.new_imag)
        return result

    def __str__(self):
        return '(%g, %g)' % (self.real, self.imag)

    def __repr__(self):
        if self.imag > 0:
            result = "{} + {}i".format(self.real, self.imag)
        else:
            result = "{} {}i".format(self.real, self.imag)
        return result

if __name__ == "__main__":
    a = Complex_number(2.0, -1.0)
    b = Complex_number(-1.0, 4.0)
    c = a.__add__(b)
    d = a.__mul__(b)
    e = a.__div__(b)
    print(a.__repr__())