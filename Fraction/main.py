from math import gcd

class Fraction(object):
    def __init__(self,nominator,denominator):
        self.nominator = nominator/gcd(nominator,denominator)
        self.denominator = denominator/gcd(nominator,denominator)
        if denominator < 0:
            raise ValueError("Denominator is smaller than zero!")
        elif nominator < 0:
            raise ValueError("Nominator is smaller than zero!")
        elif denominator == 0:
            raise ValueError("Denominator is equal to 0!")


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
        return "%s \ %s" % ( self.nominator, self.denominator )