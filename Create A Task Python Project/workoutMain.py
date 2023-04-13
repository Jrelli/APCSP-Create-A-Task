import PySimpleGUI as GUI
import time as T
from window import run

def main():
    print("Booting Health Fit 100 App... ")
    bootWinLayout = [[GUI.Text("Booting Health Fit 100 App.... ")]]
    bootWindow = GUI.Window("Health Fit 100", bootWinLayout, margins=(50, 50)).read()
    T.sleep(2)
    bootWindow.close
    run()

if __name__ == "__main__":
    main()