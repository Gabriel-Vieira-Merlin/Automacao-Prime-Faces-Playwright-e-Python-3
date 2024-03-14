#Importação das biliotecas
from playwright.sync_api import sync_playwright
import time
import datetime

#Função para escolher o design
def escolhe_design():
    while True:
        design = input('Selecione qual design você quer testar (1 a 7): ')

        #Se o usuário digitar 1, a opção será Material Light
        if design == '1':
            global design_link
            design_link = 'xpath=//*[@id="j_idt11"]/div/div/div[1]'
            break

        #Se o usuário digitar 2, a opção será Material Dark
        elif design == '2':
            design_link = 'xpath=//*[@id="j_idt11"]/div/div/div[2]'
            break

        #Se o usuário digitar 3, a opção será Bootstrap Light
        elif design == '3':
            design_link = 'xpath=//*[@id="j_idt11"]/div/div/div[3]'
            break

        #Se o usuário digitar 4, a opção será Bootstrap Dark
        elif design == '4':
            design_link = 'xpath=//*[@id="j_idt11"]/div/div/div[4]'
            break

        #Se o usuário digitar 5, a opção será PrimeOne Light
        elif design == '5':
            design_link = 'xpath=//*[@id="j_idt11"]/div/div/div[5]'
            break

        #Se o usuário digitar 6, a opção será PrimeOne Dim
        elif design == '6':
            design_link = 'xpath=//*[@id="j_idt11"]/div/div/div[6]'
            break

        #Se o usuário digitar 7, a opção será PrimeOne Dark
        elif design == '7':
            design_link = 'xpath=//*[@id="j_idt11"]/div/div/div[7]'
            break

        #Se o usuário digita outra coisa, ele pergunta de novo
        else:
            print('Só é permitido 1 a 7')

#Input Style
def escolhe_input_style():
    #Pergunta ao usuário qual input style ele quer
    while True:
        style = input('Selecione o seu input style (1 para outline e 2 para filled): ')

        #Se for 1, o estilo será outline
        if style == '1':
            global style_type
            style_type = 'xpath=//*[@id="j_idt25"]/div[1]/div/div[2]'
            break

        #Se for 2, o estilo será filled
        elif style == '2':
            style_type = 'xpath=//*[@id="j_idt25"]/div[2]/div/div[2]'
            break

        #Se for digitado outro número, ele vai perguntar de novo
        else:
            print('Seleciona somente 1 ou 2')

#Input Text
def escolhe_input_text():
    #Pega o texto que será inserido no default do inputext
    global texto_default
    texto_default = input('Digite algo para testar o Default: ')

    #Pega o texto que será inserido no invalid do inputext
    global texto_invalid
    texto_invalid = input('Digite algo para testar o Invalid: ')

#Icons
def escolhe_icons():
    #Pergunta ao usuário o que ele quer que seja digitado em cada campo
    global icon, search, searchicon
    icon = input('Digite o que será digitado no campo Icon: ')
    search = input('Digite o que será digitado no campo Search: ')
    searchicon = input('Digite o que será digitado no campo Search com um um Icon: ')

#Float Label
def escolhe_float_label():
    global float_label
    #Pergunta ao usuário o que ele quer que seja escrito na Float Label
    float_label = input('Digite o que será inserido na Float Label: ')

#Text Area
def escolhe_text_area():
    #Coleta o texto que irá ser inserido na Text Area
    global text_area
    text_area = input('Digite o que será inserido na Text Area: ')

#Date Picker
def escolhe_data():
    #Escolhe a data para o Date Picker
    global data, dia, mes, ano
    dia = input('Digite a dia: ')
    mes = input('Digite o mês (em número): ')
    ano = input('Digite o ano: ')
    data = f"{dia}/{mes}/{ano}"

#Spinner
def escolhe_spinner():
    #Escolhe o número do spinner
    global spinner
    spinner = input('Digite o número de Spinner: ')

#Chips
def escolhe_chip():
    #Coleta o texto que será inserido no Chips
    global chip
    chip = input('Digite o texto a ser inserido no Chips: ')

#Radio Button
def escolhe_radiobutton():
    global radio, radio_button
    while True:
        #Pergunta ao usuário qual Radio Button será usado
        radio = input('Escolha um Radio button entre 1 a 3: ')
        #Verifica qual foi escolhido e armazena o xpath correspondente
        if radio == '1':
            radio_button = 'xpath=//*[@id="j_idt76"]/div/div[1]/div/div[2]'
            break
        elif radio == '2':
            radio_button = 'xpath=//*[@id="j_idt76"]/div/div[2]/div/div[2]'
            break
        elif radio == '3':
            radio_button = 'xpath=//*[@id="j_idt76"]/div/div[3]/div/div[2]'
            break
        else:
            print('Só é disponível opções de 1 a 3')

#Checkbox
def escolhe_checkbox():
    global opções, resposta, selecionados
    #Dicionário com as opções e seus xpath
    opções = {'1': 'xpath=//*[@id="j_idt81"]/div/div[1]/div/div[2]',
              '2': 'xpath=//*[@id="j_idt81"]/div/div[2]/div/div[2]',
              '3': 'xpath=//*[@id="j_idt81"]/div/div[3]/div/div[2]'}
    selecionados = []
    #Pergunta se o usuário quer selecionar a opção, se sim, armazena os xpath em outra lista
    for opção, xpath in opções.items():
        while True:
            resposta = input(f'Preencher a opção {opção} das Checkboxes? (S/N): ').upper()
            if resposta == 'S':
                selecionados.append(xpath)
                break
            elif resposta == 'N':
                break
            else:
                print('Só é permitido "S" para sim e "N" para não')

#Select Button
def escolhe_selectbutton():
    global opçõesbutton, selectbutton, xpathbutton, valorxpath
    #Cria um dicionário com o xpath de cada opção
    opçõesbutton = {'1': 'xpath=//*[@id="j_idt108"]/div[1]/span',
                    '2': 'xpath=//*[@id="j_idt108"]/div[2]/span',
                    '3': 'xpath=//*[@id="j_idt108"]/div[3]/span'}
    while True:
    #Pega o xpath correspondente da opção
        xpathbutton = input('Escolha uma opção de 1 a 3 do Select Button: ')
        if xpathbutton in opçõesbutton:
            valorxpath = opçõesbutton[xpathbutton]
            break
        else:
            print('Somente 1 a 3')

#Select Button Multiple
def escolhe_selectbutton_multi():
    global opçõesmulti, respostamulti, selecionadosmulti
    #Dicionário com as opções e seus xpath
    opçõesmulti = {'1': 'xpath=//*[@id="j_idt113"]/div[1]/span',
                   '2': 'xpath=//*[@id="j_idt113"]/div[2]/span',
                   '3': 'xpath=//*[@id="j_idt113"]/div[3]/span'}
    selecionadosmulti = []
    #Pergunta se o usuário quer selecionar a opção, se sim, armazena os xpath em outra lista
    for opçãomulti, xpathmulti in opçõesmulti.items():
        while True:
            respostamulti = input(f'Preencher a opção {opçãomulti} do Select Button Multi? (S/N): ').upper()
            if respostamulti == 'S':
                selecionadosmulti.append(xpathmulti)
                break
            elif respostamulti == 'N':
                break
            else:
                print('Só é permitido "S" para sim e "N" para não')

#Rating
def escolhe_rating():
    global rating
    #Cria um dicionário com o xpath de cada opção
    opções_rating = {'0': '//*[@id="j_idt72"]/div[2]', '1': '//*[@id="j_idt72"]/div[3]',
                     '2': '//*[@id="j_idt72"]/div[4]', '3': '//*[@id="j_idt72"]/div[5]',
                     '4': '//*[@id="j_idt72"]/div[6]', '5': '//*[@id="j_idt72"]/div[7]'}
    while True:
        #Pega a avaliação do usuário
        rating = input('Avalie entre 0 e 5 estrelas: ')
        #Verifica se a opção está presente e armazena ela na variável rating
        if rating in opções_rating:
            rating = opções_rating[rating]
            break
        else:
            print('Escolha somente entre 0 a 5')

#Icons
def escolhe_icon():
    global icon_button
    #Cria um dicionário com as opções e seus xpath
    opções_icon = {'Icon': 'xpath=//*[@id="j_idt121"]/span[2]',
                   'Icon Submit': 'xpath=//*[@id="j_idt122"]/span[2]',
                   'Submit Icon': 'xpath=//*[@id="j_idt123"]/span[2]'}
    #Pega a resposta do usuário e guarda numa variável
    while True:
        icon_button = input('Selecione uma opção(Icon, Icon Submit, Submit Icon): ')
        if icon_button in opções_icon:
            icon_button = opções_icon[icon_button]
            break
        else:
            print('Selecione apenas entre as opções Icon, Submit ou Submit Icon')

#Severities
def escolhe_severity():
    global severity
    #Cria um dicionário com o xpath de cada opção
    opções_severities = {'Primary': 'xpath=//*[@id="j_idt125"]/span', 'Secondary': 'xpath=//*[@id="j_idt126"]/span',
                         'Success': 'xpath=//*[@id="j_idt127"]/span', 'Info': 'xpath=//*[@id="j_idt128"]/span',
                         'Warning': 'xpath=//*[@id="j_idt129"]/span', 'Help': 'xpath=//*[@id="j_idt130"]/span',
                         'Danger': 'xpath=//*[@id="j_idt131"]/span'}
    #Pega a escolha e guarda numa variável
    while True:
        severity = input('Selecione uma Severity (Primary, Secondary, Success, Info, Warning, Help, Danger): ')
        if severity in opções_severities:
            severity = opções_severities[severity]
            break
        else:
            print('Selecione somente as opções Primary, Secondary, Success, Info, Warning, Help, Danger')

#Raised Buttons
def escolhe_raisedbuttons():
    global raised
    #Cria um dicionário pro Xpath de cada opção
    opções_raised = {'Primary': 'xpath=//*[@id="j_idt133"]/span', 'Secondary': 'xpath=//*[@id="j_idt134"]/span',
                         'Success': 'xpath=//*[@id="j_idt135"]/span', 'Info': 'xpath=//*[@id="j_idt136"]/span',
                         'Warning': 'xpath=//*[@id="j_idt137"]/span', 'Help': 'xpath=//*[@id="j_idt138"]/span',
                         'Danger': 'xpath=//*[@id="j_idt139"]/span'}
    #Pega a opção escolhida e armazena numa variável
    while True:
        raised = input('Selecione um Raised Button (Primary, Secondary, Success, Info, Warning, Help, Danger): ')
        if raised in opções_raised:
            raised = opções_raised[raised]
            break
        else:
            print('Selecione somente as opções Primary, Secondary, Success, Info, Warning, Help, Danger')

#Rounded Buttons
def escolhe_roundedbuttons():
    global rounded
    #Cria um dicionário pro Xpath de cada opção
    opções_rounded = {'Primary': 'xpath=//*[@id="j_idt141"]/span', 'Secondary': 'xpath=//*[@id="j_idt142"]/span',
                     'Success': 'xpath=//*[@id="j_idt143"]/span', 'Info': 'xpath=//*[@id="j_idt144"]/span',
                     'Warning': 'xpath=//*[@id="j_idt145"]/span', 'Help': 'xpath=//*[@id="j_idt146"]/span',
                     'Danger': 'xpath=//*[@id="j_idt147"]/span'}
    #Pega a opção escolhida e armazena numa variável
    while True:
        rounded = input('Selecione um Rounded Button (Primary, Secondary, Success, Info, Warning, Help, Danger): ')
        if rounded in opções_rounded:
            rounded = opções_rounded[rounded]
            break
        else:
            print('Selecione somente as opções Primary, Secondary, Success, Info, Warning, Help, Danger')

#Flat Buttons
def escolhe_flatbuttons():
    global flat
    #Cria um dicionário pro Xpath de cada opção
    opções_flat = {'Primary': 'xpath=//*[@id="j_idt149"]/span', 'Secondary': 'xpath=//*[@id="j_idt150"]/span',
                      'Success': 'xpath=//*[@id="j_idt151"]/span', 'Info': 'xpath=//*[@id="j_idt152"]/span',
                      'Warning': 'xpath=//*[@id="j_idt153"]/span', 'Help': 'xpath=//*[@id="j_idt154"]/span',
                      'Danger': 'xpath=//*[@id="j_idt155"]/span', 'Plain': 'xpath=//*[@id="j_idt156"]/span'}
    #Pega a opção escolhida e armazena numa variável
    while True:
        flat = input('Selecione um Flat Button (Primary, Secondary, Success, Info, Warning, Help, Danger, Plain): ')
        if flat in opções_flat:
            flat = opções_flat[flat]
            break
        else:
            print('Selecione somente as opções Primary, Secondary, Success, Info, Warning, Help, Danger, Plain')

#Raised Text
def escolhe_raisedtext():
    global raisedtext
    #Cria um dicionário pro Xpath de cada opção
    opções_raisedtext = {'Primary': 'xpath=//*[@id="j_idt158"]/span', 'Secondary': 'xpath=//*[@id="j_idt159"]/span',
                   'Success': 'xpath=//*[@id="j_idt160"]/span', 'Info': 'xpath=//*[@id="j_idt161"]/span',
                   'Warning': 'xpath=//*[@id="j_idt162"]/span', 'Help': 'xpath=//*[@id="j_idt163"]/span',
                   'Danger': 'xpath=//*[@id="j_idt164"]/span', 'Plain': 'xpath=//*[@id="j_idt165"]/span'}
    #Pega a opção escolhida e armazena numa variável
    while True:
        raisedtext = input('Selecione um Raised Text Button (Primary, Secondary, Success, Info, Warning, Help, Danger, Plain): ')
        if raisedtext in opções_raisedtext:
            raisedtext = opções_raisedtext[raisedtext]
            break
        else:
            print('Selecione somente as opções Primary, Secondary, Success, Info, Warning, Help, Danger, Flat, Plain')

#Outlined Buttons
def escolhe_outlinedbuttons():
    global outline
    #Cria um dicionário pro Xpath de cada opção
    opções_outline = {'Primary': 'xpath=//*[@id="j_idt167"]/span', 'Secondary': 'xpath=//*[@id="j_idt168"]/span',
                      'Success': 'xpath=//*[@id="j_idt169"]/span', 'Info': 'xpath=//*[@id="j_idt170"]/span',
                      'Warning': 'xpath=//*[@id="j_idt171"]/span', 'Help': 'xpath=//*[@id="j_idt172"]/span',
                      'Danger': 'xpath=//*[@id="j_idt173"]/span'}
    # Pega a opção escolhida e armazena numa variável
    while True:
        outline = input('Selecione um Outlined Button (Primary, Secondary, Success, Info, Warning, Help, Danger): ')
        if outline in opções_outline:
            outline = opções_outline[outline]
            break
        else:
            print('Selecione somente as opções Primary, Secondary, Success, Info, Warning, Help, Danger')

#Rounded Icons
def escolhe_roundedicons():
    global roundicon
    #Cria um dicionário com o xpath de cada opção
    opções_roundicon = {'Marcador': 'xpath=//*[@id="j_idt175"]/span[2]', 'Lupa': 'xpath=//*[@id="j_idt176"]/span[2]',
                        'Perfil': 'xpath=//*[@id="j_idt177"]/span[2]', 'Sino': 'xpath=//*[@id="j_idt178"]/span[2]',
                        'Coração': 'xpath=//*[@id="j_idt179"]/span[2]', 'X': 'xpath=//*[@id="j_idt180"]/span[2]',
                        'Visto': 'xpath=//*[@id="j_idt181"]/span[2]'}
    #Pega a opção escolhida e bota numa variável
    while True:
        roundicon = input('Escolha um Rounded Icon entre Marcador, Lupa, Perfil, Sino, Coração, X e Visto: ')
        if roundicon in opções_roundicon:
            roundicon = opções_roundicon[roundicon]
            break
        else:
            print('Essa não é uma opção válida')

#Rounded Text Icons
def escolhe_texticons():
    global texticon
    #Cria um dicionário com o xpath de cada opção
    opções_texticon = {'Marcador': 'xpath=//*[@id="j_idt184"]/span[2]', 'Lupa': 'xpath=//*[@id="j_idt185"]/span[2]',
                        'Perfil': 'xpath=//*[@id="j_idt186"]/span[2]', 'Sino': 'xpath=//*[@id="j_idt187"]/span[2]',
                        'Coração': 'xpath=//*[@id="j_idt188"]/span[2]', 'X': 'xpath=//*[@id="j_idt189"]/span[2]',
                        'Visto': 'xpath=//*[@id="j_idt183"]/span[2]', 'Filtro': 'xpath=//*[@id="j_idt190"]/span[2]'}
    #Pega a opção escolhida e bota numa variável
    while True:
        texticon = input('Escolha um Text Icon entre Marcador, Lupa, Perfil, Sino, Coração, X, Visto e Filtro: ')
        if texticon in opções_texticon:
            texticon = opções_texticon[texticon]
            break
        else:
            print('Essa não é uma opção válida')

#Outline Icons
def escolhe_outlineicons():
    global outlineicon
    #Cria um dicionário com o xpath de cada opção
    opções_outlineicon = {'Marcador': 'xpath=//*[@id="j_idt193"]/span[2]', 'Lupa': 'xpath=//*[@id="j_idt194"]/span[2]',
                       'Perfil': 'xpath=//*[@id="j_idt195"]/span[2]', 'Sino': 'xpath=//*[@id="j_idt196"]/span[2]',
                       'Coração': 'xpath=//*[@id="j_idt197"]/span[2]', 'X': 'xpath=//*[@id="j_idt198"]/span[2]',
                       'Visto': 'xpath=//*[@id="j_idt192"]/span[2]'}
    # Pega a opção escolhida e bota numa variável
    while True:
        outlineicon = input('Escolha um Outlined Icon entre Marcador, Lupa, Perfil, Sino, Coração, X e Visto: ')
        if outlineicon in opções_outlineicon:
            outlineicon = opções_outlineicon[outlineicon]
            break
        else:
            print('Essa não é uma opção válida')

#Badges
def escolhe_badge():
    global badge
    #Cria um dicionário com os xpath de cada badge
    opções_badges = {'Emails': 'xpath=//*[@id="j_idt201"]/span', 'Messages': 'xpath=//*[@id="j_idt203"]/span[2]'}
    #Pega a resposta do usuário e guarda numa variável
    while True:
        badge = input('Selecione uma opção entre Emails e Messages: ')
        if badge in opções_badges:
            badge = opções_badges[badge]
            break
        else:
            print('Essa não é uma opção válida')

#Button Set
def escolhe_buttonset():
    global buttonset
    #Cria um dicionário com sua opções e seus xpath respectivos
    opções_buttonset = {'Save': 'xpath=//*[@id="j_idt205"]/span[2]', 'Delete': 'xpath=//*[@id="j_idt206"]/span[2]', 'Cancel': 'xpath=//*[@id="j_idt207"]/span[2]'}
    #Pega a resposta e guarda numa variável
    while True:
        buttonset = input('Selecione uma opção entre Save, Delete e Cancel: ')
        if buttonset in opções_buttonset:
            buttonset = opções_buttonset[buttonset]
            break
        else:
            print('Essa não é uma opção válida')

#Accordion Pannel
def escolhe_accordionpannel():
    global selecionadosaccordion
    #Dicionário com as opções e os xpath
    opçõesaccordion = {'I': 'xpath=//*[@id="j_idt236:j_idt237_header"]', 'II': 'xpath=//*[@id="j_idt236:j_idt239_header"]', 'III': 'xpath=//*[@id="j_idt236:j_idt241_header"]'}
    selecionadosaccordion = []
    #Pega a opções escolhidas e coloca numa variável
    for opçãoaccordion, xpathaccordion in opçõesaccordion.items():
        while True:
            if opçãoaccordion == 'I':
                respostaaccordion = input(f'Fechar o Header {opçãoaccordion}?(S/N): ').upper()
                if respostaaccordion == 'S':
                    selecionadosaccordion.append(xpathaccordion)
                    break
                elif respostaaccordion == 'N':
                    break
                else:
                    print('Essa não é uma resposta válida')
            else:
                respostaaccordion = input(f'Abrir o Header {opçãoaccordion}?(S/N): ').upper()
                if respostaaccordion == 'S':
                    selecionadosaccordion.append(xpathaccordion)
                    break
                elif respostaaccordion == 'N':
                    break
                else:
                    print('Essa não é uma resposta válida')

#Escolhe Tab View
def escolhe_tabview():
    global tabview
    #Cria um dicionário com as opções e seus respectivos xpath
    opções_tabview = {'I': 'xpath=//*[@id="j_idt244"]/ul/li[1]/a', 'II': 'xpath=//*[@id="j_idt244"]/ul/li[2]/a', 'III': 'xpath=//*[@id="j_idt244"]/ul/li[3]/a'}
    #Pega a opção do usuário e guarda numa variável
    while True:
        tabview = input('Selecione um entre "I", "II" e "III": ')
        if tabview in opções_tabview:
            tabview = opções_tabview[tabview]
            break
        else:
            print('Esse não é uma resposta válida')

#Escolhe as configurações do design material
def config1():
    global cor1, cor2, tcor1, tcor2
    #Cor primária
    cor1 = input('Insira o colorhex que desejar para a cor primária (EX: #3C153B): ').lower()
    cor1 = f'#{cor1}'

    #Cor Secundária
    cor2 = input('Insira o colorhex que desejar para a cor secundária (EX: #C42021): ').lower()
    cor2 = f'#{cor2}'

    #Cor do texto primário
    tcor1 = input('Insira o colorhex que desejar para a cor do texto primário (EX: #EDB458): ').lower()
    tcor1 = f'#{tcor1}'

    #Cor do texto secundário
    tcor2 = input('Insira o colorhex que desejar para a cor do texto secundário (EX: #F0C987): ').lower()
    tcor2 = f'#{tcor2}'

#Escolhe as configurações dos designs restantes
def config2():
    global text1s, text2s, braidius, opacity, cor1s, tcor1s, hlcors, hltcors, hover, focus, error

    #Cor do texto primário
    text1s = input('Insira o colorhex que desejar para a cor do texto primário (EX: #EDB458): ').lower()
    text1s = f'#{text1s}'

    #Cor do texto secundário
    text2s = input('Insira o colorhex que desejar para a cor do texto secundário (EX: #F0C987): ').lower()
    text2s = f'#{text2s}'

    #Número do Border Radius
    braidius = input('Digite o border radius desejado em pixels: ')
    braidius = f'{braidius}px'

    #Nível de opacidade
    opacity = input('Digite o valor da opacidade deseja: ')

    #Cor Primária
    cor1s = input('Insira o colorhex que desejar para a cor primária (EX: #3C153B): ').lower()
    cor1s = f'#{cor1s}'

    #Cor do texto na cor primária
    tcor1s = input('Insira o colorhex que desejar para a cor do texto na cor primária (EX: #EDB458): ').lower()
    tcor1s = f'#{tcor1s}'

    #Cor do Highlight
    hlcors = input('Insira o colorhex que desejar para a cor do highlight (EX: #F1D302): ').lower()
    hlcors = f'#{hlcors}'

    #Cor do texto no Highlight
    hltcors = input('Insira o colorhex que desejar para a cor do texto no highlight (EX: #0F110C): ').lower()
    hltcors = f'#{hltcors}'

    #Cor do Hover Background
    hover = input('Insira o colorhex que desejar para a cor do hover (EX: #F1D302): ').lower()
    hover = f'#{hover}'

    #Cor do Focus Outline
    focus = input('Insira o colorhex que desejar para a cor do outline (EX: #00A878): ').lower()
    focus = f'#{focus}'

    #Cor do Error
    error = input('Insira o colorhex que desejar para a cor do error (EX: #E2D4BA): ').lower()
    error = f'#{error}'

#Realiza a automação
def automacao():
    #Cria um navegador
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)

        #Cria uma nova página
        pagina = navegador.new_page()
        pagina.wait_for_load_state("load")

        #Indica qual página deve ser acessada
        pagina.goto("https://www.primefaces.org/designer-jsf/")
        pagina.wait_for_load_state("load")
        pagina.screenshot(path="print_designs.png", full_page=True)

        #Seleciona o design que será usado
        pagina.locator(design_link).click()

        #Executa a config escolhida
        if design_link in ['xpath=//*[@id="j_idt11"]/div/div/div[1]', 'xpath=//*[@id="j_idt11"]/div/div/div[2]']:
            #Clica na cor primária
            pagina.fill('xpath=//*[@id="j_idt11"]/div[2]/div/div[3]/div[1]/input', cor1)
            #Clica na cor secundária
            pagina.fill('xpath=//*[@id="j_idt11"]/div[2]/div/div[3]/div[3]/input', cor2)
            #Clica no texto primário
            pagina.fill('xpath=//*[@id="j_idt11"]/div[2]/div/div[3]/div[2]/input', tcor1)
            #Clica no texto secundário
            pagina.fill('xpath=//*[@id="j_idt11"]/div[2]/div/div[3]/div[4]/input', tcor2)
        else:
            #Cor do texto primário
            pagina.fill('xpath=//*[@id="j_idt11"]/div[2]/div/div[3]/div[2]/input', text1s)
            #Cor do texto secundário
            pagina.fill('xpath=//*[@id="j_idt11"]/div[2]/div/div[3]/div[3]/input', text2s)
            #Border Radius
            pagina.fill('xpath=//*[@id="j_idt11"]/div[2]/div/div[3]/div[4]/input', braidius)
            #Opacidade do Disabled
            pagina.fill('xpath=//*[@id="j_idt11"]/div[2]/div/div[3]/div[5]/input', opacity)
            #Cor primária
            pagina.fill('xpath=//*[@id="j_idt11"]/div[2]/div/div[4]/div[1]/input', cor1s)
            #Cor do texto na cor primária
            pagina.fill('xpath=//*[@id="j_idt11"]/div[2]/div/div[4]/div[2]/input', tcor1s)
            #Cor do Highlight
            pagina.fill('xpath=//*[@id="j_idt11"]/div[2]/div/div[4]/div[3]/input', hlcors)
            #Cor do texto no Highlight
            pagina.fill('xpath=//*[@id="j_idt11"]/div[2]/div/div[4]/div[4]/input', hltcors)
            #Cor do hover background
            pagina.fill('xpath=//*[@id="j_idt11"]/div[2]/div/div[4]/div[5]/input', hover)
            #Cor do Focus Outline
            pagina.fill('xpath=//*[@id="j_idt11"]/div[2]/div/div[4]/div[6]/input', focus)
            #Cor do Error
            pagina.fill('xpath=//*[@id="j_idt11"]/div[2]/div/div[4]/div[7]/input', error)
        time.sleep(1)

        #Seleciona o input style que será utilizado
        pagina.locator(style_type).click()
        time.sleep(1)

        #Insere o texto no Default do InputText
        pagina.fill('xpath=//*[@id="j_idt47"]', texto_default)
        #Insere o texto no Invalid do InputText
        pagina.fill('xpath=//*[@id="j_idt51"]', texto_invalid)
        time.sleep(1)

        #Insere os textos nos Icons
        pagina.fill('xpath=//*[@id="j_idt53"]', icon)
        pagina.fill('xpath=//*[@id="j_idt55"]', search)
        pagina.fill('xpath=//*[@id="j_idt57"]', searchicon)
        time.sleep(1)

        #Insere os textos na Float Label
        pagina.fill('xpath=//*[@id="username"]', float_label)
        time.sleep(1)

        #Insere os textos na Text Area
        pagina.fill('xpath=//*[@id="j_idt61"]', text_area)
        time.sleep(1)

        #Insera a data escolhida no Date Picker
        pagina.fill('xpath=//*[@id="j_idt65_input"]', data)
        time.sleep(1)

        #Insere o número escolhido no Spinner
        pagina.fill('xpath=//*[@id="basic_input"]', spinner)
        time.sleep(1)

        #Insere o texto escolhido no Chips
        pagina.fill('xpath=//*[@id="j_idt68_input"]', chip)
        time.sleep(1)

        #Clica no radio button escolhido
        pagina.locator(radio_button).click()
        time.sleep(1)

        #Clica nos Checkbox escolhidos
        for xpath in selecionados:
            pagina.locator(xpath).click()
        time.sleep(1)

        #Clica no Toggle Button
        pagina.locator('xpath=//*[@id="j_idt106"]/span').click()
        time.sleep(1)

        #Clica no Select Button
        pagina.locator(valorxpath).click()
        time.sleep(1)

        #Clica nos Select Button multi escolhidos
        for xpathmulti in selecionadosmulti:
            pagina.locator(xpathmulti).click()
        time.sleep(1)

        #Clica na rating seleciona
        pagina.locator(rating).click()
        time.sleep(1)

        #Clica no toggle switch
        pagina.locator('xpath=//*[@id="j_idt74"]/div[2]/span').click()
        time.sleep(1)

        #Clica o botão Basic
        pagina.locator('xpath=//*[@id="j_idt118"]/span').click()
        time.sleep(1)

        #Clica no icon selecionado
        pagina.locator(icon_button).click()
        time.sleep(1)

        #Clica na severity escolhida
        pagina.locator(severity).click()
        time.sleep(1)

        #Clica no raised button escolhido
        pagina.locator(raised).click()
        time.sleep(1)

        #Clica no rounded button escolhido
        pagina.locator(rounded).click()
        time.sleep(1)

        #Clica no flat button escolhido
        pagina.locator(flat).click()
        time.sleep(1)

        #Clica no raised text escolhido
        pagina.locator(raisedtext).click()
        time.sleep(1)

        #Clcia no outlined button escolhido
        pagina.locator(outline).click()
        time.sleep(1)

        #Clica no rounded icon escolhido
        pagina.locator(roundicon).click()
        time.sleep(1)

        #Clica no text icon escolhido
        pagina.locator(texticon).click()
        time.sleep(1)

        #Clica no outline icon escolhido
        pagina.locator(outlineicon).click()
        time.sleep(1)

        #Clica na badge escolhida
        pagina.locator(badge).click()
        time.sleep(1)

        #Clica no buttonset escolhido
        pagina.locator(buttonset).click()
        time.sleep(1)

        #Clica nos Header do Accordion Pannel escolhidos
        for xpathaccordion in selecionadosaccordion:
            pagina.locator(xpathaccordion).click()

        time.sleep(1)

        #Clica no Tab View escolhido
        pagina.locator(tabview).click()

        #Clica no Panel
        pagina.locator('xpath=//*[@id="j_idt252_toggler"]/span').click()

        #Clica no Fieldset
        pagina.locator('xpath=//*[@id="j_idt255"]/legend/span').click()

        pagina.screenshot(path="print.png", full_page=True)

        time.sleep(20)

#Chama as funções
escolhe_design()
#Verifica o design escolhido e chama a config respectiva
if design_link in ['xpath=//*[@id="j_idt11"]/div/div/div[1]', 'xpath=//*[@id="j_idt11"]/div/div/div[2]']:
    config1()
else:
    config2()
escolhe_input_style()
escolhe_input_text()
escolhe_icons()
escolhe_float_label()
escolhe_text_area()
escolhe_data()
escolhe_spinner()
escolhe_chip()
escolhe_radiobutton()
escolhe_checkbox()
escolhe_selectbutton()
escolhe_selectbutton_multi()
escolhe_rating()
escolhe_icon()
escolhe_severity()
escolhe_raisedbuttons()
escolhe_roundedbuttons()
escolhe_flatbuttons()
escolhe_raisedtext()
escolhe_outlinedbuttons()
escolhe_roundedicons()
escolhe_texticons()
escolhe_outlineicons()
escolhe_badge()
escolhe_buttonset()
escolhe_accordionpannel()
escolhe_tabview()
automacao()