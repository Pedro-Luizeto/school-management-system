
from time import sleep
import os

alunos = []


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def linha():
    print('=' * 30)


def espaco():
    print()


def cadastrar_aluno():
    nome = input("Digite o nome: ").strip()
    idade = int(input("Digite a idade: "))
    nota = float(input("Digite a nota: "))

    aluno = {
        'Nome': nome,
        'Idade': idade,
        'Nota': nota
    }

    alunos.append(aluno)
    print('Aluno cadastrado com sucesso!')


def remover_aluno():
    nome = input('Digite o nome do aluno que deseja remover: ').strip().lower()

    for aluno in alunos:
        if aluno['Nome'].lower() == nome:
            alunos.remove(aluno)
            print('Aluno removido com sucesso!')
            return

    print('Aluno não encontrado.')


def buscar_aluno():
    nome = input('Digite o nome do aluno que deseja buscar: ').strip().lower()

    for aluno in alunos:
        if aluno['Nome'].lower() == nome:
            print('Aluno encontrado!')
            print(f"Nome: {aluno['Nome']}")
            print(f"Idade: {aluno['Idade']}")
            print(f"Nota: {aluno['Nota']:.2f}")
            return

    print('Aluno não encontrado.')


def listar_alunos():
    print('=== LISTA DE ALUNOS ===')
    linha()

    if len(alunos) == 0:
        print('Nenhum aluno cadastrado.')
        return

    for aluno in alunos:
        print(f"Nome: {aluno['Nome']}")
        print(f"Idade: {aluno['Idade']}")
        print(f"Nota: {aluno['Nota']:.2f}")
        linha()


def media_geral():
    if len(alunos) == 0:
        print('Não existem alunos cadastrados.')
        return

    soma = 0

    for aluno in alunos:
        soma += aluno['Nota']

    media = soma / len(alunos)

    print(f'A média geral da turma é: {media:.2f}')


while True:
    limpar_tela()

    print('=== MENU ESCOLAR ===')
    linha()
    espaco()

    print('O que deseja fazer?')
    espaco()

    print('[1] - Adicionar aluno')
    print('[2] - Remover aluno pelo nome')
    print('[3] - Buscar aluno pelo nome')
    print('[4] - Listar todos os alunos')
    print('[5] - Mostrar média geral')
    print('[6] - Sair')

    linha()

    try:
        opcao_menu = int(input('> '))
    except ValueError:
        print('Digite uma opção válida!')
        sleep(2)
        continue

    limpar_tela()

    match opcao_menu:
        case 1:
            print('=== ADICIONAR ALUNO ===')
            cadastrar_aluno()

        case 2:
            print('=== REMOVER ALUNO ===')
            remover_aluno()

        case 3:
            print('=== BUSCAR ALUNO ===')
            buscar_aluno()

        case 4:
            print('=== LISTA DE ALUNOS ===')
            listar_alunos()

        case 5:
            print('=== MÉDIA GERAL ===')
            media_geral()

        case 6:
            print('Encerrando o programa...')
            sleep(1)
            break

        case _:
            print('Opção inválida!')

    espaco()
    input('Pressione ENTER para voltar ao menu...')
