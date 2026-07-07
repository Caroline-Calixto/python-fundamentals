#5) Notas de alunos
# As professoras do EducaMin@ precisam de um programa que leia o nome e as notas de vários alunos. 
# Para cada aluno, é necessário armazenar as notas em uma lista dentro de um dicionário, onde a chave 
# é o nome do aluno. O programa deve permitir a exibição das notas de um aluno específico e a média das notas de todos os alunos.

boletim = {
    "joao": 9,
    "maria": 8,
    "pedro": 6
}

# exibir nota por aluno
def exibirNota():
    consultaAluno = input("informe o nome do aluno: ")
    if consultaAluno in boletim:
        print(f"a nota do aluno {consultaAluno} é {boletim[consultaAluno]}")

# media das notas dos alunos
def mediaNotas():
    soma = sum(boletim.values())
    media = soma / len(boletim)
    print(f"a média da turma foi: {media}")

exibirNota()
mediaNotas()