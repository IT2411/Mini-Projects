from tkinter import *
from random import *

root = Tk()
root.geometry("700x400")

num = randint(0, 30)

def begin():
    myL.destroy()
    start_button.destroy()
    enter.pack()
    click.pack()
    
def end():
    root.destroy()
    
def check():
    i=enter.get()
    enter.delete(0, END)
    if i.lower()=='q':
        myLA = Label(root, text='Better Luck next time.', font=(20) )
        myLA.pack()
        click.destroy()
        thanks.pack()
    elif i.isnumeric()!=True:
        myLA = Label(root, text='Please enter a number', font=(20))
        myLA.pack()
    elif int(i)>num:
        myLA = Label(root, text='The number is less than ' + i, font=(20))
        myLA.pack()
    elif int(i)<num:
        myLA = Label(root, text='The number is greater than ' + i, font=(20))
        myLA.pack()
    elif int(i)==num:
        myLA = Label(root, text='Congratualtions!!!\n'+str(num)+' is the correct answer!', font=(20))
        myLA.pack()
        click.destroy()
        enter.destroy()
        thanks.pack()
        
intro = '''
Welcome to the guessing game!
The number will between 0 to 30
If you wish to quit type q
All the best!!!
'''
    
myL = Label(root, text=intro, font=('Helvetica 18'))
myL.pack()
enter = Entry(root, font=('Helvetica 18'))
start_button = Button(root, text="Start Game", command=begin, font=('Helvetica 18'))
click = Button(root, text="Enter", command=check, font=('Helvetica 18'))
thanks = Button(root, text="Thank you for playing!", command=end, font=('Helvetica 18'))
start_button.pack()

root.mainloop()