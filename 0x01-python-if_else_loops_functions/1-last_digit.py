#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
resultado2 = number * -1
if number < 0:
    resultado = (resultado2 % 10) * -1
else:
    resultado = number % 10
if resultado > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, resultado))
elif resultado == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, resultado))
else: 
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, resultado))