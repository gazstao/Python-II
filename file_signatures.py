# File signature magic bytes
# Gazstao 19 OCT 23

import pathlib
import keyboard

def testa_dir(_path):

    for child in pathlib.Path(_path).glob("*"):
        try:
            if child.is_file():
                print(testa_arquivo(child))
            elif child.is_dir():
                testa_dir(child)
        except Exception as e:
            print(f'Erro {e} no arquivo {child}')


def testa_arquivo(file_path):

    if (keyboard.is_pressed("enter") | keyboard.is_pressed(" ")):
        exit(0)

    try:
        print(f"[*] testa_arquivo {file_path}: ", end="")
        # Defina as assinaturas de arquivo para os tipos que você deseja identificar
        file_signatures = {
            b'GIF89a': 'GIF',  # Exemplo de assinatura para arquivos GIF
            b'%PDF': 'PDF',   # Exemplo de assinatura para arquivos PDF
            b'\x89PNG\r': 'PNG',
            b'PK\x03\x04': 'ZIP',
            b'\xFF\xFB': 'MP3',
            b'{\n': 'JSON',
            b'IRPF ':'IRPF',
            b'<?xml':'XML',
            b'<!DOC':'HTML',
            b'MZ\x90\x00\x03':'EXE',
            b'{\\rtf':'RTF',
            b'\x00\x01\x00\x00\x00':'TTF'
            # Adicione outras assinaturas conforme necessário
        }

        # Leitura dos primeiros bytes do arquivo
        with open(file_path, 'rb') as file:
            file_header = file.read(5)  # Leitura dos primeiros 5 bytes

        # Verifique se as assinaturas correspondem
        for signature, file_type in file_signatures.items():
            if file_header.startswith(signature):
                return file_type
        string = 'Desconhecido: '+str(file_header)
        return string
    except Exception as e:
        print(f"Erro {e}")

testa_dir('c:')


