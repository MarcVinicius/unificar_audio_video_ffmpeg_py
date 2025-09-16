import os
from dotenv import load_dotenv
import time
from pathlib import Path
from datetime import datetime

load_dotenv()

CAMINHO_ORIGEM = Path(os.getenv('CAMINHO_ORIGEM'))
CAMINHO_SAIDA = Path(os.getenv('CAMINHO_SAIDA'))

os.makedirs(CAMINHO_SAIDA, exist_ok=True)

def hora_atual() -> str:
    return datetime.now().strftime("%H:%M:%S")

def caminho_log() -> str:
    data = datetime.now().strftime("%d-%m-%y")

    caminho = os.path.join(CAMINHO_SAIDA, f'log-{data}.txt')

    return caminho

def retorna_extensao(arquivo: str, qtd_extensao: int) -> str:
    # qtd_extensao 1 = apenas a ultima extensao ex: .mp4
    # qtd_extensao 2 = ultima e penultima ex: .f136.mp4
    if '.' in arquivo:
        arquivo_dividido = arquivo.split('.')

        extensao = '.'+arquivo_dividido[-1]

        if len(arquivo_dividido) > 2:
            extensao_extensao = '.'+arquivo_dividido[-2]+extensao

        else:
            extensao_extensao = None

        if qtd_extensao == 1:
            return extensao

        return extensao_extensao
    
    return None


arquivos = [
    arquivo.replace(retorna_extensao(arquivo, 2), '')
    for arquivo in os.listdir(CAMINHO_ORIGEM)
    if arquivo[-4:] == '.mp4'
]

for indice, arquivo in enumerate(arquivos):
    if indice == 0:
        with open(caminho_log(), 'a', encoding='utf8') as arquivo_log:
            arquivo_log.write(f'Iniciando conversão {hora_atual()}'+'='*50+'\n\n')

    print('Iniciando checagem do', arquivo+'...')

    if os.path.exists(os.path.join(CAMINHO_SAIDA, arquivo+'.mp4')):
        print(f'<Arquivo {arquivo}.mp4> já existe, pulando para o próximo!')

        with open(caminho_log(), 'a', encoding='utf8') as arquivo_log:
            arquivo_log.write(f'[{hora_atual()}] <{arquivo}.mp4> já existe na pasta, pulou para o próximo! \n')
            arquivo_log.write('-'*80+'\n')
    
    else:
        print(f'iniciando conversao <{arquivo}>...')

        try:
            os.system(f'ffmpeg -i "'+os.path.join(CAMINHO_ORIGEM, arquivo+".f136.mp4")+'" -i "'+os.path.join(CAMINHO_ORIGEM, arquivo+".f251.webm")+ \
            '" -c:v copy -c:a aac -b:a 192k "'+os.path.join(CAMINHO_SAIDA, arquivo+".mp4")+'"')

            texto_log = f'[{hora_atual()}] gerando <{arquivo}.mp4>\n'

            tempo = 30
        
        except Exception as erro:
            texto_log = erro
            tempo = 0

        with open(caminho_log(), 'a', encoding='utf8') as arquivo_log:
            arquivo_log.write(texto_log)
            arquivo_log.write('_'*80+'\n')

        time.sleep(tempo)

    if indice == len(arquivos)-1:
        with open(caminho_log(), 'a', encoding='utf8') as arquivo_log:
            arquivo_log.write('\n')

    # os.system(f'ffmpeg -i {os.path.join(CAMINHO_ORIGEM, arquivo+".f136.mp4")} -i {os.path.join(CAMINHO_ORIGEM, arquivo+".f251.webm")} -c copy \
    #            {os.path.join(CAMINHO_SAIDA, arquivo+".mp4")}')

    # print(os.path.join(CAMINHO_SAIDA, arquivo+".mp4"))
    
#     os.system(f'ffmpeg -i "'+os.path.join(CAMINHO_ORIGEM, arquivo+".f137.mp4")+'" -i "'+os.path.join(CAMINHO_ORIGEM, arquivo+".f251.webm")+ \
# '" -c:v copy -c:a aac -b:a 192k "'+os.path.join(CAMINHO_SAIDA, arquivo+".mp4")+'"')

# for i in arquivos:
#     print(i, ' : ', os.path.exists(os.path.join(CAMINHO_ORIGEM, i+'.f137.mp4')))