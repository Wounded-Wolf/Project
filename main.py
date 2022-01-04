# from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import function as fn


global date
def instructions(root):
    ints = ["1. First set date.", "2. Then Type the registration number.", "3. Then select the operation."]
    ins = tk.Toplevel(root)
    ins.title("Instructions")
    i = 0
    for items in ints:
        tk.Label(ins, text=ints[i]).grid(row=i,column=0)
        i += 1
        

def sele_date(cal, ent, b1, b2, datt, b3):
    global date
    date = cal.get_date()
    datt.config(text = date, fg = "green")
    # date = x.replace("/", "")
    enable_widgets(ent, b1, b2, b3)
    # fn.read_file(date)

def enable_widgets(ent, b1, b2, b3):
    ent['state'] = 'enable'
    b1['state'] = 'enable'
    b2['state'] = 'enable'
    b3['state'] = 'enable'


def add_attendance(ent):
    regist_num = ent.get()
    if(not(regist_num.isspace()) and len(regist_num) != 0):
        fn.add_attendance(regist_num.upper(), date)
    else:
        messagebox.showerror("Error", "Invalid input.")
                                            


def delete_attendance(e_inp):
    regist_num = ent.get()

    if(not(regist_num.isspace()) and len(regist_num) != 0):
        fn.deletion_of_attendance(regist_num.capitalize(), date)
    else:
        messagebox.showerror("Error", "Invalid input.")


def show_result(date, root):
    fn.show_data(date, root)

root = tk.Tk()
root.title("Attendance System")
root.geometry("430x250")
# for label
tk.Label(root, text="Enter Registration Number").place(x=3, y=0)
tk.Label(root, text="Selected Date: ").place(x=167,y=183)
dates = tk.Label(root, text="Un-Defined", fg='red')
# for remaining widgets
e_inp = Entry(root, width=15, state = "disabled")
b_inst = Button(root, text="Instructions", command=lambda: instructions(root))
b_setDate = Button(root, text="Select date", command=lambda: sele_date(cal, e_inp, b_add_attendance, b_delete_attendance, dates, b_show_data))
b_delete_attendance = Button(root, text="Delete Attendance", state = 'disabled', command=lambda: delete_attendance(e_inp))
b_show_data = Button(root, text="Show Attendance Data.",state='disabled' ,command=lambda:show_result(date, root))
b_add_attendance = Button(root, text="Add Attendance", command=lambda: add_attendance(e_inp), state='disabled')
# for calender
cal = Calendar(root, selectmode = 'day', year = 2021, month = 12, day = 26)
# placement data
dates.place(x=247, y=183)
cal.place(x=170,y=0)
e_inp.place(x=3,y=18)
b_inst.place(x=3, y=40)
b_setDate.place(x=3,y=68)
b_add_attendance.place(x=3, y=96)
b_delete_attendance.place(x=3, y=124)
b_show_data.place(x=3, y=152)
root.mainloop() # main loop to iterate through the code