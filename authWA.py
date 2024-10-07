from time import sleep as sl, strftime as st # Time
import pyautogui as pg # Automate
from pyperclip import copy # Trad Clipboard
from ctpaperclip import PyClipboardPlus # Image to Clipboard
from pandas import read_sql, read_sql_query # Tratamento de Dados
from dataframe_image import export # Export png
from os import system, mkdir # Systems
from sqlalchemy import create_engine # SQL Server
from urllib.parse import quote_plus 
from datetime import datetime #Tempo Real
import smtplib # Envio de email
import email.message # Montagemd do Email
import logging # Logs
from PIL import Image # Pillage

pg.PAUSE = .5
pg.FAILSAFE = False
try: mkdir('logs')
except: ...
logging.basicConfig(filename='logs/error_logs.log', filemode='a', level=logging.ERROR, format="Horario do erro: %(asctime)s - %(levelname)s, Aqruivo: %(filename)s, Mensagem:%(message)s")
logger = logging.getLogger('root')

def atalho(*args):
    with pg.hold(args[0]):
        pg.press(args[1])
    sl(1)

def atalho2(*args):
    with pg.hold(args[0]):
        pg.press(args[1])
        pg.press(args[3])

def cola(txt: str):
    copy(txt)
    atalho('ctrl','v')

def dsp(x):
    print(st(f'Horario de inicio {x} - %x - %X'))
    sl(1)
    system('cls')
    
def conectar_email(em, pwd):
    global sm, emailFrom
    emailFrom = em
    sm = smtplib.SMTP('smtp.gmail.com', 587)
    sm.starttls()
    try:
        sm.login(emailFrom, pwd)
    except Exception as e:
        logger.error(e)
        print(f'Erro de Login - Email: {e}')

def enviar_erro(erro, data):
    corpo_email = f"""
    <body style="background-color: black; color: white; font-family: Arial, Helvetica, sans-serif">
        <div style="display: flex; justify-content: center; justify-items: center;align-items: center;">
            <div>
                <img src='https://portalprod.gpsvista.com.br/assets/media/logos/Gpslogo.svg' style="width: 200px;"/>
            </div>
        </div>
        <div style="margin-left: 30px;">
            <h1>Log de Erros</h1>
            <p>O <b> Parcial(AuthWA) </b> obteve um erro na data {data}</p>
            <p>{erro}</p>
        </div>
        <div style="margin-top: 300px; margin-left: 50px; margin-bottom: 50px; display: flex;">
            <img src="https://avatars.githubusercontent.com/u/64221923?v=4" alt="foto" style="border-radius: 50%; width: 200px;"/>
            <div style="font-family: 'Courier New', Courier, monospace; margin-left: 30px; margin-top: 30px;">
                <p style="margin-bottom: -10;">Att</p>
                <p style="margin-bottom: -10;">Guilherme Breve</p>
                <p style="margin-bottom: -10;">Analista de Projetos</p>
                <p style="color: gray; margin-bottom: -10;"><i>+55 439966617904</i></p>
            </div>
        </div>
    </body>
    """
    
    conectar_email('foxtec198@gmail.com', 'fwmeylchtupgrmeb')
    msg = email.message.Message()
    msg['Subject'] = "Erro no AuthWA" # Assunto 
    msg['From'] = emailFrom #Remetente
    msg['To'] = "guilherme.breve@gpssa.com.br" # Destinatario
    msg.add_header('Content-Type','text/html')
    msg.set_payload(corpo_email)

    sm.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Erro enviado por email, ja iremos tratar o problema ☺')

def enviar_email(erro):
    data = st('%x - %X')
    try:
        enviar_erro(str(erro), data)
        logger.error(erro)
    except Exception as e:
        logger.error(erro)
        print(f'Erro ao enviar email: {e}')

class WA:
    def __init__(self):
        self.pc = PyClipboardPlus()
        self.conn = None
        try: mkdir('dist/')
        except: ...

    def sql_connection(self, uid, pwd, server, database='Vista_Replication_PRD', driver='ODBC Driver 18 for SQL Server'):
        self.uid = quote_plus(uid)
        self.pwd = quote_plus(pwd)
        self.server = quote_plus(server)
        self.database = quote_plus(database)
        driver = quote_plus(driver)
        url = f'mssql://{self.uid}:{self.pwd}@{self.server}/{self.database}?driver={driver}&&TrustServerCertificate=yes'
        engine = create_engine(url)
        return engine

    def enviar_msg(self, nome, mensagem, img = None):
        # Pesquisa a Conversa
        sl(3)
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

    def enviar_msg_old(self, nome, mensagem, img = None):
        # Pesquisa a Conversa
        sl(3)
        atalho('ctrl','f')
        sl(2)
        cola(nome)
        sl(2)
        # Entra na conversa
        atalho('ctrl','1')
        sl(7)

        if img: # Caso tenha Imagem
            system(f'explorer {img}')
            sl(5)
            atalho('ctrl','c')
            sl(5)
            atalho('ctrl','w')
            sl(5)
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
        df = read_sql_query(consulta, self.connSQl)
        export(df, filename=arquivo, max_cols=-1, max_rows=-1)
        return arquivo

    def criar_imagem_SQL_GGPS(self, consulta, arquivo = 'dist/temp.png', escalonadas=None):
        if self.conn:
            df = read_sql_query(consulta, self.conn)
            if df.empty and escalonadas: return 'src/zeradas.png'
            export(df, filename=arquivo, max_cols=-1, max_rows=-1, table_conversion="matplotlib")
            dt = Image.open(arquivo)
            logo = Image.open('src/GPS.png')
            hm = dt.size[1] + logo.size[1] 
            wm = dt.size[0]
            modelo = Image.new('RGBA', (wm, hm), color='#DFDFDF')
            mid = int(modelo.width/2) - int(logo.width/2)
            modelo.paste(logo, (mid, 0), logo)
            modelo.paste(dt, (0, logo.height + 1))
            modelo.save(arquivo)
            return arquivo
    
class Parcial:
    def __init__(self, uid, pwd, server, db, hora_inicio = 0, hora_final = 23,):
        self.hora_inicio = hora_inicio
        self.hora_final = hora_final
        self.whats = WA()
        self.uid = uid
        self.pwd = pwd
        self.server = server
        self.engine = self.whats.sql_connection(uid, pwd, server)
        self.db = db

    def update(self):
        self.now = datetime.now().strftime('%d/%m/%Y %H:%M')
        self.date = datetime.date(datetime.today())
        self.time = datetime.time(datetime.today())
        self.hora = int(st('%H'))
        self.day = st('%d')
        self.month = st('%m')
        self.year = st('%Y')
        self.fds = st('%a')
        if self.hora == 24: self.hora = 0

    def definir_inicio(self):
        self.update()
        alternated = 0
        if self.hora == 0: alternated = 1
        if self.hora == 23: alternated = 0
        if self.hora_inicio == self.hora: alternated = self.hora_inicio
        if self.hora < self.hora_inicio: alternated = self.hora_inicio
        if self.hora > self.hora_inicio: alternated = self.hora + 1

        return alternated
    
    def main_loop(self, funcs: list):
        h = self.definir_inicio()
        while True:
            self.update()
            for f in funcs:
                if type(f) == list:
                    if self.fds == 'Sat' or self.fds == 'Sun':
                        if self.hora == h:
                            try:
                                atalho('alt','tab')
                                with self.engine.connect() as conn:
                                    self.whats.conn = conn
                                    for i in f: i()
                                atalho('alt','tab')
                                h += 1
                            except Exception as erro: enviar_email(str(erro))
                if type(f) == tuple:
                    if self.fds != 'Sat' and self.fds != 'Sun':
                        if self.hora == h:
                            try:
                                atalho('alt','tab')
                                with self.engine.connect() as conn:
                                    self.whats.conn = conn
                                    for i in f: i()
                                atalho('alt','tab')
                                h += 1
                            except Exception as erro: enviar_email(str(erro))
                if self.hora == self.hora_final: h = self.hora_inicio
            dsp(h)

if __name__ == '__main__':
    p = Parcial('guilherme.breve','Gtaiv@130520','10.56.6.56','Vista_Replication_PRD')
    dds = (
        lambda: print('Inicio'),
        lambda: p.whats.enviar_msg(
            'Guilherme',
            'Teste de Atualização',
            p.whats.criar_imagem_SQL_GGPS('select top 1 nome from tarefa')
        )
    )
    main = []
    main.append(dds)
    p.main_loop(main)