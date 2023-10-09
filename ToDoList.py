from cryptography.fernet import Fernet

#  ██████   █████  ███████ ███████ ████████  █████   ██████
# ██       ██   ██    ███  ██         ██    ██   ██ ██    ██
# ██   ███ ███████   ███   ███████    ██    ███████ ██    ██
# ██    ██ ██   ██  ███         ██    ██    ██   ██ ██    ██
#  ██████  ██   ██ ███████ ███████    ██    ██   ██  ██████

print(" █████  ███████  █████  ███████ ███████ ██ ██████  ███████ ███████ ")
print("██   ██ ██      ██   ██    ███  ██      ██ ██   ██ ██      ██      ")
print("███████ █████   ███████   ███   █████   ██ ██████  █████   ███████ ")
print("██   ██ ██      ██   ██  ███    ██      ██ ██   ██ ██           ██ ")
print("██   ██ ██      ██   ██ ███████ ███████ ██ ██   ██ ███████ ███████ ")

# Esse programa cria uma lista de tarefas, e adiciona uma nova tarefa ao se digital qualquer frase no prompt
# Ao usar alguma letra ou palavra reservada, executa as ações determinadas.
# Ao usar quit ou save, ele cria uma nova chave criptográfica e guarda o arquivo de tarefas criptografado
# Ao iniciar o programa, tenta carregar uma chave do arquivo, e se der certo tenta descriptografar e carregar as tarefas


print("ToDo v2.0  ", end="")

help_message = ("\n_____________HELP\n\n(h)elp:   ajuda\n(l)ist:    mostra todas as tarefas\n"
                "(d)one/(d)elete:  apaga uma tarefa\n(e)dit:     edita uma tarefa\n"
                "(s)ave:  save to file\n(clear):  limpa a lista\n"
                "Quit:    Encerra o programa\nDigitar uma tarefa:  adiciona uma tarefa\n")


# Lista todas as tarefas com um indice
def list_items(_tarefas):
    """Exibe uma lista no formato í-item"""
    # print("_____________ITENS")
    for i, item in enumerate(_tarefas, start=1):
        print(f"{i}. {item}")


# Grava as tarefas no disco
def save(_tarefas, nome_arquivo='todolist.bin'):
    """Recebe uma lista de tarefas e um nome de arquivo, e grava de modo criptografado a chave e o arquivo"""
    try:
        # Gerar nova chave criprográfica
        chave = Fernet.generate_key()
        fernet = Fernet(chave)

        nome_chave = f"{nome_arquivo}.key"
        # Grava a chave para recuperar o arquivo depois
        with open(nome_chave, 'wb') as arquivo:
            arquivo.write(chave)

        # Grava o arquivo criptografado com a chave gerada acima
        with open(nome_arquivo, 'wb') as arquivo:
            lista_criptografada = fernet.encrypt('\n'.join(_tarefas).encode())
            arquivo.write(lista_criptografada)
        print(f"\n_____________SAVED TO {nome_arquivo} NEW KEY {chave}")
    except Exception as _e:
        print(f"Erro {_e}")


# Carrega as tarefas do disco
def load(nome_arquivo='todolist.bin'):
    _tarefas = []
    nome_chave = f"{nome_arquivo}.key"
    try:
        # Se existe, le a chave do disco
        with open(nome_chave, 'rb') as arquivo:
            chave = arquivo.read()
            fernet = Fernet(chave)

        # le o arquivo e descriptografa com a chave obtida anteriormente
        with open(nome_arquivo, 'rb') as arquivo:
            lista_criptografada = arquivo.read()
            lista_descriptografada = fernet.decrypt(lista_criptografada).decode()
            itens = lista_descriptografada.split('\n')
            for item in itens:
                _tarefas.append(item)
            print("Arquivo de tarefas encontrado. Carregando...\n")
        list_items(_tarefas)
    except FileNotFoundError:
        print(f"Arquivo não encontrado. Será criado novo arquivo de chave com o nome {nome_chave}")
    except Exception as _e:
        print(f"Erro {_e}\n")
    return _tarefas


# tenta carregar as tarefas do arquivo padrão
tarefas = load()

# Repete o loop de entrada do usuário
while True:
    user_prompt = input("Tarefa: ")

    # Compara com o texto capitalizado (primeira maiuscula)
    match user_prompt.capitalize():

        case 'Help' | '?' | 'H' | '':
            print(help_message)
            print(f"TASKS: ", len(tarefas), " tarefas\n")

        case 'List' | 'L':
            if len(tarefas) > 0:
                list_items(tarefas)
            else:
                print("A lista de tarefas está vazia")

        case 'Edit' | 'E':
            try:
                print("\n_____________EDIT")
                list_items(tarefas)
                indice = int(input("Qual tarefa deseja editar? "))-1
                tarefas[indice] = input("Nova tarefa: ")
            except Exception as e:
                print(f"Erro {e}")

        case 'Delete' | 'Del' | 'D' | 'Done':
            print("\n_____________DONE_OR_DELETE")
            list_items(tarefas)
            try:
                indice = int(input("Qual tarefa deseja apagar? ")) - 1
                print(f"Apagando {tarefas[indice]}\n")
                # del tarefas[indice]
                tarefas.pop(indice)
            except Exception as e:
                print(f"Erro: {e}")
            list_items(tarefas)

        case 'Save' | 'S':
            save(tarefas)

        case 'Quit' | 'Exit':
            save(tarefas)
            break

        case 'Clear':
            print("Limpando a lista de tarefas...")
            # tarefas = []
            tarefas.clear()

        case _:
            # print(f"Tarefa adicionada: {user_prompt}")
            tarefas.append(user_prompt)
