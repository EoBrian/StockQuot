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

        informações = soup.find_all('div', class_='P6K39c')
        ceo = informações[9].string
        variação_hoje = informações[1].string
        variação_ano = informações[2].string
        indicePL = informações[5].string

        dicionario['AÇÃO'] = {
            'EMPRESA': nome_empresa,
            'COTAÇÃO': cotação,
            'CEO': ceo,
            'VAR-HOJE': variação_hoje,
            'VAR-ANO': variação_ano,
            'PL': indicePL,
        }

        return dicionario

    except:
        exit()


def parsingMOEDAS(text):
    dicionario = {}

    try:
        soup = BeautifulSoup(text, 'html.parser')
        nome_empresa = soup.find('div', class_='zzDege').string
        cotação = soup.find('div', class_='YMlKec fxKbKc').string

        dicionario['MOEDA'] = {
            'EMPRESA': nome_empresa,
            'COTAÇÃO': cotação,
        }

        return dicionario

    except:
        exit()


def pegandoCotaçao(link):
    requisição = requisiçãoWeb(link)
    
    try:
        parsing = parsingHTML(requisição)
        return parsing
    except:
        parsing2 = parsingMOEDAS(requisição)
        return parsing2
