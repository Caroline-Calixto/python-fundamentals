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