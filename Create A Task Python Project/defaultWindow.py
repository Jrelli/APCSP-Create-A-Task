import PySimpleGUI as GUI

def run():
    # Add color to the GUI
    GUI.theme('DarkBlue14')
     
    # creates the window layout object
    mainWindowLayout = [[GUI.Text("Some text on Row 1")], # Text
                        [GUI.Text("Enter something on Row 2"), GUI.InputText()], # input text
                        [GUI.Text("Enter something on Row 3"), GUI.InputText()], # input text
                        [GUI.Input(key='-IN-', size=(20,1)), GUI.CalendarButton("Click to pop out calendar", close_when_date_chosen=True,  target='-IN-', location=(0,0), no_titlebar=False,)],
                        [GUI.Button("Ok"), GUI.Button("Cancel")] ] # buttons

    # Initialize the window object and pass in our layout object
    # This actually creates the window.
    window = GUI.Window("Window Title", mainWindowLayout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == GUI.WIN_CLOSED or event == "Cancel": # if user closes window or clicks cancel
            break
        row2Input = values[0]
        row3Input = values[1]
        calendarInput = GUI.popup('You chose:', GUI.popup_get_date())
        print("Calendar date selected" + calendarInput)

    window.close()