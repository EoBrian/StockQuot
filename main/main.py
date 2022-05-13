import apps

import PySimpleGUI as sg

BITCOIN = apps.pegandoCotaçao('https://www.google.com/finance/quote/BTC-BRL?sa=X&ved=2ahUKEwjIh6nDpM73AhWUFrkGHZDOAKYQ-fUHegQIAhAX&window=MAX')
DOLLAR = apps.pegandoCotaçao('https://www.google.com/finance/quote/USD-BRL')
EURO = apps.pegandoCotaçao('https://www.google.com/finance/quote/EUR-BRL')
ETHERIUM = apps.pegandoCotaçao('https://www.google.com/finance/quote/ETH-BRL')

layout = [

    #AREA DO BOTÃO, INPUT E TEXTO
    [sg.Text('DIGITE O CÓDIGO DA AÇÃO:',font='Arial 15', background_color='MediumOrchid'),
     sg.Input(str(' ').strip().upper(), key='-CODIGO-')], 
    
    #BOTÃO PARA MOSTRA A COTAÇÃO
    [sg.Button('MOSTRAR COTAÇÃO', key='-SHOW-', expand_x= True)],     
   
    #TEXTO ONDE VAI APARECER O NOME DA EMPRESA E A COTAÇÃO 
    [sg.VPush('blueviolet')],

    [sg.Text('',key='-EMPRESA-',font='Arial 20',background_color='blueviolet', justification='center',expand_x=1)],   
    [sg.Text('',key='-COTAÇÃO-',font='Arial 25',background_color='blueviolet',justification='center',expand_x=1)],
    
    [sg.VPush('blueviolet')],
   
    #COTAÇÃO FIXA DO DOLLAR E BITICOIN
    [sg.Push(background_color='black')],

    [sg.Text(str('US$:'),background_color='red'), sg.Text(str(DOLLAR['AÇÃO']['COTAÇÃO']),background_color='blueviolet',expand_x=1),     
    sg.Text(str('€uro:'),background_color='red'), sg.Text(str(EURO['AÇÃO']['COTAÇÃO']),background_color='blueviolet',expand_x=1),
    sg.Text(str('ETH:'),background_color='red'), sg.Text(str(ETHERIUM['AÇÃO']['COTAÇÃO']),background_color='blueviolet',expand_x=1),
    sg.Text(str('BTC:'),background_color='red'),sg.Text(str(BITCOIN['AÇÃO']['COTAÇÃO']),background_color='blueviolet',expand_x=1)], 

    [sg.Push(background_color='black')],
]

WINDOW = sg.Window('COTAÇÕES', layout= layout, size=(500,280), background_color='blueviolet',button_color='black')

while True:
    event, value = WINDOW.read()
    if event == sg.WIN_CLOSED:
        break

    #EM ANDAMENTO    
    if event == '-SHOW-':       
        try:
            nome_ação = apps.nomeAção(value['-CODIGO-'])
            buscando_ação = apps.requisiçãoWeb(nome_ação)
            parsing = apps.parsingHTML(buscando_ação)

            WINDOW['-EMPRESA-'].update(parsing['AÇÃO']['EMPRESA'])
            WINDOW['-COTAÇÃO-'].update(parsing['AÇÃO']['COTAÇÃO'])         
        
        except:
            WINDOW['-EMPRESA-'].update('É PRECISO DIGITAR\nALGO VÁLIDO!')
            WINDOW['-COTAÇÃO-'].update('')

WINDOW.close()