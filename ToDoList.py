edit_message = "Qual tarefa deseja editar? "
task_message = "Tarefa: "
delete_task_message = "Qual tarefa deseja apagar? "
nome_arquivo = 'todolist.txt'

help_message = ("\n_____________HELP\n\n(h)elp:   ajuda\n(l)ist:    mostra todas as tarefas\n"
                  "(d)elete:  apaga uma tarefa\n(e)dit:     edita uma tarefa\n"
                  "(s)ave:  save to file\n(clear):  limpa a lista\n"
                  "Quit:    Encerra o programa\nOutros:  adiciona uma tarefa\n")

tarefas = []

def list_items():
    # print("_____________ITENS")
    for i, item in enumerate(tarefas, start=1):
        print(f"{i}. {item}")
    print()

def save():
# SAVE THE FILE TO DISK
    print(f"\n_____________SAVED TO {nome_arquivo}")
    with open(nome_arquivo, 'w') as arquivo:
        for item in tarefas:
            arquivo.write(f'{item}\n')

def load():
    try:
        with open(nome_arquivo,'r') as arquivo:
            for tarefa in arquivo:
                tarefas.append(tarefa.strip())
        print("Arquivo de tarefas encontrado. Carregando...")
        list_items()
    except Exception as e:
        print("Iniciando nova lista...")

print("\nThe_Funcky_ToDoList__a_Python_Experiment\n")

# obtem a entrada do usuario e executa a ação desejada
load()
while True:
    user_prompt = input(task_message)

    match user_prompt.capitalize():
        case 'Help' | '?' | 'H' | '':
            print(help_message)
            print(f"TASKS: ",len(tarefas)," tarefas\n")

        case 'List' | 'L':
            print("\n_____________LIST")
            list_items()

        case 'Edit' | 'E':
            print("\n_____________EDIT")
            list_items()
            indice = int(input(edit_message))-1
            new_task = input("Nova tarefa: ")
            tarefas[indice] = new_task

        case 'Delete' | 'Del' | 'D':
            print("\n_____________DELETE")
            list_items()
            indice = int(input(delete_task_message))-1
            try:
                print(f"Apagando {tarefas[indice]}\n")
                del tarefas[indice]
            except:
                print("Verifique o numero da tarefa. Não foi possivel remover. ")
            list_items()

        case 'Save' | 'S':
            save()

        case 'Quit' | 'Exit':
            save()
            break

        case 'Clear':
            print("Limpando a lista de tarefas...")
            tarefas = []

        case _:
            # print(f"Tarefa adicionada: {user_prompt}")
            tarefas.append(user_prompt)

print("____T_K_S_B_R_O_!_!_!_!___\n")