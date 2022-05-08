import apps

import PySimpleGUI as sg

BITCOIN = apps.pegandoCotaçao('https://www.google.com/finance/quote/BTC-BRL?sa=X&ved=2ahUKEwjIh6nDpM73AhWUFrkGHZDOAKYQ-fUHegQIAhAX&window=MAX')
DOLLAR = apps.pegandoCotaçao('https://www.google.com/finance/quote/USD-BRL')
EURO = apps.pegandoCotaçao('https://www.google.com/finance/quote/EUR-BRL')

layout = [

    #AREA DO BOTÃO, INPUT E TEXTO
    [sg.Text('DIGITE O CÓDIGO DA AÇÃO:',font='Arial 15', background_color='MediumOrchid'),
     sg.Input(str(' ').strip().upper(), key='-CODIGO-')],
    
    #BOTÃO PARA MOSTRA A COTAÇÃO
    [sg.Button('MOSTRAR COTAÇÃO', key='-SHOW-', expand_x= True)],
    [sg.VPush('blueviolet')],

    #TEXTO ONDE VAI APARECER O NOME DA EMPRESA E A COTAÇÃO
    [sg.Text('',key='-EMPRESA-',font='Arial 15',background_color='blueviolet')],   
    [sg.Text('',key='-COTAÇÃO-',expand_x=1,font='Arial 25',background_color='blueviolet')],

    #COTAÇÃO FIXA DO DOLLAR E BITICOIN
    [sg.Text(str('DOLLAR:  '), background_color='blueviolet', justification='right', expand_x=True),
        sg.Text(str(DOLLAR['AÇÃO']['COTAÇÃO']), background_color='blueviolet',justification='right')],
    
    [sg.Text(str('BITCOIN:'),background_color='blueviolet',justification='right',expand_x=True),
        sg.Text(str(BITCOIN['AÇÃO']['COTAÇÃO'][0:7]), background_color='blueviolet')],  
    
    [sg.Text(str('EURO   :  '),background_color='blueviolet',justification='right',expand_x=True),
        sg.Text(str(EURO['AÇÃO']['COTAÇÃO'][0:7]), background_color='blueviolet',justification='right')], 
    
    [sg.VPush('blueviolet')]
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