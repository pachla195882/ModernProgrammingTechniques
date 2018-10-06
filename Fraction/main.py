from math import gcd

class Fraction(object):
    def __init__(self, numerator, denominator):
        greatestCommonDivisor = gcd(numerator, denominator)
        self.numerator = int(numerator / gcd(abs(numerator), abs(denominator)))
        self.denominator = int(denominator / gcd(abs(numerator), abs(denominator)))
        if self.denominator < 0:

            self.denominator *= -1
            self.numerator *= -1
        elif self.denominator == 0:
            
            raise ZeroDivisionError


    def value(self):
        result = float(self.numerator) // float(self.denominator)
        return result

    def __add__(self, other):
        return Fraction(self.numerator * other.denominator + self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        return Fraction(self.numerator * other.denominator - self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.denominator)

    def __str__(self):
        return "%s \ %s" % (self.numerator, self.denominator)