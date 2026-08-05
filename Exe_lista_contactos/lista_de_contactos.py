import json
import os

def adicionar():
    limpar()
    desenhar_linha()
    print('CRIAR NOVO CONTACTO'.center(34))
    desenhar_linha()
    try:
        numero = int(input('Informe o número a adicionar:'))
        nome = str(input('Gravar como:'))
    except KeyboardInterrupt:
        print('\n\033[32mPreencha devidamente os campos!\033[m')
        return 
    except ValueError:
        print('\nNão esperávamos esse tipo de valor')
        return 
    else:
        with open('contactos.json') as lista_contactos:
            contactos = json.load(lista_contactos)
            novo_contacto = {
                "nome":nome,
                "contacto":numero
            }
            for pessoa in contactos:
                if pessoa["contacto"] == numero:
                    print("Esse número já existe.")
                    voltar_ao_menu()
                    return
            contactos.append(novo_contacto)
            with open('contactos.json', 'w') as guardar:
                json.dump(contactos, guardar, indent=4)
        print('Contacto salvo!')
        voltar_ao_menu()

def ver_contactos():
    limpar()
    with open('contactos.json') as lista_contactos:
        contactos = json.load(lista_contactos)
        desenhar_linha()
        print('SEUS CONTACTOS'.center(34))
        desenhar_linha()
        if not contactos:
            print('A lista ainda está vazia!')
        for pessoa in contactos:
            print(f'\033[31mNome\033[m: {pessoa["nome"]}')
            print(f'\033[31mNúmero\033[m: {pessoa["contacto"]}')
            desenhar_linha()
    voltar_ao_menu()

def remover_contacto():
    limpar()
    with open('contactos.json') as lista_contactos:
        contactos = json.load(lista_contactos)
        desenhar_linha()
        print('REMOVER CONTACTO'.center(34))
        desenhar_linha()
        if not contactos:
            print('A lista ainda está vazia!')
            voltar_ao_menu()
        remover = input('Digite o nome do contacto a ser removido:')
        for pessoa in contactos:
            if pessoa["nome"] == remover:
                contactos.remove(pessoa)
                print('Contacto removido!')
                break
        with open('contactos.json', 'w') as guardar:
            json.dump(contactos, guardar, indent=4)
    voltar_ao_menu()

def desenhar_linha():
    print('\033[32m=\033[m'*34)

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def voltar_ao_menu():
    try:
        resposta = input('Voltar ao menu?[S][N]')
    except ValueError:
        print('Digite apenas [S] ou [N]')
        voltar_ao_menu()
    except KeyboardInterrupt:
        print('Deves preencher o campo')
    else:
        if resposta.upper() == 'S':
            return menu()

def menu():
    if not os.path.exists("contactos.json"):
        with open("contactos.json", "w") as f:
            json.dump([], f)
    limpar()
    desenhar_linha()
    print('BEM-VINDO A SUA LISTA DE CONTACTOS')
    desenhar_linha()
    print('\033[32m1\033[m - Criar novo contacto')
    print('\033[32m2\033[m - Remover um contacto')
    print('\033[32m3\033[m - Listar todos contactos')
    print('\033[32m4\033[m - Sair')
    try:
        desenhar_linha()
        opcao = int(input('Sua opção:'))
    except ValueError:
        print('Era esperado um valor numérico')
        voltar_ao_menu()
    except KeyboardInterrupt:
        print('Deves preencher o campo')
        voltar_ao_menu()
    else:
        match opcao:
            case 1:
                adicionar()
            case 2:
                remover_contacto()
            case 3:
                ver_contactos()
            case 4:
                ...
            case _:
                print('Opcão inválida')
                voltar_ao_menu()


menu()
