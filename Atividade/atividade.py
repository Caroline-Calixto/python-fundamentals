# 1) Contagem de palavras
# Eliane quer escrever uma redação objetivando a nota 1000 noo Enem, 
# contudo percebeu que às vezes costuma ser repetitiva em suas produções por isso ela pede sua ajuda.
# Crie um programa que leia uma frase do usuário e conte a frequência de cada palavra na frase. 
# Imprima o resultado em um dicionário onde as chaves são as palavras e os valores são as contagens.

redação = {}
frase = input("digite seu texto: ")

palavras = frase.split()

for palavra in palavras:
    if  palavra in redação:
        redação[palavra] +=1
    else:
        redação[palavra] = 1

print(redação)        

# 2) Carrinho de Compras - Desafio
# Agora, pensando no cenário comercial, vamos agora criar o nosso carrinho de compras. Crie um código para que usuária possa:

# Coletar o nome do produto
# Verificar se ele está no nosso estoque
# Caso esteja, informar a quantidade disponível
# Coletar e adicionar no nosso carrinho:
# Quantidade do produto a ser vendida
# Valor a ser recebido pela venda deste produto
# Dica: Crie um dicionário com uma lista e a função criada na parte anterior para solucionar esta etapa.