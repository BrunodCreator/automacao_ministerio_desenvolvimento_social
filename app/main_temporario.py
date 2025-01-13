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


global primeira_execucao


#captura os valores do menu
valores_menu = menu_de_selecao()

#extrai os valores retornados
nome_da_planilha = valores_menu['nome_da_planilha']
mes_elemento_selecionado = valores_menu['mes']
ano_elemento_selecionado = valores_menu['ano']
primeira_execucao = valores_menu['primeira_execucao']


teste(nome_da_planilha, converter_mes(mes_elemento_selecionado), ano_elemento_selecionado,primeira_execucao)

