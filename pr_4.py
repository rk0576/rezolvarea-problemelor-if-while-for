  
from fractions import Fraction
x=int(input("numaratorul fractiei 1 este: "))
y=int(input("numitorul fractiei 1 este: "))
z=int(input("numaratorul fractiei 2 este: "))
w=int(input("numitorul fractiei 2 este: "))
print("suma este:",Fraction(x,y)+Fraction(z,w))
print("produsul este",Fraction(x,y)*Fraction(z,w))
