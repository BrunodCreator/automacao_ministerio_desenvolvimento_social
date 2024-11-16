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
navegador.get('https://aplicacoes.mds.gov.br/suaswebcons/restrito/execute.jsf?b=*tbmepQbsdfmbtQbhbtNC&event=*fyjcjs')

# Preenche os campos que ativam o dropdown de município
ano = Select(navegador.find_element(By.XPATH, '//*[@id="form:ano"]'))
mes = Select(navegador.find_element(By.XPATH, '//*[@id="form:mes"]'))
esf_adm = Select(navegador.find_element(By.XPATH, '//*[@id="form:esferaAdministrativa"]'))
uf = Select(navegador.find_element(By.XPATH, '//*[@id="form:uf"]'))

# Define os valores necessários para ativar o campo de município
mes.select_by_value('10')
sleep(1)
uf.select_by_visible_text('GO')
sleep(1)
ano.select_by_visible_text('2024')
sleep(1)
esf_adm.select_by_visible_text('MUNICIPAL')
sleep(1)

# Aguarda o campo 'municipio' ser ativado (não estar mais 'disabled')
municipio_dropdown = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#form\\:municipio"))
)
municipio = Select(municipio_dropdown)

# Seleciona o município desejado
municipio.select_by_visible_text('ABADIANIA')
sleep(1)

botao_pesquisar = navegador.find_element(By.ID, "form:pesquisar")
botao_pesquisar.click()
sleep(15)
