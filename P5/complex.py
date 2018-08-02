#! python3


class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return str(self.real) + "+" + str(self.imag) + "i"
        else:
            return str(self.real) + str((self.imag)) + "i"

    def __add__(self, c2):
        return(Complex(self.real + c2.real, self.imag + c2.imag))

    def __sub__(self, c2):
        return(Complex(self.real - c2.real, self.imag - c2.imag))

    def __mul__(self, c2):
        a = self.real
        b = self.imag
        c = c2.real
        d = c2.imag
        return(Complex(a * c - b * d, a * d + b * c))

    def __truediv__(self, c2):
        a = self.real
        b = self.imag
        c = c2.real
        d = c2.imag
        modulus = pow(c, 2) + pow(d, 2)
        return(Complex(((a * c + b * d) / modulus), ((b * c - a * d) / modulus)))


if __name__ == "__main__":
    file = open('numbers.txt', 'r')
    lines = file.readlines()
    # print(lines[0])
    # print(lines[1])
    [x1, y1] = lines[0].split(" ")
    [x2, y2] = lines[1].split(" ")
    # print(x1)
    # print(y1)
    # print(x2)
    # print(y2)
    c1 = Complex(int(x1), int(y1))
    c2 = Complex(int(x2), int(y2))
    print(c1)
    print(c2)
    print(c1 + c2)
    print(c1 - c2)
    print(c1 * c2)
    print(c1 / c2)
