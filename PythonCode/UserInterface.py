from tkinter import ttk
import screen, os, browser
from tkinter import * 

OutputPath = (os.getcwd()).replace("PythonCode","")+"/UserAudios"
generalPath = (os.getcwd()).replace("PythonCode","")

def findCoor(second):
    global X,Y
    Xcord,Ycord = screen.findPosition(second)
    X.delete(0,END)
    Y.delete(0,END)
    X.insert(0,Xcord)
    Y.insert(0,Ycord)

def finderWindow():
    global sbt, X, Y
    global Xtext, Ytext
    ModeChoice = LabelFrame(sbt,text=" <---| Find Position |---> ",bg="purple")
    ModeChoice.pack(pady = 25, padx = 25)

    Xtext = Label(ModeChoice, text="X coordinate =", bg="purple", fg="black",font=('Helvetica',11,"bold"))
    Xtext.grid(row=0,column=0,columnspan=1,rowspan=1, pady=10,padx=10,ipady=10)
    X = Entry(ModeChoice, width= 30, bg="gray", fg="white", borderwidth=5,font=('Helvetica',11))
    X.grid(row=0,column=1,columnspan=1,rowspan=1, pady=10,padx=10,ipady=10)
    
    Ytext = Label(ModeChoice, text="Y coordinate =", bg="purple", fg="black",font=('Helvetica',11,"bold"))
    Ytext.grid(row=1,column=0,columnspan=1,rowspan=1, pady=10,padx=10,ipady=10)
    Y = Entry(ModeChoice, width= 30, bg="gray", fg="white", borderwidth=5,font=('Helvetica',11))
    Y.grid(row=1,column=1,columnspan=1,rowspan=1, pady=10,padx=10,ipady=10)

    second = Scale(ModeChoice, from_=3, to=15, bg="purple", orient=HORIZONTAL,borderwidth=0)
    second.grid(row=2,column=0,columnspan=1,rowspan=1, pady=10,padx=10,ipady=10)

    generate = Button(ModeChoice, text= "Start Countdown", bg="black",fg="white", pady =25, padx = 25 ,command = lambda:findCoor(second.get()))
    generate.grid(row=2,column=1,columnspan=1,rowspan=1, pady=7,padx=5) 

def homeWindow():
    global home,acy
    
    welcome = Label(home, bg= "gray",text="[Welcome to Screen Position Finder]",font=('Helvetica',11,"bold"))
    welcome.grid(row=0,column=0,columnspan=5,rowspan=1, pady=2,padx=2) 
    welcome2 = Label(home, bg= "gray",text="-Created by ACY-",font=('Helvetica',8,"bold"))
    welcome2.grid(row=2,column=2,columnspan=1,rowspan=1, pady=2,padx=2) 
    photo = Button(home, bg= "gray",image=acy,borderwidth=0,command=lambda:browser.openURL("https://youtu.be/dQw4w9WgXcQ"))
    photo.grid(row=1,column=2,columnspan=1,rowspan=1, pady=0,padx=2) 

    Me = LabelFrame(home,text=" <---| Follow Me |---> ",bg="gray")
    Me.grid(row=3,column=0,columnspan=5,rowspan=1, pady=10,padx=5)

    Instagram = Button(Me, text= "My Instagram", bg="purple", pady =25, padx = 25 ,command = lambda:browser.openURL("https://www.instagram.com/atcan_ymc/?hl=en"))
    Instagram.grid(row=0,column=0,columnspan=1,rowspan=1, pady=7,padx=5) 

    LinkedIn = Button(Me, text= "My LinkedIn",fg="white", bg="blue", pady =25, padx = 25 ,command = lambda:browser.openURL("https://tr.linkedin.com/in/ata-can-yaymac%C4%B1"))
    LinkedIn.grid(row=0,column=1,columnspan=1,rowspan=1, pady=7,padx=5) 

    Github = Button(Me, text= " My Github ", fg="white", bg="black", pady =25, padx = 25 ,command = lambda:browser.openURL("github.com"))
    Github.grid(row=0,column=2,columnspan=1,rowspan=1, pady=7,padx=5) 

    email = Button(Me, text= " My Email  ", bg="white", pady =25, padx = 25 ,command = lambda:browser.openURL("mailto:atacanymc@gmail.com"))
    email.grid(row=0,column=3,columnspan=1,rowspan=1, pady=7,padx=5) 

def rootWindow():
    global root,sbt,home,acy
    root = Tk()
    root.geometry("600x350")
    root.title("Screen Position Finder")
    root.iconbitmap(generalPath+"/ProgramUsage/images/fd_logo.ico")
    acy = PhotoImage(file= generalPath+"/ProgramUsage/images/Acy.png")
    mainBoard = ttk.Notebook(root)
    mainBoard.pack()

    home = Frame(mainBoard, width=600, height=350, bg= "gray")
    home.pack(fill = "both", expand=1)
    homeWindow()

    sbt = Frame(mainBoard, width=600, height=350, bg= "purple")
    sbt.pack(fill = "both", expand=1)
    finderWindow()

    mainBoard.add(home, text= "< Home >")
    mainBoard.add(sbt, text= "< Position Screenshot >")

    root.mainloop()

rootWindow()
