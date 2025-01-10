# Torna os campos que ativam o dropdown de município selecionáveis
def selecionar_elementos(navegador):
    ano = Select(WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="form:ano"]'))
    ))
    mes = Select(WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="form:mes"]'))
    ))
    esf_adm = Select(WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="form:esferaAdministrativa"]'))
    ))
    uf = Select(WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="form:uf"]'))
    ))

    return ano, mes, esf_adm, uf


# Preenche o valor no campos
def selecionar_valores_elementos():
    mes.select_by_value(mes_elemento_selecionado)
    sleep(1)
    uf.select_by_visible_text('GO')
    sleep(1)
    ano.select_by_visible_text(ano_elemento_selecionado)
    sleep(1)
    esf_adm.select_by_visible_text('MUNICIPAL')
    sleep(1)


def click_pesquisar():
    try:
        # Clica no botão pesquisar
        botao_pesquisar = navegador.find_element(By.ID, "form:pesquisar")
        botao_pesquisar.click()

        # Aguarda até que o elemento "valor_elemento" esteja disponível (ou o tempo limite expire)
        WebDriverWait(navegador, 30).until(
            EC.presence_of_element_located((By.XPATH, '//td[@class="tdParNum"]/table/tbody/tr/td[2]/span'))
        )
        print("Página carregada e elemento encontrado.")
    except TimeoutException:
        print("O tempo de espera terminou. O elemento não foi encontrado.")