{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}

from tkinter import Label, Entry, Button

# function to calculate property tax
def calculate_tax():
    try:
        # get the actual value entered by the user
        actual_value = float(actual_value_entry.get())

        # calculate assessment value (60% of actual value)
        assessment_value = 0.6 * actual_value

        # calculate property tax ($0.75 for each $100 of assessment value)
        property_tax = (assessment_value / 100) * 0.75

        # display the calculated values in the GUI
        assessment_value_label.config(text=f"Assessment Value: ${assessment_value:,.2f}")
        property_tax_label.config(text=f"Property Tax: ${property_tax:,.2f}")

    except ValueError:
        # handle the case where the user enters invalid input
        assessment_value_label.config(text="Invalid Input")
        property_tax_label.config(text="")

# create the main window
root = tk.Tk()
root.title("Property Tax Calculator")

# create and place widgets in the window
actual_value_label = Label(root, text="Enter Actual Value:")
actual_value_label.pack(pady=10)

actual_value_entry = Entry(root)
actual_value_entry.pack(pady=10)

calculate_button = Button(root, text="Calculate", command=calculate_tax)
calculate_button.pack(pady=10)

assessment_value_label = Label(root, text="")
assessment_value_label.pack(pady=10)

property_tax_label = Label(root, text="")
property_tax_label.pack(pady=10)

# start the GUI event loop
root.mainloop()
import tkinter as tk
from tkinter import Label, Entry, Button

def on_button_click():
    user_input = entry.get()
    label.config(text=f"You entered: {user_input}")

# Create the main window
root = tk.Tk()
root.title("Simple GUI")

# Create and place widgets in the window
label = Label(root, text="Enter something:")
label.pack(pady=10)

entry = Entry(root)
entry.pack(pady=10)

button = Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
