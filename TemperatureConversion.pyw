# Authors: Willem Vidler
# Date: December 14th, 2020
# Program Name: Temperature Conversion
# Program Description: Program that converts celcius into fahrenheit and vice-versa

from tkinter import * # Imports the tkinter module
from tkinter.ttk import * # Replace the tk widget with the ttk ones

# Constants
CELCIUS = "Celcius"
FAHRENHEIT = "Fahrenheit"
CELCIUS_CONV = "Convert to Celcius"
FAHRENHEIT_CONV = "Convert to Fahrenheit"

def celciusToFahrenheit(celcius):
    """Converts Celcius to Fahrenheit"""
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def fahrenheitToCelcius(fahrenheit):
    """Coverts Fahrenheit to Celcius"""
    celcius = (fahrenheit - 32) * 5/9
    return celcius

def fahrenheitClick():
    """
    Called when the farhenheit radiobutton is clicked
    - Swap input/output labels
    """
    inputLabel.configure(text=CELCIUS)
    outputLabel.configure(text=FAHRENHEIT)

def celciusClick():
    """
    Called when the celcius radiobutton is clicked
    - Swap input/output labels
    """
    inputLabel.configure(text=FAHRENHEIT)
    outputLabel.configure(text=CELCIUS)

def convertButtonClick():
    """
    Called when the convert button is clicked
    - Converts temperature from celcius to fahrenheit and vice-versa
    - Displays an error message if input is invalid
    """
    inputValue = inputText.get() # Get the input entry text
    # Validation
    try:
        inputValue = float(inputValue)
        isNumeric = True # Able to convert 
    except:
        outputText.set("Error - Invalid Input!") # Write the error in the output entry
        isNumeric = False # Not able to convert

    # Valid Number
    if isNumeric:
        if conversionType.get() == CELCIUS:
            result = fahrenheitToCelcius(inputValue)
        else: 
            result = celciusToFahrenheit(inputValue)
        outputText.set(round(result,1))

def clearButtonClick():
    """
    Called when the clear button is clicked"
    - Resets input/output text and radiobutton to fahrenheit
    """

    conversionType.set(FAHRENHEIT) # Default selection
    inputText.set("0.0") # Set default Value
    outputText.set("0.0") # Set default Value
    fahrenheitClick() # Reset the labels

def keyHandler(event:Event):
    if event.keysym == "Return":
        convertButtonClick()
    elif event.keysym == "Escape":
        clearButtonClick()

# Window Properties
tk = Tk() # Create a Tk object
tk.title("Temperature Conversion - Willem Vidler and Jesse Talon")
tk.resizable(width=False, height=False) 
tk.bind("<Key>", keyHandler)

# 2 frames holding the widgets
leftFrame = Frame()
rightFrame = Frame()

# Labels
inputLabel = Label(leftFrame, text=CELCIUS)
outputLabel = Label(rightFrame, text=FAHRENHEIT)

# Entries
inputText = StringVar()
inputText.set("0.0") # Set the default
inputEntry = Entry(leftFrame, width=30, textvariable=inputText)
outputText = StringVar()
outputText.set("0.0") # Set the default
outputEntry = Entry(rightFrame, width=30, state="readonly", cursor="no", textvariable=outputText)

# Radio buttons
conversionType = StringVar()
conversionType.set(FAHRENHEIT) # Default selection
fahrenheitRadioButton = Radiobutton(leftFrame, text=FAHRENHEIT_CONV, variable=conversionType, value=FAHRENHEIT, command=fahrenheitClick)
celciusRadioButton = Radiobutton(rightFrame, text=CELCIUS_CONV, variable=conversionType, value=CELCIUS, command=celciusClick)

# Buttons
clearButton = Button(leftFrame, text="Clear", command=clearButtonClick)
convertButton = Button(rightFrame, text="Convert", command=convertButtonClick)

# Position the widgets
#left frame
leftFrame.pack(side="left", padx=(10,5), pady=10)
inputLabel.pack(anchor="w")
inputEntry.pack()
fahrenheitRadioButton.pack(anchor="w")
clearButton.pack(fill="x")
# Right frame
rightFrame.pack(side="right", padx=(5,10), pady=10)
outputLabel.pack(anchor="w")
outputEntry.pack()
celciusRadioButton.pack(anchor="w")
convertButton.pack(fill="x")

# Make the GUI visible
tk.mainloop()