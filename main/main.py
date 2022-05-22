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
    
    [sg.Text('',key='-EMPRESA-',font='Arial 14',background_color='blueviolet',expand_x=1),

        sg.Text('CEO:',visible=False,justification='right', expand_x=1,key='1',background_color='blueviolet'), sg.Text('', key='-CEO-',visible=False,background_color='black')],
        [sg.Text('Váriação no dia:',visible=False,justification='right', expand_x=1,key='2',background_color='blueviolet'), sg.Text('', key='-VAR-HOJE-',visible=False,background_color='black')], 

    [sg.Text('',key='-COTAÇÃO-',font='Arial 15',background_color='blueviolet',expand_x=1),

        sg.Text('Váriação no ano:',visible=False,justification='right', expand_x=1, key='3',background_color='blueviolet'), sg.Text('', key='-VAR-ANO-',visible=False,background_color='black')],
        [sg.Text('P/L:',visible=False,justification='right', expand_x=1,key='4',background_color='blueviolet'),sg.Text('', key='-PL-',visible=False,background_color='black')],
    
    [sg.VPush('blueviolet')],
   
    #COTAÇÃO FIXA DO DOLLAR E BITICOIN
    [sg.Push(background_color='black')],

    [sg.Text(str('US$:'),background_color='red'),sg.Text(str(DOLLAR['MOEDA']['COTAÇÃO']),background_color='blueviolet',expand_x=1),
     sg.Text(str('€uro:'),background_color='red'),sg.Text(str(EURO['MOEDA']['COTAÇÃO']),background_color='blueviolet',expand_x=1),
     sg.Text(str('ETH:'),background_color='red'),sg.Text(str(ETHERIUM['MOEDA']['COTAÇÃO']),background_color='blueviolet',expand_x=1),
     sg.Text(str('BTC:'),background_color='red'),sg.Text(str(BITCOIN['MOEDA']['COTAÇÃO']),background_color='blueviolet',expand_x=1)], 

    [sg.Push(background_color='black')],
]

WINDOW = sg.Window('COTAÇÕES', layout= layout, size=(600,300), background_color='blueviolet',button_color='black')

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
           
            for contador in range(1,5):
                WINDOW[f'{contador}'].update(visible=True) 

            WINDOW['-CEO-'].update(parsing['AÇÃO']['CEO'],visible=True)     
            WINDOW['-VAR-HOJE-'].update(parsing['AÇÃO']['VAR-HOJE'],visible=True)
            WINDOW['-VAR-ANO-'].update(parsing['AÇÃO']['VAR-ANO'],visible=True)
            WINDOW['-PL-'].update(parsing['AÇÃO']['PL'],visible=True)
        
        except:
            for contador in range(1,5):
                WINDOW[f'{contador}'].update(visible=False)
            WINDOW['-EMPRESA-'].update('É PRECISO DIGITAR ALGO VÁLIDO!')
            WINDOW['-COTAÇÃO-'].update('')
            WINDOW['-PL-'].update('')
            WINDOW['-VAR-ANO-'].update('')
            WINDOW['-VAR-HOJE-'].update('')
            WINDOW['-CEO-'].update('')

WINDOW.close()