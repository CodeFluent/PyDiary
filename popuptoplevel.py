#http://zetcode.com/gui/tkinter/drawing/

from Tkinter import *
from tkFileDialog import *

import time
import hashlib



class Intro:
  
    def __init__(self, parent):   
        self.parent = parent        
        self.initUI() #intro message
        self.login() # side for user login

        otherFrame = Frame()
        login_button= Button(otherFrame, borderwidth=4, text="Login", width=10, command=self.gotoWindow)
        login_button.pack()
        otherFrame.pack(side=LEFT, padx=20, pady=20)
        
        bottomFrame = Frame()       
        b1 = Button(bottomFrame,width=10, borderwidth=4, text="New User", command=self.gotoWindow2)
        b1.pack()
        bottomFrame.pack(side=RIGHT, padx=20, pady=20)

        
    def initUI(self):
        
        self.parent.title("PyDiary")        

        first = Label(self.parent, text="Welcome to PyDiary! \nPlease login below or pick New User.")
        first.pack(side=TOP)

    def login(self, **options):

        username= Label(self.parent, text="User name: ").pack(side=TOP, fill=X)

        #compare entry to class3 below
        entry = Entry(self.parent, show="*", **options)
        entry.pack(padx=10, anchor=E, fill=X)

        password= Label(self.parent, text="Password: ").pack(side=TOP, fill=X)

        entry2 = Entry(self.parent,show="*", **options)
        entry2.pack(padx=10, anchor=E, fill=X)
    
    def gotoWindow(self):
        root2= Toplevel(self.parent)
        myGUI=Window1(root2)

    def gotoWindow2(self):
        root3=Toplevel(self.parent)
        myGUI2=Window3(root3)


class Window1:
    def __init__(self, parent):
        self.parent = parent
        self.parent.geometry("500x200+100+200")
        self.parent.title("Text Editor")
        
        self.text = Text(self.parent,width=400, height=400)
        self.text.pack()
        self.saveFile()
        
        menubar = Menu(self.parent)
        filemenu = Menu(menubar, tearoff = 0)
        filemenu.add_command(label="Save", command=self.saveFile)
        filemenu.add_command(label="Open", command=self.openFile)
        filemenu.add_separator()
        menubar.add_cascade(label="File",menu=filemenu)
        self.parent.config(menu=menubar)
        

    def saveFile(self):
        fname="Output.txt"
        now = time.ctime()
        tio = self.text.get(0.0, END)
        tia = tio.encode('base64', 'strict')
        f = open (fname, "a")
        f.write(tia)
        f.write(now)
        f.close()
        
        

    def openFile(self):
       with open("Output.txt", "r") as fname2:
           data=fname2.read()
       data2=data.decode('base64', 'strict')
       self.text.insert(1.0, data2)


class Window3:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Please Enter Information")
        self.parent.geometry("300x150+100+200")

       
        second = Label(self.parent, text="Email Password: ").pack(side=TOP, fill=X)
        hi = Entry(self.parent)
        hi.pack(padx=10, anchor=E, fill=X)
        first = Label(self.parent, text="Email Username: ").pack(side=TOP, fill=X)
        hi2=Entry(self.parent)
        hi2.pack(padx=10, anchor=E, fill=X)

        submit = Button(self.parent, text="Submit", width=10, borderwidth=4).pack(padx=10, pady=10)



    #def new_login(self):
        #pass entrys here and get data
        #use entry data and store in list
        #use http://stackoverflow.com/questions/16417111/how-to-access-members-from-one-class-by-another-class-in-python
        
    #
        

        
        
        
        

  
def main():
    root = Tk()
    start = Intro(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  


