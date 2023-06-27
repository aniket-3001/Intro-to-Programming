class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imag = i

    def getreal(self):
        return self.real

    def getimag(self):
        return self.imag

    def add(self, c):
        self.real += c.getreal()
        self.imag += c.getimag()

    def equal(self, c):
        return self.real == c.getreal() and self.imag == c.getimag()

    def sub(self, c):
        self.real -= c.getreal()
        self.imag -= c.getimag()

    def mod(self):
        return (((self.real)**2)+((self.imag)**2))**0.5

    def conj(self):
        return (self.real, -self.imag)
