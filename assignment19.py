# question 1

from tkinter import*

root = Tk()
hwL = Label(root, text = "hello world!")
hwL.pack()
exitA = Button

exitA = Button(root,text='exit', width=25,command=root.destroy)

exitA.pack()

root.mainloop()


# question 2

from tkinter import*

root  = Tk()
root.title('hello')

def click():
    rt = Tk()
    labL = Label(rt, text = "HELLO")
    labL.pack()
               
               

texta = Button(root,text="Clickme", width=25,command=click)
texta.pack()

exita = Button(root,text="Exit", width=25,command=root.destroy)
exita.pack()
               

root.mainloop()



# question 3


from tkinter import*

root = Tk()
root.title("frame")

def click():
    rt = Tk()
    labL = Label(rt,text="Hello",bg="red")
    labL.pack()


frame = Frame(root,bg="green")
frame.pack(fill=X)
labL= Label(frame,text = "click on any button",bg="white")
labL.pack()

textb = Button(root,text="click", bg= "yellow", width=25,command=click)
textb.pack()

exitb = Button(root,text="Exit", width=25,command=root.destroy)
exitb.pack()


# question 4

from tkinter import*

root = Tk()
root.title("input")

def click():
    print(input1.get())

input1 = Entry(root)
input1.pack()

a = Button(root,text="clickme",command=click)
a.pack()

b = Button(root,text="exit",width=25,command="exit")
b.pack()
root.mainloop()


