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


# Given a list, iterate it in reverse order and print each element.

listaNumeros3 = [10, 20, 30, 40, 50]
listaReversa = []
contador3 = 0

for numero3 in listaNumeros3:
    contador3 -=1
    listaReversa.append(listaNumeros3[contador3]) 

print(listaReversa)

print("\n----------------------------")
print("\n----------------------------")    

# Write a program that takes a string and reverses it using a for loop. 
# While Python’s [::-1] shortcut is famous, reversing a string manually is a classic 
# way to understand how sequences are constructed.

listaPalavras = 'Python'
listaPalavrasReversa = ''

for letra in listaPalavras:
    listaPalavrasReversa = letra + listaPalavrasReversa

print(listaPalavras)
print(listaPalavrasReversa)

print("\n----------------------------")
print("\n----------------------------")    


# Write a program that counts the total number of vowels and consonants
# in a given sentence, ignoring spaces and special characters.

listaVogais = 'aeiou'
frase = "Loops are Fun!"
numeroVogais = 0
numeroConsoante = 0

for letra in frase.lower():
    if letra.isalpha():
        if letra in listaVogais:
            numeroVogais += 1
        else:
            numeroConsoante += 1

print(numeroVogais)            
print(numeroConsoante)
    
