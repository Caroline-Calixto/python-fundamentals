# Write a program that accepts a number from the user and calculates the sum of all numbers from 1 up to that number.

numero = int(input("digite um numero: "))
soma = 0

for contador in range(numero + 1):
  soma = contador + soma
  print(soma)
