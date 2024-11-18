from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl
import os


# Configuração do WebDriver
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)

# Configura o caminho para salvar o arquivo na área de trabalho do usuário
caminho_area_de_trabalho = os.path.join(os.path.expanduser("~"), "Desktop", "Dados_Municipios.xlsx")

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Saldo dos Municípios"

sheet['A1'] = 'MUNICIPIO'
sheet['B1'] = 'SALDO'
sheet['C1'] = 'STATUS'

linha_excel = 2

# Acessa a página
url = ('https://aplicacoes.mds.gov.br/suaswebcons/restrito/execute.jsf?b=*tbmepQbsdfmbtQbhbtNC&event=*fyjcjs')
navegador.get(url)

# Preenche os campos que ativam o dropdown de município

ano = Select(navegador.find_element(By.XPATH, '//*[@id="form:ano"]'))
mes = Select(navegador.find_element(By.XPATH, '//*[@id="form:mes"]'))
esf_adm = Select(navegador.find_element(By.XPATH, '//*[@id="form:esferaAdministrativa"]'))
uf = Select(navegador.find_element(By.XPATH, '//*[@id="form:uf"]'))


# Define os valores necessários para ativar o campo de município
def selecionar_valores_elementos():
    mes.select_by_value('10')
    sleep(1)
    uf.select_by_visible_text('GO')
    sleep(1)
    ano.select_by_visible_text('2024')
    sleep(1)
    esf_adm.select_by_visible_text('MUNICIPAL')
    sleep(1)

selecionar_valores_elementos()

# Aguarda o campo 'municipio' ser ativado (não estar mais 'disabled')
municipio_dropdown = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#form\\:municipio"))
)
municipio = Select(municipio_dropdown)

municipios_valores = [option.get_attribute("value") for option in municipio.options if option.get_attribute("value")]

# municipio.select_by_visible_text('ABADIANIA')
# sleep(1)
for valor in municipios_valores:
    sleep(5)
    try:
        ano = Select(navegador.find_element(By.XPATH, '//*[@id="form:ano"]'))
        mes = Select(navegador.find_element(By.XPATH, '//*[@id="form:mes"]'))
        esf_adm = Select(navegador.find_element(By.XPATH, '//*[@id="form:esferaAdministrativa"]'))
        uf = Select(navegador.find_element(By.XPATH, '//*[@id="form:uf"]'))
        selecionar_valores_elementos()

        # Aguarda o campo 'municipio' ser ativado novamente
        municipio_dropdown = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#form\\:municipio")))
        municipio = Select(municipio_dropdown)
        municipio.select_by_value(valor)
        sleep(2)
        texto_visivel = municipio.first_selected_option.text

        # Clica no botão de pesquisa
        botao_pesquisar = navegador.find_element(By.ID, "form:pesquisar")
        botao_pesquisar.click()
        sleep(20)

        try:
            # Localiza o segundo <td> dentro da estrutura <td> -> <table> -> <tbody> -> <tr> -> <td>
            valor_elemento = navegador.find_element(By.XPATH, 
                '//td[@class="tdParNum"]/table/tbody/tr/td[2]/span')
            
            # Extrai o texto visível do elemento
            valor_texto = valor_elemento.text.strip()
            print(f"Valor extraído de {texto_visivel} é {valor_texto}")
            sheet[f'A{linha_excel}'] = texto_visivel
            sheet[f'B{linha_excel}'] = valor_texto
            sheet[F'C{linha_excel}'] = 'CONCLUIDO'
            linha_excel += 1



        except Exception as e:
            print(f"Erro ao extrair o valor: {e}")
        
        workbook.save(caminho_area_de_trabalho)
        print(f'Dados salvos em {caminho_area_de_trabalho}.')

    except Exception as t:
        sheet[f'A{linha_excel}'] = texto_visivel
        sheet[f'C{linha_excel}'] = 'NAO CONCLUIDO'
        print(f'Deu erro na linha {texto_visivel}')
        linha_excel += 1
        navegador.refresh()

    
    
navegador.quit()
