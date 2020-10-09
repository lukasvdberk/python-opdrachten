import PySimpleGUI as sg

sg.theme('DarkAmber')	# Add a touch of color
# All the stuff inside your window.
layout = [ 
            [sg.Image('hoed.png')],
            [sg.Text('Programmeren ja of nee?')],
            [sg.Combo(['yehes', 'yehes'])],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    print(event)
    print('You entered ', values)

window.close()