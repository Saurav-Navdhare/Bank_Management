import tkinter as tk
from tkinter import EXCEPTION
import Employee_end as Ee
import sys
import time

def C1(name, phone, email):
    global F, TL1
    TL1 = tk.Label(F, text = '', font = ('Arial', 18, 'bold'), bg = 'grey')
    TL1.place(relx = 0.1, rely = 0.1)
    if not(name and phone and email):
        TL1['text'] = 'Make Sure to Fill all the details'
    elif not(phone.isdigit() and len(phone) == 10):
        TL1['text'] = 'Please Enter Phone Number Correctly, No need to add Country code'
    else:
        try:
            A = Ee.new_user(name, phone, email)
        except:
            TL1['text'] = EXCEPTION
        else:
            TL1['text'] = A[1]

def T1(a, b, c, d):  # Amount, Sender, Beneficiar, Mode
    global Fr
    FrL4 = tk.Label(Fr, font = ('Arial', 18), background = 'yellow')
    FrL4.place(relx = 0.3, rely = 0.9)
    e = Ee.trans(str(a),d, str(b), str(c))
    FrL4['text'] = e

def accsel(z):
    global F1, SE
    SE = tk.Tk()
    SE.geometry('1280x720')
    SE.minsize(1280, 720)
    SE.configure(background = 'lightblue')
    L1 = tk.Label(SE, text = "Enter Account Holder's Name", font = ('Arial', 18))
    L1.place(relx = 0.1, rely = 0.1)
    E1 = tk.Entry(SE)
    E1.place(relx = 0.5, rely = 0.1, relwidth = 0.4)
    B1 = tk.Button(SE, text = 'Search Account Number', font = ('Arial', 18), command = lambda: search(E1.get(),z))
    B1.place(relx = 0.3, rely = 0.2)
    F1 = tk.Frame(SE)
    F1.place(relx = 0.1 ,rely = 0.35, relwidth = 0.8, relheight = 0.35)
    SE.mainloop()

def search(a,z):
    global srno, b, F1, X
    try:
        X.destroy()
    except:
        pass
    F1.destroy()
    F1 = tk.Frame(SE)
    F1.place(relx = 0.1 ,rely = 0.35, relwidth = 0.8, relheight = 0.35)
    b = Ee.account_number(a)
    srno = 0
    for i in b:
        X = tk.Entry(F1, width = 270)
        X.grid(row = srno, column = 0)
        srno += 1
        X.insert(tk.END, str(srno) + ' > ' + i[0] + ' ' + i[1])
        X['state'] = 'disabled'
    if(srno == 0):
        X = tk.Entry(F1, width = 270)
        X.grid(row = srno +1, column = 0)
        X.insert(tk.END, 'No Account Founded')
        X['state'] = 'disabled'
    else:
        C = tk.Label(SE, text = 'Please Enter the Serial Number', font = ('Arial', 18))
        C.place(relx = 0.1, rely = 0.8)
        D = tk.Entry(SE)
        D.place(relx = 0.6, rely = 0.8)
        E = tk.Button(SE, text = 'Click to Select Account', font = ('Arial', 18), command = lambda : acc(D.get(),z))
        E.place(relx = 0.3, rely = 0.9)

def acc(a,z):
    global b, Number, Fr, FrB1, FrE1, FrB2, FrE2
    Number = 0
    if not(a.isdigit()):
        A = tk.Label(SE, text = 'Please Enter Digits only', font = ('Arial', 18))
        A.place(relx = 0.6, rely = 0.9, relwidth = 0.3)
    elif(int(a) > srno):
        A = tk.Label(SE, text = 'Please Enter From Given', font = ('Arial', 18))
        A.place(relx = 0.6, rely = 0.9, relwidth = 0.3)
    else:
        k = 1
        for i in b:
            if(int(a) == k):
                Number = i[0]
            k += 1
        SE.destroy()
        if(z == 1):
            FrB1.destroy()
            FrE1 = tk.Entry(Fr)
            FrE1.place(relx = 0.6, rely = 0.25)
            FrE1.insert(tk.END, Number)
            FrE1['state'] = 'disabled'
        else:
            FrB2.destroy()
            FrE2 = tk.Entry(Fr)        
            FrE2.place(relx = 0.6, rely = 0.4)
            FrE2.insert(tk.END, Number)
            FrE2['state'] = 'disabled'
            FrL3 = tk.Label(Fr, text = "Amount", font = ('Arial', 18))
            FrL3.place(relx = 0.2, rely = 0.6)
            FrE3 = tk.Entry(Fr)
            FrE3.place(relx = 0.5, rely = 0.6)
            FrE3.insert(tk.END, '500')
            FrL4 = tk.Label(Fr, text = '', font = ('Arial',18))
            FrL4.place(relx = 0.4, rely = 0.8)
            FrB3 = tk.Button(Fr, text = 'Make Transaction', font = ('Arial', 18), activebackground = 'yellow', command = lambda : T1(FrE3.get(),FrE1.get, FrE2.get(), 1))
            FrB3.place(relx = 0.3, rely = 0.7)
            FrB4 = tk.Button(Fr, text = 'Main Menu', font = ('Arial',18),activebackground = 'yellow', command = main_menu)
            FrB4.place(relx = 0.6, rely = 0.8)
                
    
def TM1():
    global Fr, FrB1, FrB2
    Fr = tk.LabelFrame(F, text = 'Bank to Bank Transaction', font = ('Arial', 18, 'bold'))
    Fr.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    FrL1 = tk.Label(Fr, text = "Sender's Account Number", font = ('Arial', 18))
    FrL1.place(relx = 0.2, rely = 0.25)
    FrB1 = tk.Button(Fr, text = "Select", font = ('Arial', 18), activebackground = 'yellow', command = lambda : accsel(1))
    FrB1.place(relx = 0.6, rely = 0.25)
    FrL2 = tk.Label(Fr, text = "Beneficiar's Account Number", font = ('Arial', 18))
    FrL2.place(relx = 0.2, rely = 0.4)
    FrB2 = tk.Button(Fr, text = "Select", font = ('Arial', 18), activebackground = 'yellow', command = lambda : accsel(2))
    FrB2.place(relx = 0.6, rely = 0.4)

app = tk.Tk()
app.geometry('1280x720')
app.minsize(1280,720)
app.title('Bank Management System By Saurav And Ovesh')
app.configure(bg = 'lightblue')

def new_user():
    global F
    F = tk.LabelFrame(app, text = 'New User', width = 1280, height = 720, bg = 'lightblue', font = ('Arial', 22, 'bold'))
    F.place(relx = 0, rely = 0)
    NL1 = tk.Label(F, text = 'Enter Name', font = ('Arial', 18, 'bold'))
    NL1.place(relx = 0.2, rely = 0.25, relwidth = 0.15)
    NL2 = tk.Label(F, text = 'Enter Email', font = ('Arial', 18, 'bold'))
    NL2.place(relx = 0.2, rely = 0.45, relwidth = 0.15)
    NL3 = tk.Label(F, text = 'Enter Phone', font = ('Arial', 18, 'bold'))
    NL3.place(relx = 0.2, rely = 0.65, relwidth = 0.15)
    name = tk.Entry(F)
    name.place(relx = 0.5, rely = 0.25, relwidth = 0.2)
    email = tk.Entry(F)
    email.place(relx = 0.5, rely = 0.45, relwidth = 0.2)
    phone = tk.Entry(F)
    phone.place(relx = 0.5, rely = 0.65, relwidth = 0.2)
    NB1 = tk.Button(F, text = '< Back', bg = 'grey', activebackground = 'yellow', font = ('Arial', 18, 'bold'), command = main_menu)
    NB1.place(relx = 0.2, rely = 0.80, relwidth = 0.2)
    NB2 = tk.Button(F, text = 'Create Account >', bg = 'grey', activebackground = 'yellow', font = ('Arial', 18, 'bold'), command = lambda: C1(name.get(), phone.get(), email.get()))
    NB2.place(relx = 0.5, rely = 0.80, relwidth = 0.2)


def Transaction():
    global F
    F = tk.LabelFrame(app, text = 'Transaction', width = 1280, height = 720, bg = 'lightblue', font = ('Arial', 22, 'bold'))
    F.place(relx = 0, rely = 0)
    TL1 = tk.Label(F, text = 'Select Type of Transaction', bg = 'grey', font = ('Arial', 14))
    TL1.place(relx = 0.3, rely = 0.1, relwidth = 0.25)
    TB1 = tk.Button(F, text = 'Bank to Bank', bg = 'grey', activebackground = 'yellow', command = TM1)
    TB1.place(relx = 0.3, rely = 0.2, relwidth = 0.25)
    TB2 = tk.Button(F, text = 'Cash Withdrawal', bg = 'grey', activebackground = 'yellow')
    TB2.place(relx = 0.3,rely = 0.4, relwidth = 0.25)
    TB3 = tk.Button(F, text = 'Cash Deposit', bg = 'grey', activebackground = 'yellow')
    TB3.place(relx = 0.3, rely = 0.6, relwidth = 0.25)
    TB4 = tk.Button(F, text = 'Back', bg = 'grey', activebackground = 'yellow', command = main_menu)
    TB4.place(relx = 0.3, rely = 0.8, relwidth = 0.25)

def main_menu():
    try:
        global F
        F.destroy()
    except:
         pass
    Button1 = tk.Button(app, text = 'New User', bg = 'grey', activebackground = 'yellow', command = new_user)
    Button1.place(relx = 0.1, rely = 0.2, relwidth = 0.2)
    Button2 = tk.Button(app, text = 'View Account Details', bg = 'grey', activebackground = 'yellow')
    Button2.place(relx = 0.1, rely = 0.5, relwidth = 0.2)
    Button3 = tk.Button(app, text = 'Transaction', bg = 'grey', activebackground = 'yellow', command= Transaction)
    Button3.place(relx = 0.1, rely = 0.8, relwidth = 0.2)
    Button4 = tk.Button(app, text = 'View Trasaction History', bg = 'grey', activebackground = 'yellow')
    Button4.place(relx = 0.6, rely = 0.2, relwidth = 0.2)
    Button5 = tk.Button(app, text = 'Close an Account', bg = 'grey', activebackground = 'yellow')
    Button5.place(relx = 0.6, rely = 0.5, relwidth = 0.2)
    Button6 = tk.Button(app, text = 'Exit', bg = 'grey', activebackground = 'yellow', command = sys.exit)
    Button6.place(relx = 0.6, rely = 0.8, relwidth = 0.2)

main_menu()
app.mainloop()