import os
import json
global terminada

def adicionar():
    limpar()
    global terminada 
    terminada = False
    desenhar_linha()
    print('ADICIONAR NOVA TAREFA'.center(50))
    desenhar_linha()
    try:
        tarefa = str(input('Tarefa a ser adicionada:'))
    except KeyboardInterrupt:
        print('\n\033[31mPreencha devidamente os campos!\033[m')
        return 
    except TypeError:
        print('\n\033[31mApenas são aceites letras\033[m')
        return 
    except ValueError:
        print('\n\033[31mNão esperávamos esse tipo de valor\033[m')
        return 
    else:
        with open('tarefas.json') as lista_tarefas:
            tarefas = json.load(lista_tarefas)

            nova_tarefa = {
                "tarefa": tarefa,
                "terminada": terminada
            }
            tarefas.append(nova_tarefa)
            with open('tarefas.json', 'w') as guardar:
                json.dump(tarefas, guardar, indent=4)
        print('Tarefa salva!')
        voltar_ao_menu()

def terminar_tarefa():
    limpar()
    with open('tarefas.json') as lista_tarefas:
        cont = 0
        tarefas = json.load(lista_tarefas)
        desenhar_linha()
        print('TERMINAR TAREFA'.center(50))
        desenhar_linha()
        if not tarefas:
            print('A lista ainda está vazia!')
            voltar_ao_menu()
        terminar = input('Digite a tarefa a ser terminada:')
        for task in tarefas:
        
            if task["tarefa"] == terminar:
                cont = 1
                task["terminada"] = True
                print('Tarefa terminada')
                break
        if cont == 0:
            print('Tarefa não encontrada')
            voltar_ao_menu()
        with open('tarefas.json', 'w') as guardar:
            json.dump(tarefas, guardar, indent=4)
    voltar_ao_menu()

def eliminar():
    limpar()
    with open('tarefas.json') as lista_tarefas:
        tarefas = json.load(lista_tarefas)
        desenhar_linha()
        print('REMOVER TAREFA'.center(50))
        desenhar_linha()
        if not tarefas:
            print('A lista ainda está vazia!')
            voltar_ao_menu()
        remover = input('Digite a tarefa a ser removido:')
        for task in tarefas:
            if task["tarefa"] == remover:
                tarefas.remove(task)
                print('Tarefa removida!')
                break
        with open('tarefas.json', 'w') as guardar:
            json.dump(tarefas, guardar, indent=4)
    voltar_ao_menu()

def ver_tarefas():
    limpar()
    with open('tarefas.json') as lista_tarefas:
        tarefas = json.load(lista_tarefas)
        desenhar_linha()
        print('SUAS TAREFAS'.center(50))
        desenhar_linha()
        if not tarefas:
            print('A lista ainda está vazia!')
        for task in tarefas:
            print(f'\033[31mTarefa\033[m: {task["tarefa"]}')
            print(f'\033[31mEstá terminada?\033[m: {task["terminada"]}')
            desenhar_linha()
    voltar_ao_menu()

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def desenhar_linha():
    print('\033[32m=\033[m'*50)

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
    if not os.path.exists("tarefas.json"):
        with open("tarefas.json", "w") as f:
            json.dump([], f)
    limpar()
    desenhar_linha()
    print('BEM-VINDO A SUA AGENDA'.center(50))
    desenhar_linha()
    print('\033[32m1\033[m - Criar nova tarefa')
    print('\033[32m2\033[m - Remover uma tarefa')
    print('\033[32m3\033[m - Terminar tarefa')
    print('\033[32m4\033[m - Listar todas as tarefas')
    print('\033[32m5\033[m - Sair')
    try:
        desenhar_linha()
        opcao = int(input('Sua opção:'))
    except ValueError:
        print('\033[31mEra esperado um valor numérico\033[m')
        voltar_ao_menu()
    except KeyboardInterrupt:
        print('\033[31mDeves preencher o campo\033[m')
        voltar_ao_menu()
    else:
        match(opcao):
            case 1:
                adicionar()
            case 2:
                eliminar()
            case 3:
                terminar_tarefa()
            case 4:
                ver_tarefas()
            case 5:
                ...
            case _:
                print('\033[31mOpcão inválida\033[m')
                voltar_ao_menu()

if __name__ == '__main__':
    menu()