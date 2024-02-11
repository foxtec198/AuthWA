from time import sleep as sl, strftime as st # Time
import pyautogui as pg # Automate
from pyperclip import copy # Trad Clipboard
from ctpaperclip import PyClipboardPlus # Image to Clipboard
from pandas import read_sql # Tratamento de Dados
from dataframe_image import export # Export png
from os import system, mkdir # Systems
from sqlalchemy import create_engine # SQL Server
from datetime import datetime
import sys

def atalho(*args):
    with pg.hold(args[0]):
        pg.press(args[1])

def cola(txt: str):
    copy(txt)
    atalho('ctrl','v')

def display(x):
    print(st(f'%X - Horario de inicio {x} '))
    sl(1)
    system('cls')

class WA:
    def __init__(self):
        try: mkdir('dist/')
        except: ...
        self.pc = PyClipboardPlus()

    def sql_connection(self, uid, pwd, server, 
            database = 'Vista_Replication_PRD', 
            driver = 'SQL Server'):
            
        self.engine = create_engine(f'mssql://{uid}:{pwd}@{server}/{database}?driver={driver}')
        try:
            self.conn = self.engine.connect()
            return 'Conexão realizada com sucesso'
        except: return "Conexão Invalida"
        
    def enviar_msg(self, nome, mensagem, img = None):
        # Entra no Whats
        atalho('alt','tab')
        sl(1)
        # Pesquisa a Conversa
        atalho('ctrl','f')
        sl(2)
        cola(nome)
        sl(2)
        # Entra na conversa
        atalho('ctrl','1')
        sl(7)

        if img: # Caso tenha Imagem
            self.pc.write_image_to_clipboard(img)
            atalho('ctrl','v')
            sl(5)
            cola(mensagem)
            sl(1)
            pg.press('enter')
            pg.press('esc')
        else: # Caso não tenha Imagem
            cola(mensagem)
            pg.press('enter')
            pg.press('esc')

        atalho('ctrl','f')
        atalho('ctrl','a')
        pg.press('backspace')
        atalho('alt','tab')

    def criar_imagem_SQL(self, consulta, arquivo = 'dist/temp.png'):
        try:
            df = read_sql(consulta, self.conn)
            export(df, arquivo)
            return arquivo
        except: return 'Imagem não criada'

class Parcial:
    def __init__(self, uid, pwd, server, 
                 hora_inicio = 8, hora_final = 18,):

        self.hora_inicio = hora_inicio
        self.hora_final = hora_final

        self.whats = WA()
        login = self.whats.sql_connection(uid, pwd, server)
        if not login: sys.exit('Login SQL não realizado, verifique as credenciais... ')
    def update(self):
        self.hora = int(st('%H'))
        self.now = datetime.now()
        self.day = st('%d')
        self.month = st('%m')
        self.year = st('%Y')

    def definir_inicio(self):
        self.update()
        alternated = 0
        if self.hora_inicio == self.hora:
            alternated = self.hora_inicio
        elif self.hora > self.hora_inicio:
            alternated = self.hora + 1
        elif self.hora < self.hora_inicio:
            alternated = self.hora_inicio
        return alternated
    
    def main_loop(self, funcs: list):
        h = self.definir_inicio()
        while True:
            fds = st('%a')
            self.update()
            for f in funcs:
                if self.hora == h:
                    if type(f) == list and fds == 'Sat' or fds == 'Sun':
                        for i in f:
                            i()
                        h += 1
                    elif type(f) != list and fds != 'Sat' and fds != 'Sun':
                        f()
                        h += 1
                elif type(f) == dict:
                    he = st('%X')
                    for item in f:
                        horario = item
                        func = f[item]
                        if he >= f'{horario}:00' and he <= f'{horario}:01':
                            func()
                elif self.hora == self.hora_final: h = self.hora_inicio
                display(h)