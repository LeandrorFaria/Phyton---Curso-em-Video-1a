# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo calcule e mostre o comprimento da hipotenusa.

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = ((co ** 2) + (ca ** 2)) ** 0.5
print('A hipotenuza vai medir {:.2f} .'.format(h))

# -- outro modo
from math import hypot
hi2 = hypot(co, ca)
print('A hipotenuza vai medir {:.2f} .'.format(hi2))

# -- outro modo
import math
hi = math.hypot(co,ca)
print('A hipotenuza vai medir {:.2f} .'.format(hi))


