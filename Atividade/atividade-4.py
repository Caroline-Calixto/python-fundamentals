# 4) Catálogo de livros
# As alunas da UFABC querem implementar um sistema simples que gerencie um catálogo de livros da biblioteca. 
# O programa deve permitir ao usuário adicionar novos livros (título e autor), 
# remover livros pelo título, e buscar livros por autor. Use um dicionário para armazenar os dados.
import sys

biblioteca = {}

continuar = 's'

def addLivros():
    titulo = input("digite o titulo do livro a adicionar: ")
    autor = input("digite o autor do livro a adicionar: ")
    biblioteca[titulo] = autor
    print("livro adicionado")
    print(biblioteca)
    
def removeByTitle():
    titulo = input("informe o titulo do livro a ser excluido: ")
    if titulo in biblioteca:
        del biblioteca[titulo]
        print(f"livro {titulo} removido")
    else: 
        print("Livro não encontrado")

def searchByauthor():
    autor = input("informe o nome do autor: ")

    if autor in biblioteca.values():
        for titulo in biblioteca:
            if biblioteca[titulo] == autor:
                print(f"titulo {titulo}")
    else:
        print("Autor não encontrado")

def selecModule(modulo):
    match modulo:
        case 1:
            return addLivros()
        case 2:
            return removeByTitle()
        case 3: 
            return searchByauthor()
        case _:
            print("saindo....")
            sys.exit()

while continuar == 's':
    print("======= biblioteca =======/n")
    print("1 - adicionar livros ")
    print("2 - remover por titulo ")
    print("3 - procurar por autor ")
    print("4 - Encerrar")
    
    modulo = int(input("Selecione o modulo da biblioteca: "))
    selecModule(modulo)
    
    