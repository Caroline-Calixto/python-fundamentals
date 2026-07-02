# Write a program to use a loop to find the factorial of a given number (e.g., 5!). 
# The factorial of N is the product of all integers from 1 to N.

# usuario digita numero
# numero * (numero -1)
# quantidade de multiplicações é predeterminada por (numenro -1)
# limite é 1

import math

numero = int(input("insira um numero: "))
fatorial = math.factorial(numero)

print(fatorial)

#--------------------------
#n! = n . (n – 1) . (n – 2) . ... . (n – (n-1))!
numero = int(input("digite um numero: "))
fatorial = 1

for i in range(1, numero+1):
    fatorial = i * fatorial
    print(fatorial)

    