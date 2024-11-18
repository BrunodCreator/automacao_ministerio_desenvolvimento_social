from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

# Configuração do WebDriver
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)

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
    sleep(1)

    # Clica no botão de pesquisa
    botao_pesquisar = navegador.find_element(By.ID, "form:pesquisar")
    botao_pesquisar.click()
    sleep(10)

    try:
        # Localiza o segundo <td> dentro da estrutura <td> -> <table> -> <tbody> -> <tr> -> <td>
        valor_elemento = navegador.find_element(By.XPATH, 
            '//td[@class="tdParNum"]/table/tbody/tr/td[2]/span')
        
        # Extrai o texto visível do elemento
        valor_texto = valor_elemento.text.strip()
        print(f"Valor extraído: {valor_texto}")

    except Exception as e:
        print(f"Erro ao extrair o valor: {e}")

    
    
    
navegador.quit()
