#Number System Converter
#Created on:13/11/2018 9:36 am
#version 1.0.0: Created the basic GUI and Decimal to Binary Converter+Bug Fixes(in the previous code)
    #Known Issues: Quit Button NOT WORKING,
    #Decimal to Binary Window widgets NOT EXPANDING TO FIT ACCORDING TO SCREEN-SIZE


#importing modules

from tkinter import *

#variables

col='gray80'

#Functions

#Window+Widgets for Decimal to Binary Conversion

def D2B():

    def dectobin():
        output_text_widget.delete('1.0', END)
        output_text_widget.insert(END,dec_bin(input_text_widget.get()))
        
    D2Bwin=Tk()
    D2Bwin.title('Decimal to Binary Converter')
        
    frame_outer=Frame(D2Bwin, bg='black')
    frame_outer.pack(fill='both', expand=True, padx=5, pady=5)

    frame_inner=Frame(frame_outer, bg=col)
    frame_inner.pack(fill='both', expand=True, padx=2, pady=2)
        
    l0=Label(frame_inner, font=('arial',20,'italic'), text='Input:', bg=col)
    input_text_widget=Entry(frame_inner)
    execute_widget=Button(frame_inner,text='      Convert      ',command=dectobin)
    l1=Label(frame_inner, font=('arial',20,'italic'), text='Output:', bg=col)
    output_text_widget=Text(frame_inner, width=40, height=1)

    l0.grid(column=0, row=0, pady=5, sticky=S+W)
    input_text_widget.grid(column=0, row=1, columnspan=4, padx=10, pady=10, sticky=N+S+E+W)
    execute_widget.grid(column=4, row=1, padx=5)
    l1.grid(column=0, row=3, pady=5, sticky=S+W)
    output_text_widget.grid(column=0, row=5, columnspan=5,padx=10, pady=10)

    D2Bwin.mainloop()

#Window+Widgets for the program

def Credits():
        
    Cwin=Tk()
    Cwin.title('Credits')
        
    frame_outer=Frame(Cwin, bg='black')
    frame_outer.pack(fill='both', expand=True, padx=5, pady=5)

    frame_inner=Frame(frame_outer, bg=col)
    frame_inner.pack(fill='both', expand=True, padx=2, pady=2)

    l0=Label(frame_inner, font=('arial',25,'bold','underline'), \
                 text='Front-end Designer:', bg=col)
    l0.pack(fill='both', expand=True, padx=50, pady=15)
    l1=Label(frame_inner, font=('arial',20,'italic'), text='Tapajyoti Bose', bg=col)
    l1.pack(fill='both', expand=True, padx=25, pady=15)

    l2=Label(frame_inner, font=('arial',25,'bold','underline'), \
                 text='Back-end Coder:', bg=col)
    l2.pack(fill='both', expand=True, padx=50, pady=15)
    l3=Label(frame_inner, font=('arial',20,'italic'), text='Moumita Das', bg=col)
    l3.pack(fill='both', expand=True, padx=25, pady=15)

    Cwin.mainloop()

#Function for Converting the input in decimal number system to binary number system

def dec_bin(num):

#using the input (Eliminating a few potential errors)
    
    num=str(num)
    num.lstrip()
    num.rstrip()

    #initializing variables
    
    integer=''
    decimal=''
    bin_num=''
    temp_bin=''
    flagdec=False

    #checking whether the input is a number

    for i in num:
        if i=='.' and flagdec==False:
            flagdec=True
        elif (i.isdigit()==False and i!='.') or (i=='.' and flagdec==True):
            return 'Wrong Input. Please check the input again.'

    #separating the integer and float part
    
    for i in range(len(num)):
        if num[i]=='.':
            decimal='0.'+num[i+1:]
            break
        integer+=num[i]
        
    if decimal=='':
        decimal='0.0'
    
    #type-casting into proper types

    decimal=float(decimal)
    
    if integer=='':
        integer=0
    else:
        integer=int(integer)

    #finding the binary of integer part

    while integer>0:
        temp=integer%2
        bin_num=bin_num+str(temp)
        integer=integer//2

    bin_num=bin_num[::-1]
    
    #finding the binary of the float part (upto 4 place)

    for i in range(4):
        decimal*=2
        temp=int(decimal)
        decimal-=temp
        temp_bin+=str(temp)

    temp_bin=temp_bin.rstrip('0')

    #combining the two values and returning

    if bin_num=='':
        bin_num='0'
        
    if temp_bin=='':
        temp_bin='0'

    bin_num=bin_num+'.'+temp_bin

    return (float(bin_num))

#Main window creation and adding details

main_window=Tk()
main_window.title('Number system Converter')

#Drop-down Menu

MainMenu=Menu(main_window)
main_window.config(menu=MainMenu)

submenu=Menu(MainMenu)
MainMenu.add_cascade(label='File', menu=submenu)
submenu.add_cascade(label='Decimal to Binary',command=D2B)
submenu.add_separator()
submenu.add_cascade(label='Credits',command=Credits)
submenu.add_separator()
submenu.add_cascade(label='Quit',command=main_window.quit)

#Help (Start-up Window)

frame_outer=Frame(main_window, bg='black')
frame_outer.pack(fill='both', expand=True, padx=5, pady=5)

frame_inner=Frame(frame_outer, bg=col)
frame_inner.pack(fill='both', expand=True, padx=2, pady=2)

l0=Label(frame_inner, text='', bg=col)
l1=Label(frame_inner, font=('arial',25,'bold','underline'), \
         text='WELCOME TO THE NUMBER SYSTEM CONVERTER:', bg=col)
l2=Label(frame_inner, font=('arial',25,'bold','italic'), \
         text='=======================================================', bg=col)
l3=Label(frame_inner, text='', bg=col)
l4=Label(frame_inner, font=('arial',20), bg=col, \
         text='You can select conversion systems from the \'File\' Menu in the top drop-down menu')
l5=Label(frame_inner, text='', bg=col)
l6=Label(frame_inner, font=('arial',20), bg=col, \
         text='Hope you enjoy the program!')

l0.pack(fill='both', expand=True, padx=15)
l1.pack(fill='both', expand=True, padx=15)
l2.pack(fill='both', expand=True, padx=15)
l3.pack(fill='both', expand=True, padx=15)
l4.pack(fill='both', expand=True, padx=15)
l5.pack(fill='both', expand=True, padx=15)
l6.pack(fill='both', expand=True, padx=15, pady=25)

#mainloop

main_window.mainloop()
