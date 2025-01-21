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
from func.func_main import teste
from logs import func_logs_api

Cliente = 'RPA_IEL'
nome_processo = 'HAHAHAHAHAHHAHAHAHAHHAHAHAHHAHAAHHAHAHAHAHAHAHAHHAHAHAHAHAHAHHAAHAHA'
nome_robo = 'ESTRELINHA'
data_hora_inicio_robo = None
data_hora_fim_robo = None
categoria = 'INFO'
numero_point = 0
data_hora_inicio_point = None
data_hora_fim_point = None
status_point = 'AHAHHAAAAAAAAAAHAHAHHAHAHAHHAAHHAHAHAHAHHA'
status_execucao = 'EM_ANDAMENTO'
msg_erro = ''
execucao = ''



# Chamada da primeira execução
func_logs_api.primeira_execucao(
    cliente=Cliente,
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
    execucao=execucao
    
)



#captura os valores do menu
valores_menu = menu_de_selecao()

#extrai os valores retornados
nome_da_planilha = valores_menu['nome_da_planilha']
mes_elemento_selecionado = valores_menu['mes']
ano_elemento_selecionado = valores_menu['ano']
primeira_execucao = valores_menu['primeira_execucao']


teste(nome_da_planilha, converter_mes(mes_elemento_selecionado), ano_elemento_selecionado,primeira_execucao)

