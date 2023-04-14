import PySimpleGUI as GUI

def run():
    # Add a touch of color
    GUI.theme('DarkAmber')  
     
    # All the stuff inside your window.
    layout = [  [GUI.Text('Some text on Row 1')],
                [GUI.Text('Enter something on Row 2'), GUI.InputText()],
                [GUI.Button('Ok'), GUI.Button('Cancel')] ]

    # Create the Window
    window = GUI.Window('Window Title', layout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == GUI.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        print('You entered ', values[0])

    window.close()