# Importing the Py Simple GUI module to create a Graphical User Interface
import PySimpleGUI as GUI

def main():
    # Print line to console letting us know the app is booting
    print("Launching Health Fit 100 App... ")
    
    # Set theme/color of window and its elements
    GUI.theme('DarkBlue14')
    
    # lists to hold information relating to the gaining of calories
    foodDrinkNames = []
    calories = []

    # list to hold information relating to the calculation of calories lost from cardio
    distanceTraveled = []
    userWeight = []
    # list to hold the weight and reps if the use does weight training
    workoutWeight = []
    workoutReps = []
    
    # lists to hold the dates of entries
    workoutEntryDates = []
    foodEntryDates = []

    # layout object to hold the elements on the calorie intake tab
    calorieIntakeLayout = [[GUI.Text("Log your meals!")],
                           [GUI.Input(key="Calendar1", size = (20,1)), GUI.CalendarButton("Click to pop out calendar", close_when_date_chosen = True,  target = "Calendar1", location = (0,0), no_titlebar = False,)],
                           [GUI.Text("Enter the name of the food/drink: "), GUI.InputText()], # input text
                           [GUI.Text("Enter the number of calories it is: "), GUI.InputText()], # input text
                           [GUI.Button("Log Food Entry")]] # button to log entry

    # layout object to hold the elements on the calorie burning tab
    cardioLayout = [[GUI.Text("Log your cardio workouts")],
                    [GUI.Input(key = "Calendar2", size = (20,1)), GUI.CalendarButton("Click to pop out calendar", close_when_date_chosen = True,  target = "Calendar2", location = (0,0), no_titlebar = False,)],
                    [GUI.Text("Enter runner's weight: "), GUI.InputText()], # input text
                    [GUI.Text("Enter the distance taveled: "), GUI.InputText()], # input text
                    [GUI.Button("Log Cardio Entry")]]
    
    weightTrainingLayout = [[GUI.Text("Log your weight workouts")],
                            [GUI.Input(key = "Calendar3", size = (20,1)), GUI.CalendarButton("Click to pop out calendar", close_when_date_chosen = True,  target = "Calendar3", location = (0,0), no_titlebar = False,)],
                            [GUI.Text("Enter the weight used: "), GUI.InputText()], # input text
                            [GUI.Text("Enter the number reps: "), GUI.InputText()], # input text
                            [GUI.Button("Log Weight Training Entry")]]

    # layout object to hold the elements on the history tab
    historyLayout = [[GUI.Text("See your history!")]]
    
    # main layout object that holds our center title, and will go on to hold the rest of the tabs.
    mainWindowLayout = [[GUI.Text('Health Fit 100', size = (38, 1), justification = 'center', font = ("Helvetica", 16), relief = GUI.RELIEF_RIDGE, k = '-TEXT HEADING-', enable_events = True)]]
    
    # creates and adds a tab group object with all our tabs.
    mainWindowLayout +=[[GUI.TabGroup([[GUI.Tab('Calorie Intake', calorieIntakeLayout),
                                        GUI.Tab('Cardio', cardioLayout),
                                        GUI.Tab("Weight Training", weightTrainingLayout),
                                        GUI.Tab('History', historyLayout)
                                       ]], key='-TAB GROUP-', expand_x=True, expand_y=True),
                        ]]

    # Initialize the window object and pass in our layout object, This actually creates the window.
    window = GUI.Window("Health Fit 100", mainWindowLayout, grab_anywhere=True, resizable=True, margins=(0, 0), finalize = True)

    # Sets the minimum size of the window to the size in which it is at start up.
    window.set_min_size(window.size)
    
    # Infinite Loop which keeps our window open until a conditional is met that breaks us out of the loop
    while True:
        # assigns event and values variables to the data on our boot Window using the .read() method
        event, values = window.read()
        
        for value in values:
            print(value)
            print(values[value])
        
        # End the program if user closes window or presses the Start button
        if event == "START" or event == GUI.WIN_CLOSED:
            # closes window
            window.close()

            # end while loop
            break
        # if event == "Log Food Entry":
        #     foodDrinkNames.append(values[0])
        # if event == "Log Cardio Entry":
        #     distanceTraveled.append(values[1])
        
    
# Main method
if __name__ == "__main__":
    main()