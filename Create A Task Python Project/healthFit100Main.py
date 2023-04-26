# Importing the Py Simple GUI module to create a Graphical User Interface
import PySimpleGUI as GUI


def main():
    # Print line to console letting us know the app is booting
    print("Launching Health Fit 100 App... ")
    
    # Set theme/color of window and its elements
    GUI.theme('DarkBlue14')
    
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

    calorieIntakeLayout = [[GUI.Text("Log your")]]

    calorieBurningLayout = [[]]

    historyLayout = [[]]
    
    mainWindowLayout = [[GUI.Text('Health Fit 100', size = (38, 1), justification = 'center', font = ("Helvetica", 16), relief = GUI.RELIEF_RIDGE, k = '-TEXT HEADING-', enable_events = True)]]
    
    mainWindowLayout +=[[GUI.TabGroup([[GUI.Tab('Calorie Intake', calorieIntakeLayout),
                                        GUI.Tab('Calorie burning', calorieBurningLayout),
                                        GUI.Tab('History', historyLayout)
                                       ]], key='-TAB GROUP-', expand_x=True, expand_y=True),
                        ]]

    # Initialize the window object and pass in our layout object, This actually creates the window.
    window = GUI.Window("Health Fit 100", mainWindowLayout, grab_anywhere=True, resizable=True, margins=(0, 0))

    # Sets the minimum size of the window to the size in which it is at start up.
    window.set_min_size(window.size)
    
    # Infinite Loop which keeps our window open until a conditional is met that breaks us out of the loop
    while True:
        # assigns event and values variables to the data on our boot Window using the .read() method
        event, values = window.read()
        
        # End the program if user closes window or presses the Start button
        if event == "START" or event == GUI.WIN_CLOSED:
            # closes window
            window.close()

            # end while loop
            break
    
# Main method
if __name__ == "__main__":
    main()