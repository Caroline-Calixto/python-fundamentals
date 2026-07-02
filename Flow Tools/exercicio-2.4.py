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
    
print("\n----------------------------")
print("\n----------------------------")    
