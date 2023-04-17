# Importing the Py Simple GUI module to create a Graphical User Interface
import PySimpleGUI as GUI

# importing my run method from my defaultWindow file
from defaultWindow import run

def main():
    # Print line to console letting us know the app is booting
    print("Launching Health Fit 100 App... ")
    
    # Add color to the GUI
    GUI.theme('DarkBlue14')
    
    # Create the window layout object
    bootWinLayout = [[GUI.Text("Launching Health Fit 100 App.... ")], # Text
                     [GUI.Button(button_text = "START", auto_size_button = True)]] # Start button
    
    # Initialize the window object and pass in our layout object
    # This actually creates the window.
    bootWindow = GUI.Window("Health Fit 100", bootWinLayout, margins=(50, 50))
    
    # Infinite Loop which keeps our window open until a conditional is met that breaks us out of the loop
    while True:
        # assigns event and values variables to the data on our boot Window using the .read() method
        event, values = bootWindow.read()
        
        # End the program if user closes window or presses the Start button
        if event == "START" or event == GUI.WIN_CLOSED:
            # closes window
            bootWindow.close()
            
            # boots our run method which contains our main app page
            run()
            
            # end while loop
            break
    
# Main method
if __name__ == "__main__":
    main()