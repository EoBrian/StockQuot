from requests import get
from bs4 import BeautifulSoup


def nomeAção(código_da_ação ='BOVA11'):
    return f"https://www.google.com/finance/quote/{código_da_ação}:BVMF?sa=X&ved=2ahUKEwjk-cXbk8v3AhW7LrkGHayPCyUQ3ecFegQIGxAY"


def requisiçãoWeb(url):
    try:
        site = get(url)
        if site.status_code == 200:
            return site.text
    
    except Exception as error:
        print(f'ERRO NA REQUISIÇÃO: {url}')
        print(error)


def parsingHTML(text):
    dicionario = {}

    try:
        soup = BeautifulSoup(text, 'html.parser')
        nome_empresa = soup.find('div', class_='zzDege').string
        cotação = soup.find('div', class_='YMlKec fxKbKc').string

        dicionario['AÇÃO'] = {
            'EMPRESA': nome_empresa,
            'COTAÇÃO': cotação
        }

    
    except:
        print('')

 
    return dicionario


def pegandoCotaçao(link):
    requisição = requisiçãoWeb(link)
    parsing = parsingHTML(requisição)
    return parsing


