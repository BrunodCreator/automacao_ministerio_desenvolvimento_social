import requests
from datetime import datetime


def primeira_execucao(cliente="", nomeProcesso="Criando UUID da Execução",
                      nomeRobo="", dataHoraInicioRobo=None, categoria="INFO",
                      numeroPoint=0, dataHoraInicioPoint=None, dataHoraFimPoint=None,
                      statusPoint="Sucesso", statusExecucao="SUCESSO", msgErro="", execucao=""): 
    try:
        url = ''

        headers = {
        "Content-Type": "application/json",
        "Authorization": "6f2c9478-453d-47db-90de-1538dc6f7203"
        }
        
        if not dataHoraInicioRobo:
            dataHoraInicioRobo = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if not dataHoraInicioPoint:
            dataHoraInicioPoint = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if not dataHoraFimPoint:
            dataHoraFimPoint = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
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
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  
        
        execucao = response.json()
        print(execucao)
        
        return  dataHoraInicioRobo,dataHoraInicioPoint,dataHoraFimPoint, execucao
    
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        
        return dataHoraInicioRobo, None
        
def exec_inicio_point(cliente,nomeProcesso='',
    nomeRobo='', dataHoraInicioRobo='', categoria='',
    numeroPoint='', dataHoraInicioPoint='',
    statusPoint='', statusExecucao='', msgErro='', execucao=''):
    try:
        url = ''

        headers = {
            "Content-Type": "application/json",
            "Authorization": "6f2c9478-453d-47db-90de-1538dc6f7203"
        }
        
        dataHoraInicioPoint = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        payload = {
            "cliente": f"{cliente}",
            "nomeProcesso": f"{nomeProcesso}",
            "nomeRobo": f"{nomeRobo}",
            "dataHoraInicioRobo": f"{dataHoraInicioRobo}",
            "dataHoraFimRobo": "",
            "categoria": f"{categoria}",
            "numeroPoint": f"{numeroPoint}",
            "dataHoraInicioPoint": f"{dataHoraInicioPoint}",
            "dataHoraFimPoint": "",
            "statusPoint": f"{statusPoint}",
            "statusExecucao": f"{statusExecucao}",
            "msgErro": f"{msgErro}",
            "execucao": f"{execucao}"
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        return  dataHoraInicioPoint

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        
        return  dataHoraInicioPoint
    

def exec_fim_point(cliente, nomeProcesso,
    nomeRobo, dataHoraInicioRobo, categoria,
    numeroPoint, dataHoraInicioPoint, dataHoraFimPoint,
    statusPoint, statusExecucao, msgErro, execucao): 
    try:
        url = ''

        headers = {
        "Content-Type": "application/json",
        "Authorization": "6f2c9478-453d-47db-90de-1538dc6f7203"
        }

        if not dataHoraFimPoint:
            dataHoraFimPoint = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

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
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  

        #execucao = response.json()

        return dataHoraFimPoint

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")

        return dataHoraFimPoint
    
    
    
def exec_fim_robo(cliente, nomeProcesso,
    nomeRobo, dataHoraInicioRobo, categoria,
    numeroPoint, dataHoraInicioPoint, dataHoraFimPoint,dataHoraFimRobo,
    statusPoint, statusExecucao, msgErro, execucao): 
    try:
        url = ''

        headers = {
        "Content-Type": "application/json",
        "Authorization": "6f2c9478-453d-47db-90de-1538dc6f7203"
        }
        if not dataHoraFimRobo:
            dataHoraFimRobo = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

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
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Levanta exceções para códigos de erro HTTP

        #execucao = response.json()
        print(execucao)

        return dataHoraFimRobo

    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")

        return dataHoraFimRobo