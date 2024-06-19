import tkinter
import os
import sys
import subprocess
import requests
import json
from getshop import list

from tkinter import *

def main_ui():
    from getshop import list
    window = Tk() 
    window.geometry('500x500') 
    window.config(bg = "#a1dbcd")
    item_names, ticket_values, image_urls = list()
    list = Listbox(window, selectmode = "multiple") 
    
    # Widget expands horizontally and 
    # vertically by assigning both to  
    # fill option 
    list.pack(expand = YES, fill = "both") 
    
    # Taking a list 'x' with the items  
    # as languages 
    
    
    for each_item in range(len(item_names)): 
        padded_item = '\n     ' + item_names[each_item] + '\n'  # Add spaces to the beginning and end
        list.insert(END, padded_item) 
        

        # coloring alternative lines of listbox 
        list.itemconfig(each_item, 
                 bg = "" if each_item % 2 == 0 else "grey") 



    window.mainloop()

main_ui()