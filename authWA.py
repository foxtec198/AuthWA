from time import sleep as sl, strftime as st # Time
import pyautogui as pg # Automate
from pyperclip import copy # Trad Clipboard
from ctpaperclip import PyClipboardPlus # Image to Clipboard
from pandas import read_sql # Tratamento de Dados
from dataframe_image import export # Export png
from os import system, mkdir, startfile # Systems
from sqlalchemy import create_engine # SQL Server
from datetime import datetime #Tempo Real
import smtplib # Envio de email
import email.message # Montagemd do Email
from win32com import client
from webbrowser import open_new_tab

pg.PAUSE = 1
pg.FAILSAFE = False

def atalho(*args):
    with pg.hold(args[0]):
        pg.press(args[1])

def atalho2(*args):
    with pg.hold(args[0]):
        pg.press(args[1])
        pg.press(args[3])

def cola(txt: str):
    copy(txt)
    atalho('ctrl','v')

def display(x):
    print(st(f'%X - Horario de inicio {x} '))
    sl(1)

def conectar_email(em, pwd):
    global sm, emailFrom
    emailFrom = em
    sm = smtplib.SMTP('smtp.gmail.com', 587)
    sm.starttls()
    try:
        sm.login(emailFrom, pwd)
        ...
    except Exception as e:
        print(e)

def enviar_email(erro, data):
    corpo_email = f"""
    <p>{erro}</p>
    <p>{data}</p>
    """
    
    msg = email.message.Message()
    msg['Subject'] = "Erro no AuthWA" # Assunto 
    msg['From'] = emailFrom #Remetente
    msg['To'] = "guilherme.breve@gpssa.com.br" # Destinatario
    msg.add_header('Content-Type','text/html')
    msg.set_payload(corpo_email)

    sm.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Erro enviado por email, ja iremos tratar o problema ☺')
    sl(3)

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
        # atalho('alt','tab')

    def enviar_msg_web(self, nome, mensagem, img = None):
        # Pesquisa a Conversa
        atalho2('ctrl','alt','k')
        sl(2)
        cola(nome)
        sl(2)
        # Entra na conversa
        pg.press('enter')
        sl(5)

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

    def criar_imagem_SQL(self, consulta, arquivo = 'dist/temp.png'):
        with open('dist/temp.png', 'w') as f:
            f.close()
        try:
            df = read_sql(consulta, self.conn)
            export(df, arquivo)
            return arquivo
        except Exception as erro:
            enviar_email(erro, st('%x - %X'))
            return arquivo

class Parcial:
    def __init__(self, uid, pwd, server, 
                 hora_inicio = 0, hora_final = 23,):

        self.hora_inicio = hora_inicio
        self.hora_final = hora_final

        self.whats = WA()
        self.whats.sql_connection(uid, pwd, server)

    def update(self):
        self.hora = int(st('%H'))
        if self.hora == 24:
            self.hora = 0
        self.now = datetime.now()
        self.day = st('%d')
        self.month = st('%m')
        self.year = st('%Y')
        self.fds = st('%a')

    def definir_inicio(self):
        self.update()
        alternated = 0
        
        if self.hora == 0: alternated = 0
        if self.hora_inicio == self.hora: alternated = self.hora_inicio
        if self.hora < self.hora_inicio: alternated = self.hora_inicio
        if self.hora > self.hora_inicio: alternated = self.hora + 1

        return alternated
    
    def main_loop(self, funcs: list):
        h = self.definir_inicio()
        if type(funcs) == list: 
            while True:
                self.update()
                if h == 24: h = 0
                for f in funcs:
                    if type(f) == dict:
                        sl(1)
                        he = st('%X')
                        for item in f:
                            horario = item
                            func = f[horario]
                            if he == horario:
                                try:
                                    atalho('alt','tab')
                                    func()
                                    atalho('alt','tab')
                                except Exception as erro: 
                                    enviar_email(erro, st('%x - %X'))
                    if self.hora == h:
                        if type(f) == list and self.fds == 'Sat' or self.fds == 'Sun':
                            try:
                                atalho('alt','tab')
                                for i in f:
                                    i()
                                h += 1
                                atalho('alt','tab')
                            except Exception as erro: enviar_email(erro, st('%x - %X'))
                        if type(f) == tuple and self.fds != 'Sat' and self.fds != 'Sun':
                            try:
                                atalho('alt','tab')
                                for i in f:
                                    i()
                                h += 1
                                atalho('alt','tab')
                            except Exception as erro: enviar_email(erro, st('%x - %X'))
                    display(h)
        else: return 'Isto não é uma lista'

conectar_email('foxtec198@gmail.com','vewmksduxchpjirg')