from func_main import navegador, selecionar_elementos, selecionar_valores_elementos, webdriver, WebDriverWait, EC, By, Select, click_pesquisar
from time import sleep
import openpyxl
import os
from menu.menu_de_selecao import  menu_de_selecao

#captura os valores do menu
valores_menu = menu_de_selecao()

#extrai os valores retornados
nome_da_planilha = valores_menu['nome_da_planilha']
ano_elemento_selecionado = valores_menu['ano']
mes_elemento_selecionado = valores_menu['mes']


menu_de_selecao()
