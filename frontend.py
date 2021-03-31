import generator
import re
from tkinter import *


def add_part():
    '''
    No return
    When add button is pressed this function adds the decided password type to the display.
    '''
    parts = decision.get() #retrieves the selected password type option
    
    disp.config(state=NORMAL) #allows for editing
    disp.insert(END,parts)
    disp.config(state=DISABLED) #closes the display to editing again

def erase():
    '''
    No return
    Clears the display box.
    Utilizies the same technique for allow then disallowing editing as in add_part
    '''
    disp.config(state=NORMAL)
    disp.delete(1.0,END) #deletes the text from the display
    disp.config(state=DISABLED)

def generate():
    '''
    No return
    This function turns the sequence string into a list of the data types using re.findall.
    It then calls on the Password class to create the password while checking to make sure it
    doesn't violate the limit. Finally it displays the password. 
    '''
    sequence = disp.get("1.0",END)
    sequence = sequence[0:len(sequence)-1] #when using disp.get a '\n' was included on the end which this elminates
    seq = re.findall('[A-Z][^A-Z]*',sequence) #breaks the string into a list at every capital letter
    
    #this block creates the variables necessary to generate and check the password's limit
    count = 0
    limit = limit_val.get() 
    redo = TRUE
    gen = generator.Password(seq,limit)
    password = ''

    '''This conditional makes sure that there aren't more characters than the limit. However, this first conditional only 
    works if every part is a symbol or number because the list used doesn't include one letter words.

    I wanted to make this program so that other lists of words can be used, so I created a seperate 
    conditional that will try to make a password up to a count of 2000 tries. If it doesn't find 
    a combination within those tries it will assume that it cannot and break the while loop.
    '''
    if len(seq) <= int(limit):
        #this loop checks to make sure the password is in the limit and will redo if not
        while redo == TRUE: 
            password = gen.create_password() #creates the password object
            count += 1 
            
            #ends the loop if the password is within the limit
            if int(limit) >= len(password): 
                redo = FALSE
            
            #the second conditional referenced previously
            if count > 2000: 
                password = 'INVALID LIMIT AND SEQUENCE LENGTH COMBO' 
                redo = FALSE
    else:
        password = 'INVALID LIMIT AND SEQUENCE LENGTH COMBO' #error message in place of password if combo doesn't work
    
    #creates password display window
    view = Tk()
    view.title('Password')

    #displays password within password display window
    pass_window = Text(view, height =1,width =len(password))
    pass_window.insert(END,password)
    pass_window.pack()

#creates password creation window
window = Tk()
window.title('Easy to Remember Custom Password')

#creates list for drop down menu
decision = StringVar(window)
choices = ['Word','Number','Symbol']
decision.set('Word') #sets word as the first option

#creates option menu for password selection
drop = OptionMenu(window,decision,*choices)
Label(window,text="Choose Type").grid(row = 1, column =1)
drop.grid(row=2,column=1)

#creates limit entry box
limit_val = StringVar(window)
limit = Entry(window, textvariable = limit_val)
limit.insert(0,'20') #sets default limit of 20
Label(window,text="Optional: Set Limit").grid(row=1, column = 2)
limit.grid(row=2,column =2)

#creates window to display user chosen sequence
disp = Text(window, height=1,width=40)
disp.config(state=DISABLED)
disp.grid(row=0,column=1)

#creates button that uses add_part function
add = Button(window,text='Add',command=add_part)
add.grid(row=2, column = 0)

#creates button that uses erase function
delete = Button(window,text="Delete", command = erase)
delete.grid(row=0, column=2)

#creates button that uses generate function
create = Button(window, text='Create Pasword', command = generate)
create.grid(row=0,column=0)

#keeps the window open
window.mainloop()

