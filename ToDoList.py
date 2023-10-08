#  ██████   █████  ███████ ███████ ████████  █████   ██████
# ██       ██   ██    ███  ██         ██    ██   ██ ██    ██
# ██   ███ ███████   ███   ███████    ██    ███████ ██    ██
# ██    ██ ██   ██  ███         ██    ██    ██   ██ ██    ██
#  ██████  ██   ██ ███████ ███████    ██    ██   ██  ██████

print("      ___       _______      ___       ________   _______  __  .______       _______      _______.")
print("     /   \     |   ____|    /   \     |       /  |   ____||  | |   _  \     |   ____|    /       |")
print("    /  ^  \    |  |__      /  ^  \    `---/  /   |  |__   |  | |  |_)  |    |  |__      |   (----`")
print("   /  /_\  \   |   __|    /  /_\  \      /  /    |   __|  |  | |      /     |   __|      \\   \\")
print("  /  _____  \  |  |      /  _____  \    /  /----.|  |____ |  | |  |\  \----.|  |____ .----)   |  ")
print(" /__/     \__\ |__|     /__/     \__\  /________||_______||__| | _| `._____||_______||_______/  ")

# Esse programa cria uma lista de tarefas, e adiciona uma nova tarefa ao se digital qualquer frase no prompt
# Ao usar alguma letra ou palavra reservada, executa as ações determinadas.
# Ao usar quit ou save, ele cria uma nova chave criptográfica e guarda o arquivo de tarefas criptografado
# Ao iniciar o programa, tenta carregar uma chave do arquivo, e se der certo tenta descriptografar e carregar as tarefas

from cryptography.fernet import Fernet

print("ToDo v2.0  ",end="")

# mensagens padrão
edit_message = "Qual tarefa deseja editar? "
task_message = "Tarefa: "
delete_task_message = "Qual tarefa deseja apagar? "
nome_arquivo = 'todolist.bin'
help_message = ("\n_____________HELP\n\n(h)elp:   ajuda\n(l)ist:    mostra todas as tarefas\n"
                  "(d)one/(d)elete:  apaga uma tarefa\n(e)dit:     edita uma tarefa\n"
                  "(s)ave:  save to file\n(clear):  limpa a lista\n"
                  "Quit:    Encerra o programa\nDigitar uma tarefa:  adiciona uma tarefa\n")

tarefas = []

# Lista todas as tarefas com um indice
def list_items():
    # print("_____________ITENS")
    for i, item in enumerate(tarefas, start=1):
        print(f"{i}. {item}")

# Grava as tarefas no disco
def save():
    try:
        # Gerar nova chave criprográfica
        chave = Fernet.generate_key()
        fernet = Fernet(chave)

        # Grava a chave para recuperar o arquivo depois
        with open('key.bin','wb') as arquivo:
            arquivo.write(chave)

        # Grava o arquivo criptografado com a chave gerada acima
        with open(nome_arquivo, 'wb') as arquivo:
            lista_criptografada = fernet.encrypt('\n'.join(tarefas).encode())
            arquivo.write(lista_criptografada)
        print(f"\n_____________SAVED TO {nome_arquivo} NEW KEY {chave}")
    except Exception as e:
        print(f"Erro {e}")

# Carrega as tarefas do disco
def load():
    try:
        # Se existe, le a chave do disco
        with open('key.bin','rb') as arquivo:
            chave = arquivo.read()
            fernet = Fernet(chave)

        # le o arquivo e descriptografa com a chave obtida anteriormente
        with open(nome_arquivo,'rb') as arquivo:
            lista_criptografada = arquivo.read()
            lista_descriptografada = fernet.decrypt(lista_criptografada).decode()
            itens = lista_descriptografada.split('\n')
            for item in itens:
                tarefas.append(item)
            print("Arquivo de tarefas encontrado. Carregando...\n")
        list_items()
    except Exception as e:
        print(f"Erro {e}")

# obtem a entrada do usuario e executa a ação desejada
load()
while True:
    user_prompt = input(task_message)

    match user_prompt.capitalize():

        case 'Help' | '?' | 'H' | '':
            print(help_message)
            print(f"TASKS: ",len(tarefas)," tarefas\n")

        case 'List' | 'L':
            if len(tarefas) > 0:
                list_items()
            else:
                print("A lista de tarefas está vazia")

        case 'Edit' | 'E':
            try:
                print("\n_____________EDIT")
                list_items()
                indice = int(input(edit_message))-1
                tarefas[indice] = input("Nova tarefa: ")
            except Exception as e:
                print(f"Erro {e}")

        case 'Delete' | 'Del' | 'D' | 'Done':
            print("\n_____________DONE_OR_DELETE")
            list_items()
            indice = int(input(delete_task_message))-1
            try:
                print(f"Apagando {tarefas[indice]}\n")
                tarefas.pop(indice)    #del tarefas[indice]
            except Exception as e:
                print(f"Erro: {e}")
            list_items()

        case 'Save' | 'S':
            save()

        case 'Quit' | 'Exit':
            save()
            break

        case 'Clear':
            print("Limpando a lista de tarefas...")
            tarefas.clear() # tarefas = []

        case _:
            # print(f"Tarefa adicionada: {user_prompt}")
            tarefas.append(user_prompt)

# End message