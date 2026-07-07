# 3) Tradutor simples
# Rose estuda programação e francês, assim, para entender melhor essas duas áreas do conhecimento ela pensa em criar um programa que funciona como um tradutor simples.
# O programa deve permitir ao usuário adicionar novas palavras e suas traduções (de uma língua para outra), remover palavras e buscar traduções, usando um dicionário para armazenar os dados.

dicionario = {}
continuar = 's'

def incluir():
        addPalavra = input("Adicione uma palavra ao seu dicionario: ")
        tradução = input("informe a tradução desta palavra: ")
        dicionario[addPalavra] = tradução
        return print(f"dicionario atualizado {dicionario}")
        
def consultar():
    consultaPalavra = input("Informe a palavra buscada: ")
    if consultaPalavra in dicionario:
        busca = dicionario[consultaPalavra]
        print(f"sua pesquisa retornou: {busca}")
    else:
        print("Não há resultados para a palavra consultada")

def excluir():
    removePalavra = input("informe a palavra que deseja remover: ")
    if removePalavra in dicionario:
        del dicionario[removePalavra]
        print(dicionario)
    else: 
        print("Não há resultados para a palavra consultada")

def selecionarModulo (modulo):
    match modulo:
        case 1:
            return incluir()
        case 2:
            return consultar()
        case 3:
            return excluir()
        case _:
            return "Encerrando..."
        
while continuar == 's':
    print("digite o modulo que deseja entrar: \n")
    modulo = int(input("1 - incluir | 2 - consultar | 3 - excluir: "))
    selecionarModulo(modulo)
    continuar = input("Deseja continuar? s ou n: ")
    


    





