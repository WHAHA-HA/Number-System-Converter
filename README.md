# Number-System-Converter
This repository has been created for a beginner friendly project (Number System Converter: An application which is used to convert the given input in a specified number system to another number system of choice), for learning how to work on github as a team.



The following table shows the list of variables used in the program:

VariableName        Type			  Namespace       Initial value		  Utility
col                 str               global          'gray80'            Stores the colour of the background colour of the windows
D2Bwin              tkinter.Tk        local           -----               Window for the Decimal to Binary converter
Cwin                tkinter.Tk        local           -----               Window for Credits
frame_outer         tkinter.Frame     local           -----               Used to give the effect of border(same for all instance)
frame_inner         tkinter.Frame     local           -----               Used to give the effect of border(same for all instance)
l0,l1,l2...         tkinter.Label     local/global    -----               Text widget(text different for each instance)
input_text_widget   tkinter.Entry     local           -----               Takes the user input
output_text_widget  tkinter.Text      local           -----               Shows the output after conversion
num                 str               local           -----               Number given for conversion(same for all instance)
integer             str to int        local           ''                  Stores the integer part of the num variable
decimal             str to float      local           ''                  Stores the float part of the num variable
bin_num             str to float      local           ''                  Stores the integer part(later float part is concatenated)
temp_bin            str to float      local           ''                  Stores the float part(later concatenated to bin_num)
flagdec             bool              local           False               Checks for appearance of '.' in the num variable
main_window         tkinter.Tk        global          -----               Main(start-up) window
MainMenu            tkinter.Menu      global          -----               Main menu at the top
submenu             tkinter.Menu      global          -----               Submenu of MainMenu
