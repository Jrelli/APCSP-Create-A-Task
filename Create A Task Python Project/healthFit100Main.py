# Importing the Py Simple GUI module to create a Graphical User Interface
# Py Simple GUI is an external library not made by me, here is a link to their website
# https://www.pysimplegui.org/en/latest/
import PySimpleGUI as GUI

# Importing date and time from the computer to, as you guessed, access the date and time
from datetime import datetime

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
    # list to hold the weight and reps if the use does weight training
    workoutWeight = []
    workoutReps = []
    
    # lists to hold the dates of entries
    cardioEntryDates = []
    weightEntryDates = []
    foodEntryDates = []

    # Sets default user weight to 180lbs
    userWeight = 180

    # layout object to hold the elements on the calorie intake tab
    calorieIntakeLayout = [[GUI.Text("Log your meals!")],
                           [GUI.Input(key="Food Calendar", size = (20,1)), GUI.CalendarButton("Click to pop out calendar", close_when_date_chosen = True,  target = "Food Calendar", no_titlebar = False,)],
                           [GUI.Text("Enter the name of the food/drink: "), GUI.InputText()], # input text
                           [GUI.Text("Enter the number of calories it is: "), GUI.InputText()], # input text
                           [GUI.Button("Log Food Entry")]] # button to log entry

    # layout object to hold the elements on the calorie burning tab
    cardioLayout = [[GUI.Text("Log your cardio workouts")],
                    [GUI.Input(key = "Cardio Calendar", size = (20,1)), GUI.CalendarButton("Click to pop out calendar", close_when_date_chosen = True,  target = "Cardio Calendar", no_titlebar = False,)],
                    [GUI.Text("Enter runner's weight(lbs): "), GUI.InputText()], # input text
                    [GUI.Text("Enter the distance traveled(miles): "), GUI.InputText()], # input text
                    [GUI.Button("Log Cardio Entry")]]
    
    # layout object to hold the elements on the weight training tab
    weightTrainingLayout = [[GUI.Text("Log your weight workouts")],
                            [GUI.Input(key = "Weight Calendar", size = (20,1)), GUI.CalendarButton("Click to pop out calendar", close_when_date_chosen = True,  target = "Weight Calendar", no_titlebar = False,)],
                            [GUI.Text("Enter the weight used(lbs): "), GUI.InputText()], # input text
                            [GUI.Text("Enter the number reps: "), GUI.InputText()], # input text
                            [GUI.Button("Log Weight Training Entry")]]

    # layout object to hold the elements on the history tab
    historyLayout = [[GUI.Text("See your history!")],
                     [GUI.Button("Foods Review")],
                     [GUI.Button("Calories Review")],
                     [GUI.Button("Workout Review")]]
    
    # main layout object that holds our center title, and will go on to hold the rest of the tabs.
    mainWindowLayout = [[GUI.Text('Health Fit 100', size = (38, 1), justification = 'center', font = ("Helvetica", 16), relief = GUI.RELIEF_RIDGE, k = '-TEXT HEADING-', enable_events = True)]]
    
    # creates and adds a tab group object with all our tabs.
    mainWindowLayout += [[GUI.TabGroup([[GUI.Tab('Calorie Intake', calorieIntakeLayout),
                                         GUI.Tab('Cardio', cardioLayout),
                                         GUI.Tab("Weight Training", weightTrainingLayout),
                                         GUI.Tab('History', historyLayout)]],
                                       key='-TAB GROUP-', expand_x=True, expand_y=True),]]

    # Initialize the window object and pass in our layout object, This actually creates the window.
    window = GUI.Window("Health Fit 100", mainWindowLayout, grab_anywhere=True, resizable=True, margins=(0, 0), finalize = True)

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
        
        # If the log food entry button is pressed
        elif event == "Log Food Entry":
            # Check if a value was inputted for calories, if one was append to the list
            if values[1] != '':
                calories.append(values[1])
                validInput = True
            else:
                validInput = False
                print("Calories Needed!")
                GUI.popup("Calories Needed!", keep_on_top = True)
            
            # If calories were inputted, then append the date and name lists
            if validInput:
                # If no calendar date was entered, by default today is entered
                if values["Food Calendar"] != '':
                    foodEntryDates.append(str(values["Food Calendar"])[0:9])
                else:
                    foodEntryDates.append(str(datetime.now())[0:9])
                
                # Append food and drink names to output later.
                foodDrinkNames.append(values[0])
   
        # If the log cardio button is pressed.
        elif event == "Log Cardio Entry":
            # If no weight was entered, then don't run and print out error
            if values[2] != '':
                userWeight = values[2]
                validInput = True
            else:
                validInput = False
                print("User Weight Needed!")
                GUI.popup("User Weight Needed!", keep_on_top = True)

            # If weight was entered, check if distance was entered, then append calendar
            if validInput:
                if values[3] != '':
                    distanceTraveled.append(values[3])
                    validInput = True
                else:
                    validInput = False
                    print("Distance Ran Needed!")
                    GUI.popup("Distance Ran Needed!", keep_on_top = True)

                if validInput:
                    if values["Cardio Calendar"] != '':
                        cardioEntryDates.append(str(values["Cardio Calendar"])[0:9])
                    else:
                        cardioEntryDates.append(str(datetime.now())[0:9])
        
        # If the log weight training entry was added
        elif event == "Log Weight Training Entry":
            # If a value was entered.
            if(values[0] != '' or values[0] != ''):
                workoutWeight.append(values[4])
                workoutReps.append(values[5])
                validInput = True
            else:
                validInput = False
                print("Reps and/or Weight needed!")
                GUI.popup("Reps and/or Weight needed!", keep_on_top = True)

            if validInput:
                if weightEntryDates != '':
                    weightEntryDates.append(str(values["Weight Calendar"])[0:9])
                else:
                    weightEntryDates.append(str(datetime.now())[0:9])

        # If the list of food buttons is pressed
        elif event == "Foods Review":
            if(len(foodDrinkNames) > 0):
                GUI.popup("Food and Drinks Consumed: " + str(foodDrinkNames) + "\n Dates Consumed: " + str(foodEntryDates), keep_on_top = True)
            else:
                GUI.popup("No Food Name entries in database...", keep_on_top = True)
                
        
        # If the list of food buttons is pressed
        elif event == "Calories Review":
            totalCalories = 0
            for calorieEntry in calories:
                totalCalories += float(calorieEntry)
            
            totalDistanceTraveled = 0
            for distanceEntry in distanceTraveled:
                totalDistanceTraveled += float(distanceEntry)

            totalWeightLifted = 0
            for reps in workoutReps:
                for weightEntry in workoutWeight:
                    totalWeightLifted += (float(weightEntry) * float(reps))

            totalCaloriesBurned = (float(totalWeightLifted) / 10) + (float(totalDistanceTraveled) * float(userWeight))
            GUI.popup("Total Calories Eaten: " + str(totalCalories) + "\nTotal Calories Burned: " + str(totalCaloriesBurned) + "\nCalorie Surplus or Deficit: " + str(float(totalCalories) - float(totalCaloriesBurned)), keep_on_top = True)

        # If the list of food buttons is pressed
        elif event == "Workout Review":
            totalDistanceTraveled = 0
            for distanceEntry in distanceTraveled:
                totalDistanceTraveled += float(distanceEntry)
            
            totalWeightLifted = 0
            totalReps = 0
            for reps in workoutReps:
                totalReps += int(reps)
                for weightEntry in workoutWeight:
                    totalWeightLifted += (int(weightEntry) * int(reps))

            GUI.popup("Total Distance Walked/Ran: " + str(totalDistanceTraveled) + "miles " + "\nTotal Weight Lifted: " + str(totalWeightLifted) + "lbs " + "\nTotal Reps: " + str(totalReps), keep_on_top = True)

        # Prints for testing
        print("Current Date: " + str(datetime.now())[0:9])
        for value in values:
            print("Key: " + str(value))
            print("Value: " + str(values[value]))
            print(" ")
        print("Food Names List: " + str(foodDrinkNames))
        print("Calories List: " + str(calories))
        print("Distance List: " + str(distanceTraveled))
        print("Weight List: " + str(workoutWeight))
        print("Workout Reps List: " + str(workoutReps))
        print("Workout Entry Dates: " + str(cardioEntryDates))
        print("Food entry dates List: " + str(foodEntryDates))

# Main method
if __name__ == "__main__":
    main()