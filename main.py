import tkinter
import os
import sys
import subprocess
import requests
import json
from getshop import list
import datetime
from tkinter import *
import re
def main_ui():
    from getshop import list
    window = Tk() 
    window.geometry('500x500') 
    window.config(bg = "#a1dbcd")
    item_names, ticket_values, image_urls, current_tickets = list()
    current_tickets_str = str(current_tickets[0])
    match = re.search(r'<!-- -->(\d+)<!-- -->', current_tickets_str)
    if match:
        num_tickets = int(match.group(1))
    

    listbox = Listbox(window, selectmode = "multiple") 

    listbox.pack(expand = YES, fill = "both") 

    for each_item in range(len(item_names)): 
        padded_item = '\n     ' + item_names[each_item] + '    |     ' + ticket_values[each_item]
        listbox.insert(END, padded_item) 

        listbox.itemconfig(each_item, 
                 bg = "" if each_item % 2 == 0 else "grey") 

    total_label = Label(window, text="Total: 0")
    total_label.pack()

    def calculate_total():
        selected_indices = listbox.curselection()
        total = 0
        today = datetime.date.today()
        future = datetime.date(2024,8,31)
        diff = future - today
        for index in selected_indices:
            total += int(ticket_values[index].strip(" tickets"))
        total_label.config(text=("Total: " + str(total)+ "\n"+ "Days left: " + str(diff.days))+ "\n"+ "Average tickets per day needed: " + str(((total-num_tickets)/diff.days)) + "\n" + "You are at: " + str(num_tickets) + " tickets")
    

    calculate_button = Button(window, text="Calculate Total", command=calculate_total)
    calculate_button.pack()

    window.mainloop()

main_ui()

