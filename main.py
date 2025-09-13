import os
from dotenv import load_dotenv
import time
import sys
from pathlib import Path
from datetime import datetime

load_dotenv()

CAMINHO_ORIGEM = Path(os.getenv('CAMINHO_ORIGEM'))
CAMINHO_SAIDA = Path(os.getenv('CAMINHO_SAIDA'))

os.makedirs(CAMINHO_SAIDA, exist_ok=True)

arquivos = [
    arquivo.replace('.f137.mp4', '')
    for arquivo in os.listdir(CAMINHO_ORIGEM)
    if arquivo[-4:] == '.mp4'
]

data = datetime.now().strftime("%d-%m-%y")

# print(arquivos)

# for i in os.listdir(CAMINHO_ORIGEM):
#     print(i)

# print('ola mundo.mp4'[-4:])

for indice, arquivo in enumerate(arquivos):
    if indice == 0:
        with open(os.path.join(CAMINHO_SAIDA, f'log-{data}.txt'), 'a', encoding='utf8') as arquivo_log:
            arquivo_log.write(f'Iniciando conversão {datetime.now().strftime("%H:%M:%S")}'+'='*50+'\n\n')

    print('Iniciando checagem do', arquivo+'...')

    if os.path.exists(os.path.join(CAMINHO_SAIDA, arquivo+'.mp4')):
        print(f'Arquivo {arquivo}.mp4 já existe, pulando para o próximo!')

        with open(os.path.join(CAMINHO_SAIDA, f'log-{data}.txt'), 'a', encoding='utf8') as arquivo_log:
            arquivo_log.write(f'{arquivo}.mp4 já existe na pasta, pulou para o próximo! \n')
            arquivo_log.write('-'*80+'\n')
    
    else:
        print('iniciando conversao', arquivo+'...')

    if indice == len(arquivos)-1:
        with open(os.path.join(CAMINHO_SAIDA, f'log-{data}.txt'), 'a', encoding='utf8') as arquivo_log:
            arquivo_log.write('\n')

    # os.system(f'ffmpeg -i {os.path.join(CAMINHO_ORIGEM, arquivo+".f136.mp4")} -i {os.path.join(CAMINHO_ORIGEM, arquivo+".f251.webm")} -c copy \
    #            {os.path.join(CAMINHO_SAIDA, arquivo+".mp4")}')

    # print(os.path.join(CAMINHO_SAIDA, arquivo+".mp4"))
    
#     os.system(f'ffmpeg -i "'+os.path.join(CAMINHO_ORIGEM, arquivo+".f137.mp4")+'" -i "'+os.path.join(CAMINHO_ORIGEM, arquivo+".f251.webm")+ \
# '" -c:v copy -c:a aac -b:a 192k "'+os.path.join(CAMINHO_SAIDA, arquivo+".mp4")+'"')
    
#     time.sleep(30)

# for i in arquivos:
#     print(i, ' : ', os.path.exists(os.path.join(CAMINHO_ORIGEM, i+'.f137.mp4')))