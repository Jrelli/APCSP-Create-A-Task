# Importing the Py Simple GUI module to create a Graphical User Interface
import PySimpleGUI as GUI

# importing my run method from my defaultWindow file
from defaultWindow import run

# Method to set the size and position of the colum, this is used mainly to center the column on the page.
def ColumnFixedSize(layout, size=(None, None), *args, **kwargs):
    # An addition column is needed to wrap the column with the Sizers because the colors will not be set on the space the sizers take
    return GUI.Column([[GUI.Column([[GUI.Sizer(0,size[1]-1), GUI.Column([[GUI.Sizer(size[0]-2,0)]] + layout, *args, **kwargs, pad=(0,0))]], *args, **kwargs)]],pad=(0,0))

def main():
    # Print line to console letting us know the app is booting
    print("Launching Health Fit 100 App... ")
    
    # Set theme/color of window and its elements
    GUI.theme('DarkBlue14')

    columnElements = [[GUI.Button(button_text = "START", auto_size_button = True)]] # Start button element
    
    # Create the window layout object
    bootWinLayout = [[GUI.Text("Launching Health Fit 100 App.... ")],
                     [ColumnFixedSize(columnElements, size=(200, 50), element_justification='c', vertical_alignment='t')]]
    
    # Initialize the window object and pass in our layout object
    # This actually creates the window.
    bootWindow = GUI.Window("Health Fit 100 booter...", bootWinLayout, margins=(100, 10))
    
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