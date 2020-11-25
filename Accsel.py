import tkinter as tk
import Employee_end as Ee
import time

Number = 0

def accsel():
    global F1, SE
    SE = tk.Tk()
    SE.geometry('1280x720')
    SE.minsize(1280, 720)
    SE.configure(background = 'lightblue')
    L1 = tk.Label(SE, text = "Enter Account Holder's Name", font = ('Arial', 18))
    L1.place(relx = 0.1, rely = 0.1)
    E1 = tk.Entry(SE)
    E1.place(relx = 0.5, rely = 0.1, relwidth = 0.4)
    B1 = tk.Button(SE, text = 'Search Account Number', font = ('Arial', 18), command = lambda: search(E1.get()))
    B1.place(relx = 0.3, rely = 0.2)
    F1 = tk.Frame(SE)
    F1.place(relx = 0.1 ,rely = 0.35, relwidth = 0.8, relheight = 0.35)
    SE.mainloop()

def search(a):
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
        E = tk.Button(SE, text = 'Click to Select Account', font = ('Arial', 18), command = lambda : acc(D.get()))
        E.place(relx = 0.3, rely = 0.9)

def acc(a):
    global b, Number
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
def run():
    global Number
    accsel()
    while(SE):
        time.sleep(3)
    return Number
