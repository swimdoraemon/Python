from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTK

root = TK()
root.tiltle('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))
image = ImageTK.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root, text="Hey User! Welcome to denomination counter App.", bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo("Alert", "Do you want to caluculate the denomination count?")
    if MsgBox == 'ok':
        topwin()

button1 = Button(root,text="Let's get started!", command=msg, bg='brown', fg='white')
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denomination calucalator")
    top.configure(bg='light grey')
    top.geometry("600x350+50+50")


    label(top, text="Enter total amount", bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg='light grey')


    l1 = Label(top, text="10000", bg='light grey')
    l2 = Label(top, text="5000", bg='light grey')
    l3 = Label(top, text="1000", bg='light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calucalator():
        try:
            global amount



            amount = int(entry.get())

            note2000 = amount // 10000

            amount %= 2000

            note500 = amount // 5000

            amount %= 500

            note100 = amount // 1000

            t1.delete(0, END)

            t2.delete(0, END)

            t3.delete(0, END)
            t1.insert(END, str(note10000))
            t2.insert(END, str(note5000))

            t3.insert(END, str(note1000))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")


    btn = Button(top, text='Caluculate', command=calucalator, bg='brown', fg='white')


    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    
    top.mainloop()
root.mainloop()


    
    


               



               


