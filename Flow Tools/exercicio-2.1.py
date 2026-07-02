
#Given a Python list, use a loop to print only the elements 
# that are located at odd index positions (index 1, 3, 5, etc.).

listaNumeros2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
contador2 = 0
posição = listaNumeros2[1]

for numero2 in listaNumeros2:
    if numero2 == posição:
        contador2 += 1
        
print(f"exibindo os elementos da posição {listaNumeros2.index(posição)}: {posição} ")

print("\n----------------------------")
print("\n----------------------------")

