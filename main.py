import os
from dotenv import load_dotenv
import time
import sys
from pathlib import Path

load_dotenv()

CAMINHO_ORIGEM = Path(os.getenv('CAMINHO_ORIGEM'))
CAMINHO_SAIDA = Path(os.getenv('CAMINHO_SAIDA'))

os.makedirs(CAMINHO_SAIDA, exist_ok=True)

arquivos = [
    arquivo.replace('.f137.mp4', '')
    for arquivo in os.listdir(CAMINHO_ORIGEM)
    if arquivo[-4:] == '.mp4'
]

print(arquivos)

sys.exit()

# for i in os.listdir(CAMINHO_ORIGEM):
#     print(i)

# print('ola mundo.mp4'[-4:])

for item in arquivos:
    print('iniciando conversao', item+'...')

    # os.system(f'ffmpeg -i {os.path.join(CAMINHO_ORIGEM, item+".f136.mp4")} -i {os.path.join(CAMINHO_ORIGEM, item+".f251.webm")} -c copy \
    #            {os.path.join(CAMINHO_SAIDA, item+".mp4")}')

    # print(os.path.join(CAMINHO_SAIDA, item+".mp4"))
    
    os.system(f'ffmpeg -i "'+os.path.join(CAMINHO_ORIGEM, item+".f137.mp4")+'" -i "'+os.path.join(CAMINHO_ORIGEM, item+".f251.webm")+ \
'" -c:v copy -c:a aac -b:a 192k "'+os.path.join(CAMINHO_SAIDA, item+".mp4")+'"')
    
    time.sleep(30)

# for i in arquivos:
#     print(i, ' : ', os.path.exists(os.path.join(CAMINHO_ORIGEM, i+'.f137.mp4')))