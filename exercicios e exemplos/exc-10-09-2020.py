import requests

a= requests.get ('https://viacep.com.br/ws/01001000/json/')
dir(a)

def gera_cpf():
    dict = {}
    dict['acao'] = 'gerar_cpf'
    dict['pontuacao']= 'S'
    dict['cpf_estado']=''
    url = 'https://www.4devs.com.br/ferramentas_online.php'
    a = requests.post(url, dict)
    return a.text