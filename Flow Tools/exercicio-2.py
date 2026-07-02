# Given a list of numbers, use a loop to count how many times 
# a specific number (e.g., 10) appears.

listaNumeros1 = [10, 20, 10, 30, 10, 40, 50]
contador1 = 0

for numero in listaNumeros1:
    if numero == 10:
        contador1 += 1
        
print(f"o numero 10 apareceu {contador1} vezes\n")

print("\n----------------------------")
print("\n----------------------------")

