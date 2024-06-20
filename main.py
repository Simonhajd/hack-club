import tkinter
import os
import sys
import subprocess
import requests
import json
import time
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
    print(item_names)
    print(ticket_values)
    current_tickets_str = str(current_tickets[0])
    match = re.search(r'<!-- -->(\d+)<!-- -->', current_tickets_str)
    if match:
        num_tickets = int(match.group(1))
    

    listbox = Listbox(window, selectmode = "multiple") 

    listbox.pack(expand = YES, fill = "both") 
    
    missed_days_label = Label(window, text="Est. days to be missed: ")
    missed_days_label.pack()

    misseddays = Spinbox(window, from_=0, to=365, width=10, relief="sunken", bd=1, bg="white", fg="black", font=("Arial", 12))
    misseddays.pack()
    for each_item in range(len(item_names)): 
        padded_item = '\n     ' + item_names[each_item] + '    |     ' + ticket_values[each_item]
        listbox.insert(END, padded_item) 

        listbox.itemconfig(each_item, 
                 bg = "" if each_item % 2 == 0 else "grey") 

    total_label = Label(window, text="Total: 0")
    total_label.pack()

    def calculate_total():
        selected_indices = listbox.curselection()
        print("Selected: "+str(selected_indices))
        total=0
        missed_days = int(misseddays.get())
        today = datetime.date.today()
        future = datetime.date(2024,8,31)
        diff = future - today
        for i in selected_indices:
            total += int(ticket_values[i].strip(" tickets"))
            print("Selected: "+str(item_names[i])+"| Tickets: "+str(ticket_values[i])+"| Image URL: "+str(image_urls[i]))
        time.sleep(2)
        print(("\n")*100)
        print("Total: "+ str(total))
        print("Num tickets: "+ str(num_tickets))
        print("Difference: "+ str(diff.days))
        print("Missed days: "+ str(missed_days))
        print("-------")
        print("Total: "+ str(diff.days-missed_days))
        
        
        print("Required tickets: "+ str((total-num_tickets)))
        
        total_label.config(text=("Total: " + str(total)+ "\n"+ "Days left: " + str(diff.days))+ "\n"+ "Average tickets per day needed: " + str(((total-num_tickets)/(diff.days-missed_days))) + "\n" + "You are at: " + str(num_tickets) + " tickets")
    

    calculate_button = Button(window, text="Calculate Total", command=calculate_total)
    calculate_button.pack()

    window.mainloop()

main_ui()

