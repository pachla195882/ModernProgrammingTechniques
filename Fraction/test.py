from main import Fraction

fraction = Fraction(2,2)
fraction2 = Fraction(3,3)


c = fraction.__add__(fraction2)

c = fraction + fraction2

fraction2.__sub__(fraction)
fraction.__mul__(fraction2)
fraction2.__truediv__(fraction)


print(c)