# 2) Carrinho de Compras - Desafio
# Agora, pensando no cenário comercial, vamos agora criar o nosso carrinho de compras. Crie um código para que usuária possa:

# Coletar o nome do produto
# Verificar se ele está no nosso estoque
# Caso esteja, informar a quantidade disponível
# Coletar e adicionar no nosso carrinho:
# Quantidade do produto a ser vendida
# Valor a ser recebido pela venda deste produto
# Dica: Crie um dicionário com uma lista e a função criada na parte anterior para solucionar esta etapa.


estoque = {
    "arroz": {
        "quantidade": 20,
        "preco": 28.90
    },
    "feijao": {
        "quantidade": 15,
        "preco": 8.50
    },
    "açucar": {
        "quantidade": 18,
        "preco": 5.20
    },
    "cafe": {
        "quantidade": 12,
        "preco": 18.90
    }}

carrinho = {}
contador = 0

while True:

    produto = input("Digite o produto que deseja consultar: ").lower()

    if produto in estoque:
        print(f"{produto} em estoque! \n")
    
        quantidade = estoque[produto]["quantidade"]
        print(f"Existem {quantidade} em estoque! \n")
   
        addCarrinho = input("Deseja adicionar o produto no carrinho? (s/n): ").lower()

        if addCarrinho == "s":
            
            contador +=1
                  
            quantidadeCarrinho = int(input("digite a quantidade que deseja adicionar: "))
            precoCarrinho = int(input("digite o valor da venda: "))
            
            carrinho[contador] = {
                "produto": produto,
                "quantidade": quantidadeCarrinho,
                "preço": precoCarrinho
            }
                        
            print(f"Carrinho: {carrinho}")

        continuar = input("deseja continuar suas compras? (s/n): ").lower()
        
        if continuar == "n":
            break

    else:
        print(f"O produto {produto} não está no estoque.")


