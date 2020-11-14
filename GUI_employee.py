import sys
import Employee_end as Ee
import tkinter as tk
def give():
    print(dropdown.get())
app = tk.Tk()
app.geometry('1280x720')
app.title('SO Bank')
LF = tk.LabelFrame(app,
                    text = 'Welcome to SO Bank',
                    font = ('Helvetica',20,'bold'),
                    bg ='#6dd1e3',
                    height = 650,
                    width = 950,
                    borderwidth = 20,
                    relief = 'groove')
LF.place(relx = 0.03, rely = 0.05)
dropdown = tk.StringVar(LF)
dropdown.set("New_User") # default value
w = tk.OptionMenu(LF, dropdown, "New_User", "User_details", "Transaction", "transaction_History", "Close_Account", "Exit")
w.place(relx = 0.4, rely = 0.3)
dropdown_btn = tk.Button(LF, text = "Select", command = give, borderwidth = 0)
dropdown_btn.place(relx = 0.45, rely = 0.6)
app.mainloop()

