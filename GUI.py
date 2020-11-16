import tkinter as tk
import Employee_end as Ee
import sys



def command_1(a, b, c):
    global L1, Button_1, Button_2
    if (a and b and c):
        result = Ee.new_user(a, b, c)
        if(result[0]):
            L1 = tk.Label(app, text = result[1], font = ('Helvetica',20,'bold'),bg ='#6dd1e3')
            L1.place(relx = 0.4, rely = 0.6)
            Button_1 = tk.Button(O, text = "< Back", font = ('Helvetica',20,'bold'),bg ='#6dd1e3', command = back)
            Button_1.place(relx = 0.2, rely = 0.8)
            Button_2 = tk.Button(O, text = "Add one more >", font = ('Helvetica',20,'bold'),bg ='#6dd1e3', command = new_user)
            Button_2.place(relx = 0.6, rely = 0.8)

def back():
    try:
        L1.destroy()
        Button_1.destroy()
        Button_2.destroy()
    finally:
        O.destroy()
        Main_Menu()

def new_user():
    global O, F
    if(Mm):
        Mm.destroy()
    elif(F):
        F.destroy()
    O = tk.Frame(app, height = 720, width = 1080)
    O.place(relx = 0.1, rely = 0.1)
    F = tk.LabelFrame(O,
                    text = 'New User',
                    font = ('Helvetica',20,'bold'),
                    bg ='#6dd1e3',
                    height = 720//2,
                    width = 1280//2,
                    borderwidth = 20,
                    relief = 'groove')
    F.place(relx = 0.25, rely = 0.2)
    name_label = tk.Label(F, text = 'Enter Name')
    email_label = tk.Label(F, text = 'Enter Email')
    phone_label = tk.Label(F, text = 'Enter Phone')
    name = tk.Entry(F)
    email = tk.Entry(F)
    phone = tk.Entry(F)
    B11 = tk.Button(F, text = 'Create Account >', font = 'Helvetica', command = lambda: command_1(name.get(), phone.get(), email.get()))
    B12 = tk.Button(F, text = '< Back', font = 'Helvetica', command  = back)
    name_label.place(relx = 0.2, rely = 0.2)
    email_label.place(relx = 0.2, rely = 0.4)
    phone_label.place(relx = 0.2, rely = 0.6)
    B12.place(relx = 0.2, rely = 0.8)
    name.place(relx = 0.4, rely = 0.2)
    email.place(relx = 0.4, rely = 0.4)
    phone.place(relx = 0.4, rely = 0.6)
    B11.place(relx = 0.4, rely = 0.8)
    

app = tk.Tk()
app.title('Bank Management')
app.geometry('1280x720')
app.minsize(1280, 720)
def Main_Menu():
    global Mm 
    Mm = tk.LabelFrame(app,
                       text = 'Main Menu',
                       font = ('Helvetica',20,'bold'),
                       bg ='#6dd1e3',
                       height = 720//2,
                       width = 1280//2,
                       borderwidth = 20,
                       relief = 'groove')
    Mm.place(relx = 0.25, rely = 0.2, relwidth = 0.5)

    B1 = tk.Button(Mm, text = 'New User', font = 'Helvetica', bg = 'yellow', command = new_user)
    B1.place(relx = 0.2, rely = 0.3, anchor = 'n', width = 200)
    B2 = tk.Button(Mm, text = 'View User Details', font = 'Helvetica', bg = 'yellow')
    B2.place(relx = 0.2, rely = 0.5, anchor = 'n', width = 200)
    B3 = tk.Button(Mm, text = 'Make a Transaction', font = 'Helvetica', bg = 'yellow')
    B3.place(relx = 0.2, rely = 0.7, anchor = 'n', width = 200)
    B4 = tk.Button(Mm, text = 'View Transaction History', font = 'Helvetica', bg = 'yellow')
    B4.place( relx = 0.8, rely = 0.3, anchor = 'n', width = 200)
    B5 = tk.Button(Mm, text = 'Close Account', font = 'Helvetica', bg = 'yellow')
    B5.place(relx = 0.8, rely = 0.5, anchor = 'n', width = 200)
    B6 = tk.Button(Mm, text = 'Exit', font = 'Helvetica', bg = 'yellow', command = lambda: sys.exit())
    B6.place(relx = 0.8, rely = 0.7, anchor = 'n', width = 200)
Main_Menu()
app.mainloop()