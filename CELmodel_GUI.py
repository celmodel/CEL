# -*- coding: utf-8 -*-
"""
Created on Sun May 12 17:38:21 2019

@author: Ragna Kobin
"""

# -*- coding: utf-8 -*-

# python2 vs python3
import csv
import tkinter as tkinter
#import ipywidgets as widgets

data_name=['Exercise name:','Exercie Number:','Number of participant','Exercise time per participant','Real roles','Level 1','Level 2','Level 3','Level 4','Level 5',
           'Private sector','Public sector','Military sector','Academic sector','Mixed sectors','Seminar','Workshop','Table-top','Game','Drill','Functional','Full-scale',
           'Electricity','Natural gas','Liquid fuel','Roads','Phone','Mobile phone','Data and Digital identification','Health','Financial','Heating','Water','Aircraft',
           'Railway','Harbour','Secure Provision','Operate and Maintain','Oversee and Govern','Protect and Defend','Analyze','Collect and Operate','Investigate']
data_list=['ex_na','ex_nr','part','ti_pe','real','l1','l2','l3','l4','l5','sec1','sec2','sec3','sec4','sec5','typ1','typ2','typ3','typ4','typ5','typ6','typ7',
           'ci1','ci2','ci3','ci4','ci5','ci6','ci7','ci8','ci9','ci10','ci11','ci12','ci13','ci14','cat1','cat2','cat3','cat4','cat5','cat6','cat7']
'''
data_name=['Exercie Number:','Exercise name:']
data_list=['ex_nr','ex_na']
'''
data_type=['int','str','int','int','int','int','int','int','int','int','int','int','int','int','int','int','int','int','int','int','int','int','int',
           'int','int','int','int','int','int','int','int','int','int','int','int','int','int','int','int','int','int','int','int']

#print(len(data_name))
#print(len(data_list))

def main():
    # create a main window
    window  = tkinter.Tk() # window is the name of the main window object
    window.title("CEL MODEL Data")
    window.geometry('260x950')
    
    #copy list and create first column in GUI
    #global col1
    col1=list(data_list)
    for i in range(len(col1)):
        # http://effbot.org/tkinterbook/grid.htm
        tkinter.Label(window, text=data_name[i], fg="blue").grid(row=i, sticky="W")
        col1[i] = tkinter.Entry(window,width=5)
        col1[i].grid(column=1, row=i)
        col1[i].focus() # Set focus to entry widget

    #action when button is clicked        
    def clicked():
        #txtval2 = int(ex_nr.get()) * 2
        #txt2.insert(0,txtval2)
        data=[]
        name = col1[0].get()
        # Test to check if 'name' is empty
        if not name:
            name = "Exercise1"
        data.append(name)
        for i in range(1, len(data_list)):
            #print(col1[i].get())
            val = col1[i].get()
            # Test to check if 'val' is empty
            if not val:
                print(f"{col1[i]} is empty")
                val = 0
            # magic!
            data.append(int(val))
        csv_name=f'CEL-{name}.csv'
        #print(csv_name, 'TEKST')
        with open(csv_name, mode='w', newline='') as csv_file:
            #with open('cel_model2.csv', mode='w', newline='') as csv_file:
            cel_model_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            cel_model_writer.writerow(data_list)
            cel_model_writer.writerow(data)

    
    # add a button in the application
    btn = tkinter.Button(window, text="Save exercise data", command=clicked) 
    btn.grid(column=0, row=len(data_list))


    window.mainloop()   # infinite loop used to run the application, wait for an 
                        # event to occur and process the event till the window is
                        # not closed
                            
if __name__ == '__main__':
    main()