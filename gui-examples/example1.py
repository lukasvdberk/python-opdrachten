import PySimpleGUI as sg

import sorteerhoed_concept



sg.theme('DarkAmber')   # Add a touch of color

# All the stuff inside your window.

layout = [  [sg.Text('sorteer hoed')],

            [sg.Button('Start quiz')],

            [sg.Button('Vorige antwoorden inzien')],

            [sg.Button('Aflsuiten')]]



# Create the Window

window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Aflsuiten': # if user closes window or clicks cancel

        break

    if event == 'Start quiz': # if user starts the quiz

        meerkeuzevragen=sorteerhoed_concept.vragen_ophalen()

        sorteerhoed_concept.vraag_en_antwoord(meerkeuzevragen)

    if event == 'Vorige antwoorden inzien': # if user views old results

        f = open("antwoorden_gebruiker.txt", "r")

        print(f.read())

        f.close

    print(event)



window.close()
