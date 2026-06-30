# Write a program to print the first 10 natural numbers using a while loop. Each number should be printed on a new line.

contador = 0
while contador < 10:
  contador = contador +1
  print(contador)

print("\n----------------------------")     

# Write a program to display numbers from -10 to -1 using a for loop.

for contador in range (-10,0):
  print(contador)

print("\n----------------------------")   
  
# Write a program to display a message “Done” after the successful execution of a for loop that iterates from 0 to 4.

for contador in range(0,5):
  print(contador)
else:
  print("Done!")

print("\n----------------------------")   

# Write a program that accepts a number from the user and calculates the sum of all numbers from 1 up to that number.

# receber numero do usuário
numero = int(input("digite um numero: "))
# calcular a soma de todos os numeros ate o numero do input
soma = 0
for contador in range(numero + 1):
  soma = contador + soma
  # exibir o numero
  print(soma)

print("\n----------------------------")   
  
# Create a program that takes an integer and prints its multiplication table from 1 to 10.
n = int(input("digite um numero: "))

for contador in range(1,10):
  contador = n * contador
  print(n)

print("\n----------------------------")   
  
# Write a program that takes an integer n and prints the cube of every number from 1 to n in the format Current Number is : 1 and the cube is 1.

# O programa deve receber um número inteiro n.

n = int(input("digite um numero: "))
# Deve percorrer todos os números começando em 1 e terminando em n.
# Para cada valor de i entre 1 e n, faça o que está dentro do bloco."

cubo = 0
for i in range(1, n+1):
  cubo = i ** 3
  print(f"Current Number is: {n} and the cube is {cubo}")  
  
