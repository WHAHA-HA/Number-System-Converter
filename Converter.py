#Number System Converter

#Created on: 13/11/2018 9:36 am
#version 1.0.0: Created the basic GUI and Decimal to Binary Converter+Bug Fixes(in the previous code)
    #Known Issues: Quit Button NOT WORKING,
    #Decimal to Binary Window widgets NOT EXPANDING TO FIT ACCORDING TO SCREEN-SIZE

#version 1.0.1: Fixed: Decimal to Binary Window widgets NOT EXPANDING TO FIT ACCORDING TO SCREEN-SIZE
                #Updated the Interface
    #Known Issues: Quit Button NOT WORKING
    #Updated on: 25/11/2018 8:48 am

#version 1.0.2: Added Binary to Octal Function
    #Known Issues: Quit Button NOT WORKING
    #Updated on: 25/11/2018 9:16 am

#version 1.0.3: Added Binary to Octal Converter
    #Known Issues: Quit Button NOT WORKING
    #Updated on: 25/11/2018 9:22 am

#version 1.0.4: Added Decimal to Hexadecimal Function
    #Known Issues: Quit Button NOT WORKING
    #Updated on: 25/11/2018 9:26 am

#version 1.0.5: Fixed: Quit Button NOT WORKING (Outside editor ONLY)
    #Updated on: 27/11/2018 9:55 pm

#version 1.0.6: Added Decimal to Hexadecimal Converter
    #Updated on: 30/11/2018 9:41 pm

#version 1.0.7: Added Binary to Decimal Function
    #Updated on: 02/12/2018 1:49 pm


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

    f1=Frame(frame_inner, bg=col)
    f2=Frame(frame_inner, bg=col)
    f3=Frame(frame_inner, bg=col)
    f4=Frame(frame_inner, bg=col)

    f1.pack(fill='both', expand=True)
    f2.pack(fill='both', expand=True)
    f3.pack(fill='both', expand=True)
    f4.pack(fill='both', expand=True)
    
    l0=Label(f1, font=('arial',25,'bold'), text='Input:', bg=col)
    input_text_widget=Entry(f2)
    execute_widget=Button(f2,text='    Convert   ',font=('arial',15,'bold'),command=dectobin)
    l1=Label(f3, font=('arial',25,'bold'), text='Output:', bg=col)
    output_text_widget=Text(f4, width=45, height=1)

    l0.pack(side=LEFT, padx=10, pady=5, fill=BOTH)
    input_text_widget.pack(side=LEFT, padx=10, pady=10, fill=BOTH)
    execute_widget.pack(side=LEFT, padx=5, fill=BOTH)
    l1.pack(side=LEFT, padx=5, fill=BOTH)
    output_text_widget.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

    D2Bwin.mainloop()

#Window+Widgets for Binary to Octal Conversion

def B2O():

    def bintooct():
        output_text_widget.delete('1.0', END)
        output_text_widget.insert(END,bin_oct(input_text_widget.get()))
        
    B2Owin=Tk()
    B2Owin.title('Binary to Octal Converter')
        
    frame_outer=Frame(B2Owin, bg='black')
    frame_outer.pack(fill='both', expand=True, padx=5, pady=5)

    frame_inner=Frame(frame_outer, bg=col)
    frame_inner.pack(fill='both', expand=True, padx=2, pady=2)

    f1=Frame(frame_inner, bg=col)
    f2=Frame(frame_inner, bg=col)
    f3=Frame(frame_inner, bg=col)
    f4=Frame(frame_inner, bg=col)

    f1.pack(fill='both', expand=True)
    f2.pack(fill='both', expand=True)
    f3.pack(fill='both', expand=True)
    f4.pack(fill='both', expand=True)
    
    l0=Label(f1, font=('arial',25,'bold'), text='Input:', bg=col)
    input_text_widget=Entry(f2)
    execute_widget=Button(f2,text='    Convert   ',font=('arial',15,'bold'),command=bintooct)
    l1=Label(f3, font=('arial',25,'bold'), text='Output:', bg=col)
    output_text_widget=Text(f4, width=45, height=1)

    l0.pack(side=LEFT, padx=10, pady=5, fill=BOTH)
    input_text_widget.pack(side=LEFT, padx=10, pady=10, fill=BOTH)
    execute_widget.pack(side=LEFT, padx=5, fill=BOTH)
    l1.pack(side=LEFT, padx=5, fill=BOTH)
    output_text_widget.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

    B2Owin.mainloop()

#Window+Widgets for Binary to Hexadecimal Conversion

def B2H():

    def bintohex():
        output_text_widget.delete('1.0', END)
        output_text_widget.insert(END,bin_hex(input_text_widget.get()))
        
    B2Hwin=Tk()
    B2Hwin.title('Binary to Hexadecimal Converter')
        
    frame_outer=Frame(B2Hwin, bg='black')
    frame_outer.pack(fill='both', expand=True, padx=5, pady=5)

    frame_inner=Frame(frame_outer, bg=col)
    frame_inner.pack(fill='both', expand=True, padx=2, pady=2)

    f1=Frame(frame_inner, bg=col)
    f2=Frame(frame_inner, bg=col)
    f3=Frame(frame_inner, bg=col)
    f4=Frame(frame_inner, bg=col)

    f1.pack(fill='both', expand=True)
    f2.pack(fill='both', expand=True)
    f3.pack(fill='both', expand=True)
    f4.pack(fill='both', expand=True)
    
    l0=Label(f1, font=('arial',25,'bold'), text='Input:', bg=col)
    input_text_widget=Entry(f2)
    execute_widget=Button(f2,text='    Convert   ',font=('arial',15,'bold'),command=bintohex)
    l1=Label(f3, font=('arial',25,'bold'), text='Output:', bg=col)
    output_text_widget=Text(f4, width=45, height=1)

    l0.pack(side=LEFT, padx=10, pady=5, fill=BOTH)
    input_text_widget.pack(side=LEFT, padx=10, pady=10, fill=BOTH)
    execute_widget.pack(side=LEFT, padx=5, fill=BOTH)
    l1.pack(side=LEFT, padx=5, fill=BOTH)
    output_text_widget.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

    B2Hwin.mainloop()

#Window+Widgets for Decimal to Octal Conversion

def D2O():

    def dectooct():
        output_text_widget.delete('1.0', END)
        output_text_widget.insert(END,bin_oct(dec_bin(input_text_widget.get())))
        
    D2Owin=Tk()
    D2Owin.title('Decimal to Octal Converter')
        
    frame_outer=Frame(D2Owin, bg='black')
    frame_outer.pack(fill='both', expand=True, padx=5, pady=5)

    frame_inner=Frame(frame_outer, bg=col)
    frame_inner.pack(fill='both', expand=True, padx=2, pady=2)

    f1=Frame(frame_inner, bg=col)
    f2=Frame(frame_inner, bg=col)
    f3=Frame(frame_inner, bg=col)
    f4=Frame(frame_inner, bg=col)

    f1.pack(fill='both', expand=True)
    f2.pack(fill='both', expand=True)
    f3.pack(fill='both', expand=True)
    f4.pack(fill='both', expand=True)
    
    l0=Label(f1, font=('arial',25,'bold'), text='Input:', bg=col)
    input_text_widget=Entry(f2)
    execute_widget=Button(f2,text='    Convert   ',font=('arial',15,'bold'),command=dectooct)
    l1=Label(f3, font=('arial',25,'bold'), text='Output:', bg=col)
    output_text_widget=Text(f4, width=45, height=1)

    l0.pack(side=LEFT, padx=10, pady=5, fill=BOTH)
    input_text_widget.pack(side=LEFT, padx=10, pady=10, fill=BOTH)
    execute_widget.pack(side=LEFT, padx=5, fill=BOTH)
    l1.pack(side=LEFT, padx=5, fill=BOTH)
    output_text_widget.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

    D2Owin.mainloop()

#Window+Widgets for Decimal to Hexadecimal Conversion

def D2H():

    def dectohex():
        output_text_widget.delete('1.0', END)
        output_text_widget.insert(END,bin_hex(dec_bin(input_text_widget.get())))
        
    D2Hwin=Tk()
    D2Hwin.title('Decimal to Hexadecimal Converter')
        
    frame_outer=Frame(D2Hwin, bg='black')
    frame_outer.pack(fill='both', expand=True, padx=5, pady=5)

    frame_inner=Frame(frame_outer, bg=col)
    frame_inner.pack(fill='both', expand=True, padx=2, pady=2)

    f1=Frame(frame_inner, bg=col)
    f2=Frame(frame_inner, bg=col)
    f3=Frame(frame_inner, bg=col)
    f4=Frame(frame_inner, bg=col)

    f1.pack(fill='both', expand=True)
    f2.pack(fill='both', expand=True)
    f3.pack(fill='both', expand=True)
    f4.pack(fill='both', expand=True)
    
    l0=Label(f1, font=('arial',25,'bold'), text='Input:', bg=col)
    input_text_widget=Entry(f2)
    execute_widget=Button(f2,text='    Convert   ',font=('arial',15,'bold'),command=dectohex)
    l1=Label(f3, font=('arial',25,'bold'), text='Output:', bg=col)
    output_text_widget=Text(f4, width=45, height=1)

    l0.pack(side=LEFT, padx=10, pady=5, fill=BOTH)
    input_text_widget.pack(side=LEFT, padx=10, pady=10, fill=BOTH)
    execute_widget.pack(side=LEFT, padx=5, fill=BOTH)
    l1.pack(side=LEFT, padx=5, fill=BOTH)
    output_text_widget.pack(side=LEFT, fill=BOTH, padx=10, pady=10)

    D2Hwin.mainloop()

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

#Function for converting Binary to Octal

def bin_oct(num):

    #using the input (Eliminating a few potential errors)
    
    num=str(num)
    num.lstrip()
    num.rstrip()

    #initializing variables set 1
    
    octal=''
    flagbin=False
    integer=''
    decimal=''

    #defining the number mapping
    
    NumMap={'000':'0','001':'1','010':'2','011':'3','100':'4','101':'5','110':'6','111':'7'}

    #checking whether the input is a number

    for i in num:
        if i=='.' and flagbin==False:
            flagbin=True
        elif ((i not in ('0','1')) and i!='.') or (i=='.' and flagbin==True):
            return 'Wrong Input. Please check the input again.'

    #separating the integer and float part
    
    for i in range(len(num)):
        if num[i]=='.':
            decimal=num[i+1:]
            break
        integer+=num[i]
        
    if decimal=='':
        decimal='0'

    #initializing variables set 2

    end_marker=len(integer)
    begining_marker=len(integer)
        
    #slicing out 3 digits and geting the corresponding map

    while end_marker>0:
        begining_marker-=3
        if begining_marker<0:
            begining_marker=0
        sliced=num[begining_marker:end_marker]
        while len(sliced)<3:
            sliced='0'+sliced
        octal=NumMap[sliced]+octal
        end_marker=begining_marker

    #stripping the 0's to the left and returning 0 if empty

    octal=octal.lstrip('0')
    if octal=='':
        octal='0'

    #differenciating between float and integer part

    octal=octal+'.'

    #initializing variables set 2

    end_marker=0
    begining_marker=0
    dec_len=len(decimal)

    #slicing out 3 digits and geting the corresponding map

    while begining_marker<dec_len:
        end_marker+=3
        if begining_marker>dec_len:
            begining_marker=dec_len
        sliced=decimal[begining_marker:end_marker]
        while len(sliced)<3:
            sliced=sliced+'0'
        octal=octal+NumMap[sliced]
        begining_marker=end_marker

    #returning the result

    return octal

#Function for converting Binary to Hexadecimal

def bin_hex(num):

    #using the input (Eliminating a few potential errors)
    
    num=str(num)
    num.lstrip()
    num.rstrip()

    #initializing variables set 1
    
    hexadecimal=''
    flagbin=False
    integer=''
    decimal=''

    #defining the number mapping
    
    NumMap={'0000':'0','0001':'1','0010':'2','0011':'3','0100':'4','0101':'5','0110':'6','0111':'7',\
            '1000':'8','1001':'9','1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F'}

    #checking whether the input is a number

    for i in num:
        if i=='.' and flagbin==False:
            flagbin=True
        elif ((i not in ('0','1')) and i!='.') or (i=='.' and flagbin==True):
            return 'Wrong Input. Please check the input again.'

    #separating the integer and float part
    
    for i in range(len(num)):
        if num[i]=='.':
            decimal=num[i+1:]
            break
        integer+=num[i]
        
    if decimal=='':
        decimal='0'

    #initializing variables set 2

    end_marker=len(integer)
    begining_marker=len(integer)
        
    #slicing out 4 digits and geting the corresponding map

    while end_marker>0:
        begining_marker-=4
        if begining_marker<0:
            begining_marker=0
        sliced=num[begining_marker:end_marker]
        while len(sliced)<4:
            sliced='0'+sliced
        hexadecimal=NumMap[sliced]+hexadecimal
        end_marker=begining_marker

    #stripping the 0's to the left and returning 0 if empty

    hexadecimal=hexadecimal.lstrip('0')
    if hexadecimal=='':
        hexadecimal='0'

    #differenciating between float and integer part

    hexadecimal=hexadecimal+'.'

    #initializing variables set 2

    end_marker=0
    begining_marker=0
    dec_len=len(decimal)

    #slicing out 4 digits and geting the corresponding map

    while begining_marker<dec_len:
        end_marker+=4
        if begining_marker>dec_len:
            begining_marker=dec_len
        sliced=decimal[begining_marker:end_marker]
        while len(sliced)<4:
            sliced=sliced+'0'
        hexadecimal=hexadecimal+NumMap[sliced]
        begining_marker=end_marker

    #returning the result

    return hexadecimal

#Function for Converting Binary to Decimal

def bin_dec(num):

    #using the input (Eliminating a few potential errors)
    
    num=str(num)
    num.lstrip()
    num.rstrip()

    #initializing variables
    
    integer=''
    decimal=''
    dec=0
    temp_bin=''
    flagdec=False
    multiplier_int=1
    multiplier_dec=0.5

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
    
    if integer=='':
        integer='0'

    #finding the integer of integer part

    for i in range(-1,-(len(integer))-1,-1):
        dec+=int(integer[i])*multiplier_int
        multiplier_int*=2        
    
    #finding the decimal of the float part

    for i in range(2,len(decimal)):
        dec+=int(decimal[i])*multiplier_dec
        multiplier_dec/=2 

    return (dec)


#Main window creation and adding details

main_window=Tk()
main_window.title('Number system Converter')

#Drop-down Menu

MainMenu=Menu(main_window)
main_window.config(menu=MainMenu)

submenu=Menu(MainMenu)
MainMenu.add_cascade(label='File', menu=submenu)
submenu.add_cascade(label='Decimal to Binary',command=D2B)
submenu.add_cascade(label='Decimal to Octal',command=D2O)
submenu.add_cascade(label='Decimal to Hexadecimal',command=D2H)
submenu.add_cascade(label='Binary to Octal',command=B2O)
submenu.add_cascade(label='Binary to Hexadecimal',command=B2H)
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
