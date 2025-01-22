import openpyxl
import os
from menu.menu_de_selecao import  menu_de_selecao, converter_mes
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from func.func_main import func_main
from logs import func_logs_api
from datetime import datetime

m_cliente = 'RPA_IEL'
nome_processo = 'Criando UUID da Execução'
nome_robo = 'ESTRELINHA'
data_hora_inicio_robo = None
data_hora_fim_robo = None
categoria = 'INFO'
numero_point = 0
data_hora_inicio_point = None
data_hora_fim_point = None
status_point = 'Concluido'
status_execucao = 'EM_ANDAMENTO'
msg_erro = ''
m_execucao = ''



# Chamada da primeira execução
data_hora_inicio_robo,data_hora_inicio_point,data_hora_fim_point, m_execucao = func_logs_api.primeira_execucao(
    cliente=m_cliente,
    nomeProcesso= nome_processo,
    nomeRobo= nome_robo,
    dataHoraInicioRobo=data_hora_inicio_robo,
    categoria=categoria,
    numeroPoint=numero_point,
    dataHoraInicioPoint=data_hora_inicio_point,
    dataHoraFimPoint=data_hora_fim_point,
    statusPoint=status_point,
    statusExecucao=status_execucao,
    msgErro=msg_erro,
    execucao=m_execucao
    
)

print('UUID: ', m_execucao)


data_hora_inicio_point = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# print('UUID 2: ', m_execucao)

#captura os valores do menu
valores_menu = menu_de_selecao()

data_hora_fim_point= func_logs_api.exec_fim_point(
    cliente=m_cliente,
    nomeProcesso= 'fechano_menu_teste_NOVIDADE3',
    nomeRobo= nome_robo,
    dataHoraInicioRobo=data_hora_inicio_robo,
    dataHoraInicioPoint=data_hora_inicio_point,
    dataHoraFimPoint=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    numeroPoint=1,
    categoria=categoria,
    statusExecucao=status_execucao,
    msgErro=msg_erro,
    statusPoint=status_point,
    execucao=m_execucao
)
print(f'{data_hora_inicio_point} {data_hora_fim_point}')
print('UUID 3: ', m_execucao)

#extrai os valores retornados do menu de seleção
nome_da_planilha = valores_menu['nome_da_planilha']
mes_elemento_selecionado = valores_menu['mes']
ano_elemento_selecionado = valores_menu['ano']
primeira_execucao = valores_menu['primeira_execucao']


func_main(nome_da_planilha, converter_mes(mes_elemento_selecionado), ano_elemento_selecionado,primeira_execucao)

data_hora_fim_robo = func_logs_api.exec_fim_robo(
    cliente=m_cliente,
    nomeProcesso= 'FIM_ROBO_NOVIDADE3',
    nomeRobo= nome_robo,
    dataHoraInicioRobo=data_hora_inicio_robo,
    dataHoraInicioPoint=data_hora_inicio_point,
    dataHoraFimPoint=data_hora_fim_point,
    dataHoraFimRobo=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    numeroPoint=2,
    categoria=categoria,
    statusExecucao='SUCESSO',
    msgErro=msg_erro,
    statusPoint='Sucesso',
    execucao=m_execucao
)

print(data_hora_fim_robo)
print('UUID 4: ', m_execucao)
