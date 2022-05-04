from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk, Image
import tkinter.font as font
import os
gui = Tk()

gui.title("UOH Enigma Machine")
gui.configure(background="white")

#logotitle
image = ImageTk.PhotoImage(file="UniversityLogo.gif")
Label(gui, image=image, background='white').pack(padx=10, pady=10, side=TOP)
Label(gui, text="Enigma Machine Simulator", font=font.Font(family='Rage Italic', size=30, weight='bold'), background='white').pack(padx=10, pady=10, side=TOP)

#Rotor Labels
rotor_frame = Frame(gui, borderwidth=2, relief=FLAT, background='white',highlightbackground='brown',bd=5,highlightcolor='red',highlightthickness=4)
rotor_frame.pack(side=TOP,padx=10,pady=10)

rotor_label1=Label(rotor_frame,text='Rotor I',font=font.Font(family='newspaper', size=15, weight='bold'), fg='#DC3C3C', padx=10, pady=5, borderwidth=0, background='white')
rotor_label1.grid(row=0,column=0)
rotor_label2=Label(rotor_frame,text='Rotor II',font=font.Font(family='newspaper', size=15, weight='bold'), fg='#DC3C3C', padx=10, pady=5, borderwidth=0, background='white')
rotor_label2.grid(row=0,column=1)
rotor_label3=Label(rotor_frame,text='Rotor III',font=font.Font(family='newspaper', size=15, weight='bold'), fg='#DC3C3C', padx=10, pady=5, borderwidth=0, background='white')
rotor_label3.grid(row=0,column=2)



def slider_1(x):
	x=int(x)
	alphabet_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	label_1.configure(text='position : {}'.format(alphabet_list[x]))


def slider_2(x):
	x=int(x)
	alphabet_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	label_2.configure(text='position : {}'.format(alphabet_list[x]))

def slider_3(x):
	x=int(x)
	alphabet_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	label_3.configure(text='position : {}'.format(alphabet_list[x]))

	
#Sliders
rotor1_value = DoubleVar()
scale_1 = Scale(rotor_frame, from_=0, to=25, variable = rotor1_value, showvalue=0, command=slider_1,  length= 200, background='white',cursor='dot',troughcolor='#A2DFFF',bd=0,bg='pink',)
scale_1.grid(row=1, column=0, padx=60, pady=10)
rotor2_value = DoubleVar()
scale_2 = Scale(rotor_frame, from_=0, to=25, variable = rotor2_value, showvalue=0, command=slider_2,  length= 200, background='white',cursor='dot',troughcolor='#A2DFFF',bd=0,bg='pink')
scale_2.grid(row=1, column=1, padx=60, pady=10)
rotor3_value = DoubleVar()
scale_3 = Scale(rotor_frame, from_=0, to=25, variable = rotor3_value, showvalue=0, command=slider_3, length= 200, background='white',cursor='dot',troughcolor='#A2DFFF',bd=0,bg='pink' )
scale_3.grid(row=1, column=2, padx=60, pady=10)

#Slider_Label
label_1 = Label(rotor_frame)
label_1.grid(row=2, column=0)
label_2 = Label(rotor_frame)
label_2.grid(row=2, column=1)
label_3 = Label(rotor_frame)
label_3.grid(row=2, column=2)	

label_1.configure(text='position : A',font=font.Font(family='Gabriola', size=18),fg='#DC3C3C',background='white')
label_2.configure(text='position : A',font=font.Font(family='Gabriola', size=18),fg='#DC3C3C',background='white')
label_3.configure(text='position : A',font=font.Font(family='Gabriola', size=18),fg='#DC3C3C',background='white')

# Config of Enigma

alphabet_list=['A','B','C','D','E','F','G','H','I','J','K','L',
              'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
rotor1_list=['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y',
            'H','X','U','S','P','A','I','B','R','C','J']
rotor2_list=['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M',
            'C','Q','G','Z','N','P','Y','F','V','O','E']
rotor3_list=['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y',
            'E','I','W','G','A','K','M','U','S','Q','O']

reflectorB=['Y','R','U','H','Q','S','L','D','P','X','N',
            'G','O','K','M','I','E','B','F','Z','C','W','V','J','A','T']
PlugBoard1=['G','V','U','R','P',
         	'S','L','W','I','H']
PlugBoard2=['A','C','D','X','N',
         	'T','F','M','B','O']
reverse_direction=False
count_fast=0
count_medium=0
count_fast1=0
count_medium1=0
count_slow1=0
rtRotors=[]
helpStatus = False
finalmsg=[]
exportCounter=0
exportRotors=[]

#Custom PlugBoard
def plugboardGUI():
        plugGUI = Tk()
        plugGUI.configure(background="white",highlightbackground='red',bd=5,highlightthickness=3)
        global PlugBoard1
        global PlugBoard2
        PlugBoard1 = []
        PlugBoard2 = []
        alphabet_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        buttonsPB1 = []
        buttonsPB2 = []

        def plugset1(index):
                count = len(PlugBoard1)
                if(count < 10):
                        buttonsPB1[index].config(state="disabled",background='pink')
                        PlugBoard1.append(alphabet_list[index])
                        print("ARRAY FOR PLUGBOARD 1 ",PlugBoard1)
                if(count == 10):
                        print("ARRAY FOR PLUGBOARD 1 ",PlugBoard1)
 

        def plugset2(index):
                count = len(PlugBoard2)
                if(count<10):
                        buttonsPB2[index].config(state="disabled",background='pink')
                        PlugBoard2.append(alphabet_list[index])
                        print("ARRAY FOR PLUGBOARD 2 ",PlugBoard2)
                if(count == 10):
                        print("ARRAY FOR PLUGBOARD 2 ",PlugBoard2)



        Label(plugGUI,background="white").pack(padx=10, pady=10, side=TOP)
        Label(plugGUI, text="PlugBoard 1", font=("Pristina", 30), background='white').pack(padx=20, pady=0, side=TOP)
        #TOP FRAME
        main_frame = Frame(plugGUI, borderwidth=0, relief=FLAT, background='white',highlightbackground='blue',bd=5,highlightthickness=2)
        main_frame.pack(side=TOP, padx=10, pady=0)
        for index in range(0,26):
                buttonPB1 = Button(main_frame, bg="White", text='{}'.format(alphabet_list[index]), width=5,command=lambda index=index:plugset1(index))
                buttonPB1.grid(row=0,column=index, padx=2, pady=7)
                buttonsPB1.append(buttonPB1)
                
        for index in range(0,26):
                buttonPB2 = Button(main_frame, bg="White", text='{}'.format(alphabet_list[index]), width=5,command=lambda index=index: plugset2(index))
                buttonPB2.grid(row=1,column=index, padx=2, pady=7)
                buttonsPB2.append(buttonPB2)
        Label(plugGUI, text="PlugBoard 2",font=("Pristina", 30), background='white').pack(padx=20, pady=2, side=TOP)
        Label(plugGUI,background="white").pack(padx=10, pady=0, side=TOP)
        #Intro
        introduction = Label(plugGUI, text = "Project By \"Faaiz Ali Shah Syed\"", background='white',font=("Gabriola", 30))
        introduction.pack(side = BOTTOM, padx=10, pady=10)
                          
        plugGUI.mainloop()
        

def rotor_connections(l,m,n):
    global rotor1_list,rotor1listWorking,rotor2_list,rotor2listWorking,rotor3_list,rotor3listWorking, count_fast1, count_medium1, count_slow1
    count_fast1=int(rotor3_value.get())
    count_medium1=int(rotor2_value.get())
    count_slow1=int(rotor1_value.get())
    for e in range(l-1):
        rotor1_list.append(rotor1_list[0])
        del rotor1_list[0]
    rotor1listWorking = rotor1_list
    rotor1_list=['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y',
            'H','X','U','S','P','A','I','B','R','C','J']
    for f in range(m-1):
        rotor2_list.append(rotor2_list[0])
        del rotor2_list[0]
    rotor2listWorking = rotor2_list
    rotor2_list = ['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M',
            'C','Q','G','Z','N','P','Y','F','V','O','E']
    for g in range(n-1):
        rotor3_list.append(rotor3_list[0])
        del rotor3_list[0]   
    rotor3listWorking = rotor3_list
    rotor3_list=['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y',
            'E','I','W','G','A','K','M','U','S','Q','O']

def shift():
    global count_fast,count_medium,count_fast1, count_medium1, count_slow1, rotor1listWorking,rotor2listWorking,rotor3listWorking
    #fast rotor
    rotor3listWorking.append(rotor3listWorking[0])
    del rotor3listWorking[0]
    count_fast+=1
   
    count_fast1+=1
    if count_fast1 == 26:
        scale_3.set(0)
        count_fast1 = 0
        count_medium1 += 1
        if count_medium1 == 26:
            scale_2.set(0)
            count_medium1 = 0
            count_medium+=1
            count_slow1+=1
            if count_slow1 == 26:
                scale_1.set(0)
                count_slow1 = 0
            else:
                scale_1.set(count_slow1)
        else:
            scale_2.set(count_medium1)
    else:
        scale_3.set(count_fast1)
        
                
    if count_fast%26==0:
        #middle rotor
        rotor2listWorking.append(rotor2listWorking[0])
        del rotor2listWorking[0]
        
    if count_medium%26==0 and count_medium!=0:
        #slow rotor
        rotor1listWorking.append(rotor1listWorking[0])
        del rotor1listWorking[0]

def reflector(msg,reflect=reflectorB):
    postreflect=[]
    
    for char in msg:
        if char in alphabet_list:
            changedletter=reflect[alphabet_list.index(char)]
            postreflect.append(changedletter)
    rotor_1(postreflect)

def rotor_1(msg):
    global reverse_direction
    post_rotor_1=[]
    
    if reverse_direction==False:
        for char in msg:
            
            if char in alphabet_list:
                changedletter=rotor1listWorking[alphabet_list.index(char)]
                post_rotor_1.append(changedletter)   
                 
        reverse_direction=True
        reflector(post_rotor_1)        
    else:
        for char in msg:
            if char in alphabet_list:
                changedletter=alphabet_list[rotor1listWorking.index(char)]
                post_rotor_1.append(changedletter)    
        rotor_2(post_rotor_1)
        
def rotor_2(msg):
    global reverse_direction
    post_rotor_2=[]
    
    if reverse_direction==False:
        for char in msg:
            if char in alphabet_list:
                changedletter=rotor2listWorking[alphabet_list.index(char)]
                post_rotor_2.append(changedletter)   
 
        rotor_1(post_rotor_2)        
    else:
        for char in msg:       
            if char in alphabet_list:
                changedletter=alphabet_list[rotor2listWorking.index(char)]
                post_rotor_2.append(changedletter)    
        rotor_3(post_rotor_2)

def rotor_3(msg):
    global reverse_direction
    post_rotor_3=[]
    
    if reverse_direction==False:
        for char in msg:
            test=[]
            if char in alphabet_list:
                changedletter=rotor3listWorking[alphabet_list.index(char)]
                post_rotor_3.append(changedletter)
                test.append(post_rotor_3[-1])
                rotor_2(test)
                shift()        
    
    else:
        for char in msg:
            if char in alphabet_list:
                changedletter=alphabet_list[rotor3listWorking.index(char)]
                post_rotor_3.append(changedletter)
        plugboard(post_rotor_3)


def plugboard(msg):
    global reverse_direction, finalmsg
    global PlugBoard1
    global PlugBoard2
    plugboard1=PlugBoard1
    plugboard2=PlugBoard2
    post_PB=[]
    
    for char in msg:
        
        if char in alphabet_list:
            
            if char in plugboard1:
                changedletter=plugboard2[plugboard1.index(char)]
                post_PB.append(changedletter)
            
            elif char in plugboard2:
                changedletter=plugboard1[plugboard2.index(char)]
                post_PB.append(changedletter)
            
            else:
                post_PB.append(char)
                
    
    if reverse_direction==False:
        rotor_3(post_PB)
        print("PlugBoard",post_PB)

    else:
        finalmsg.append(post_PB)
        reverse_direction=False

def code():
    global finalmsg, count_fast, count_medium, exportCounter, exportRotors
    msg= entryvar.get()
    msg= msg.upper()
    rotor_connections(int(rotor1_value.get()) + 1,int(rotor2_value.get()) + 1,int(rotor3_value.get()) + 1)
    exportRotors.append(alphabet_list[int(rotor1_value.get())] + alphabet_list[int(rotor2_value.get())] + alphabet_list[int(rotor3_value.get())])
    
    entry_message=list(msg)
    plugboard(entry_message)
    full_message = [item for sublist in finalmsg for item in sublist]
    output_final=''.join(full_message)
    print("final message", output_final)
    flat_list = []
    finalmsg = []
    print("FASTES ROTOR TURNS: ",count_fast,"MEDIUM ROTOR TURNS: ",count_medium)
    count_fast = 0
    count_medium = 0
    value = StringVar() 
    value.set(output_final)
    output.insert(END, value.get())
    output.see("end")

#text entry label
textLabel = Label(gui, text = "ENTER YOUR PLAIN OR CIPHER TEXT", background='white',font=font.Font(family='newspaper', size=15, weight='bold'))
textLabel.pack()

#text entry
entryvar = StringVar()
entry = Entry(gui, textvariable = entryvar, width=50, background='white')
entry.focus_set()
entry.bind("<Return>", code)
entry.pack(padx=10, pady=10)

#buttons
def clear():
    global exportRotors
    output.delete(0, END)
    entry.delete(0, END)
    exportRotors = []
def export():
    global exportCounter, exportRotors
    exportCounter +=1
    fileNum = str(exportCounter)
    fileName = ("Export"+ fileNum+ ".txt")
    file = open(fileName, "w+") 
    textTuple = output.get(0, END)
    print (textTuple)
    for i in range(0, len(textTuple)):
        file.write(textTuple[i] + " Rotor Settings: [" + exportRotors[i] + "]" + "\r\n")
    file.close() 


#run button
runButton = Button(gui, text="ENCRYPT/DECRYPT", width=20, command=code, background='white',cursor='dot',bd=2,font=("Gabriola",12,'bold'))
runButton.pack()

#output frame
frame2 = Frame(gui, borderwidth=0, relief=FLAT, background='white')
frame2.pack(pady = 5)
output = Listbox(frame2, height=5, width=50, borderwidth=2, background='white',bd=2,highlightcolor='red',highlightthickness=2)
output.pack(side = LEFT, fill = Y, padx=5, pady=5)	


#frame for clear and export buttons layout
frame3 = Frame(gui, borderwidth=0, relief=FLAT, background='white')
frame3.pack(side=TOP, padx=10, pady=0)
clearButton = Button(frame3, text="Clear", width=10, command=clear, background='white')
clearButton.pack(side = LEFT, padx=5, pady=5)
exportButton = Button(frame3, text="Export", width=10, command=export, background='white')
exportButton.pack(side = LEFT, padx=5, pady=5)

#quit button
frame4 = Frame(gui, borderwidth=0, relief=FLAT, background='white')
frame4.pack(side=TOP, padx=10, pady=0)
quitButton = Button(frame4, text="Quit", width=10, command=gui.destroy, background='white')
quitButton.pack(side = LEFT, padx=5, pady=5)
#Plugboard Button
PlugButton = Button(frame4, text="Plugboard", width=10, command=plugboardGUI, background='white')
PlugButton.pack(side = LEFT, padx=5, pady=5)

#Introduction
introduction = Label(gui, text = "Project By Faaiz Ali Shah Syed", background='white',font=font.Font(family='Pristina', size=15, weight='bold'))
introduction.pack(side = BOTTOM, padx=10, pady=10)
gui.mainloop()	
