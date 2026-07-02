# Write a program that takes an integer n and prints the cube of every number from 1 to n in the format Current Number is : 1 and the cube is 1.

# O programa deve receber um número inteiro n.

n = int(input("digite um numero: "))
# Deve percorrer todos os números começando em 1 e terminando em n.
# Para cada valor de i entre 1 e n, faça o que está dentro do bloco."

cubo = 0
for i in range(1, n+1):
  cubo = i ** 3
  print(f"Current Number is: {n} and the cube is {cubo}")  
  