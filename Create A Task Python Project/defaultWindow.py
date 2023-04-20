import PySimpleGUI as GUI

def run():
    # lists to hold information relating to adding calories
    foodDrinkNames = []
    calories = []
    foodEntryDates = []

    # list to hold the distance traveled if the user does cardio
    distanceTraveled = []

    # list to hold the weight and reps if the use does weight training
    workoutWeight = []
    workoutReps = []
    workoutEntryDates = []

    # Set theme/color of window and its elements
    GUI.theme('DarkBlue14')
     
    # creates the window layout object
    mainWindowLayout = [[GUI.Text("Select a Date and enter in your food and its corresponding calories.")], # Text 
                        [GUI.Input(key="Calendar", size=(20,1)), GUI.CalendarButton("Click to pop out calendar", close_when_date_chosen=True,  target="Calendar", location=(0,0), no_titlebar=False,)],
                        [GUI.Text("Enter the name of the food/drink: "), GUI.InputText()], # input text
                        [GUI.Text("Enter the number of calories it is: "), GUI.InputText()], # input text
                        [GUI.Button("Log Entry"), GUI.Button("Exit")]] # buttons

    # Initialize the window object and pass in our layout object
    # This actually creates the window.
    window = GUI.Window("Health Fit 100 app", mainWindowLayout)
    
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        # assigns event and values variables to the data on our boot Window using the .read() method
        event, values = window.read()
        
        # prints our values for testing purposes
        print(event, values)
        
        # checks conditions (if user closes window or clicks exit) to see if we should end our loop
        if event == GUI.WIN_CLOSED or event == "Exit":
            break

        # appends our lists if an entry is logged
        if event == "Log Entry":
            foodDrinkNames.append(values[0])
            calories.append(values[1])
            calendarInput = values["Calendar"]

    # closes window
    window.close()