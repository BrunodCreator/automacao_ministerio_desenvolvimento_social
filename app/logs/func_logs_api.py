import requests
from datetime import datetime


def primeira_execucao(cliente="", nomeProcesso="Criando UUID da Execução",
                      nomeRobo="", dataHoraInicioRobo=None, categoria="INFO",
                      numeroPoint=0, dataHoraInicioPoint=None, dataHoraFimPoint=None,
                      statusPoint="Sucesso", statusExecucao="SUCESSO", msgErro="", execucao=""): 
    try:
        #URL da API
        url = ''

        # Cabeçalhos
        headers = {
        "Content-Type": "application/json",
        "Authorization": ""
        }
        
        #registrar os horários de primeira execução e point
        if not dataHoraInicioRobo:
            dataHoraInicioRobo = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if not dataHoraInicioPoint:
            dataHoraInicioPoint = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if not dataHoraFimPoint:
            dataHoraFimPoint = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
        #Corpo da requisição
        payload = {
            "cliente": f"{cliente}",
            "nomeProcesso": f"{nomeProcesso}",
            "nomeRobo": f"{nomeRobo}",
            "dataHoraInicioRobo": f"{dataHoraInicioRobo}",
            "daraHoraFimRobo": "",
            "categoria": f"{categoria}",
            "numeroPoint": f"{numeroPoint}",
            "dataHoraInicioPoint": f"{dataHoraInicioPoint}",
            "dataHoraFimPoint": f"{dataHoraFimPoint}",
            "statusPoint": f"{statusPoint}",
            "statusExecucao": f"{statusExecucao}",
            "msgErro": f"{msgErro}",
            "execucao": f"{execucao}"
        }
        #Enviando a requisição POST
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Levanta exceções para códigos de erro HTTP
        
        #Captura o valor f"{execucao}" para as chamadas posteriores
        execucao = response.json()
        print(execucao)
        
        return nomeProcesso, categoria, numeroPoint, statusPoint,statusExecucao, msgErro, execucao
    
    except requests.exceptions.RequestException as e:
        # Trata exceções relacionadas à requisição HTTP
        print(f"Erro na requisição: {e}")
        
        return nomeProcesso, categoria, numeroPoint, statusPoint, statusExecucao, msgErro, None
        
# def exec_inicio_point(cliente, nomeProcesso, nomeRobo, dataHoraInicioRobo, 
#                       numeroPoint, categoria='INFO', statusExecucao='Sucesso',
#                       msgErro='', statusPoint='Sucesso', execucao):
    
#     #URL da API
#     url = ''

#     # Cabeçalhos
#     headers = {
#         "Authorization": "",
#         "Content-Type": "application/json"
#     }
    
#     dataHoraInicioPoint = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     numeroPoint += 1
    
#     #Corpo da requisição
#     payload = {
#         "cliente": f"{cliente}",
#         "nomeProcesso": f"{nomeProcesso}",
#         "nomeRobo": f"{nomeRobo}",
#         "dataHoraInicioRobo": f"{dataHoraInicioRobo}",
#         "daraHoraFimRobo": "",
#         "categoria": f"{categoria}",
#         "numeroPoint": f"{numeroPoint}",
#         "dataHoraInicioPoint": f"{dataHoraInicioPoint}",
#         "dataHoraFimPoint": "",
#         "statusPoint": f"{statusPoint}",
#         "statusExecucao": f"{statusExecucao}",
#         "msgErro": f"{msgErro}",
#         "execucao": f"{execucao}"
#     }

#     #Enviando a requisição POST
#     response = requests.post(url, headers=headers, json=payload)

#     if response.status_code == 200:
#         print(f'Resposta da API: {response.json()}')
#     else:
#         print(f'ERRO: {response.status_code}')
#         print(f'Detalhes', response.text)
