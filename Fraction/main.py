class Fraction(object):
    def __init__(self,nominator,denominator):
        self.nominator = nominator
        self.denominator = denominator

    def value(self):
        result = float(self.nominator)/float(self.denominator)
        return result

    def __add__(self, other):
        return Fraction(self.nominator+other.nominator,self.denominator+other.denominator)

    def __sub__(self, other):
        return Fraction(self.nominator-other.nominator,self.nominator-other.denominator)

    def __mul__(self, other):
        return Fraction(self.nominator*other.denominator,self.denominator*other.denominator)

    def __truediv__(self, other):
        return Fraction(self.nominator/other.denominator,self.denominator/other.denominator)

    def __str__(self):
        return self.nominator+"/"+self.denominator
