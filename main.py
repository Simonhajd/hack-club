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
    

    list.pack(expand = YES, fill = "both") 

    
    for each_item in range(len(item_names)): 
        padded_item = '\n     ' + item_names[each_item] + '\n' 
        list.insert(END, padded_item) 
        


        list.itemconfig(each_item, 
                 bg = "" if each_item % 2 == 0 else "grey") 



    window.mainloop()

main_ui()