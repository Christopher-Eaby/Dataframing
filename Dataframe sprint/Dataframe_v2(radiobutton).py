# -*- coding: utf-8 -*-
"""
       (`-()_.-=-.
       /66  ,  ,  \
     =(o_/=//_(   /======`
         ~"` ~"~~`
Created on Thu Jul  2 10:05:53 2020
@author: Chris
"""

import pandas as pd #import for pandas
import tkinter as tk #import for gui tkinter

#intalizing the rows, columns and data for the dataframe
dat = ['Simba', 'Lays'], ['Coke', 'Fanta'], ['Cadbury', 'Tex'], ['Pepper Steak', 'Chicken'], ['Pear', 'Apple', 'Orange'], ['Vanilla', 'Choclate'], ['Spinach', 'Cabbage']
rows = ['Chips', 'Cooldrinks', 'Chocolates', 'Pies', 'Fruit', 'Cupcakes', 'Veggies']
column = ['Item 1', 'Item 2', 'Item 3']
     
#creates the dataframe
df = pd.DataFrame(data = dat, index = rows, columns = column)

#creates the gui using tkinter frame manager
gui = tk.Tk()
#sets the title 
gui.title("DataFrame Manager GUI")
#sets the size
gui.geometry("275x280")
#integer variable created
v = tk.IntVar()

#creates a textfield for displaying the info from the dataframe
txt = tk.Text(gui, fg = "white", bg = "purple", height = 5, width = 35)
#places the text field over the gridding system
txt.grid(columnspan = 4, pady = 5)

#function for finding the info related to the selection from the Radiobutton
def displayfilter(choice):
    #clears the field
    txt.delete("1.0","end")
    #finds the info needed in the dataframe according to the Radiobutton selected
    ans = df.filter(like = choice, axis = 0)
    #inserts all into the text field
    txt.insert(tk.END, ans)

#creates a label with text
lbl1 = tk.Label(gui, text = "What would you like to display ?", justify = tk.CENTER, padx = 30, pady = 10)
lbl1.grid(columnspan = 4)

#creates 7 Radiobuttons with corresponding text to the usage of the Radiobutton
#Radiobuttons use the command to run the function created to find what the user wants
#what the user wants is then parsed into the function and it returns the info in the text field
b1 = tk.Radiobutton(gui, text = "Chips", variable = v, value = 1, height = 2, width = 9, command = lambda: displayfilter("Chips"))
b1.grid(row = 2, column = 0) 
b2 = tk.Radiobutton(gui, text = "Cooldrinks", variable = v, value = 2, height = 2, width = 9, command = lambda: displayfilter("Cooldrinks"))
b2.grid(row = 2, column = 1) 
b3 = tk.Radiobutton(gui, text = "Choclates", variable = v, value = 3, height = 2, width = 9, command = lambda: displayfilter("Chocolates"))
b3.grid(row = 2, column = 2) 
b4 = tk.Radiobutton(gui, text = "Pies", variable = v, value = 4, height = 2, width = 9, command = lambda: displayfilter("Pies"))
b4.grid(row = 3, column = 0) 
b5 = tk.Radiobutton(gui, text = "Fruit", variable = v, value = 5, height = 2, width = 9, command = lambda: displayfilter("Fruit"))
b5.grid(row = 3, column = 1) 
b6 = tk.Radiobutton(gui, text = "Cupcakes", variable = v, value = 6, height = 2, width = 9, command = lambda: displayfilter("Cupcakes"))
b6.grid(row = 3, column = 2) 
b7 = tk.Radiobutton(gui, text = "Veggies", variable = v, value = 7, height = 2, width = 9, command = lambda: displayfilter("Veggies"))
b7.grid(row = 4, column = 1) 

#runs the gui
gui.mainloop()