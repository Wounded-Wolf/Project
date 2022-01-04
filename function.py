import tkinter as tk
import json
from tkinter import ttk
from tkinter import messagebox
def read_file():
	with open("data.json", 'r') as fp:
		return json.load(fp) # actul load the file, for further useage, as it re
def write_data(reg_no):
	with open("data.json", 'w') as fp:
		json.dump(reg_no, fp)


def check_duplicate_dates(loaded_list, entered):
	for i in range(len(loaded_list)):
		for j in range(len(loaded_list[i])):
			if(loaded_list[i][0] == entered):
				return i # which is present
			else:
				pass
	return -1


def check_reg_no(reg_no, loaded_list):
	for i in range(1, len(loaded_list)):
		if(reg_no == loaded_list[i]):
			return -1
	return 1

def add_attendance(reg_no, selected_date):
	load = read_file() 
	if(len(load) != 0):
		result = check_duplicate_dates(load, selected_date)
		if(result == -1):
			lists = [selected_date, reg_no]
			load.append(lists)
			write_data(load)
		else:
			res = check_reg_no(reg_no, load[result])
			if(res == -1):
				messagebox.showerror("Error", "Double attendance is not allowed.")
				pass
			else:
				load[result].append(reg_no)
				write_data(load)
	else:
		lists = [selected_date, reg_no]
		load.append(lists)
		write_data(load)


def deletion_of_attendance(reg_no, selected_date):
	load = read_file()
	if(len(load) != 0):
		result = check_duplicate_dates(load, selected_date)
		if(result == -1):
			messagebox.showerror("Error", "Record for this date is empty, try adding attendance first.")
		else:
			res = check_reg_no(reg_no, load[result])
			if(res == -1):
				load[result].remove(reg_no)
				write_data(load)
			else:
				messagebox.showerror("Error", "No such registraton number exist, in this date's record.")
	else:
		messagebox.showerror("Error", "Record is empty, try adding attendance first.")



def update_result():
	print("Update funtion")


# 
def show_data(date, root):
	file = read_file()
	if(len(file) != 0):
		result = check_duplicate_dates(file, date)
		if(result != -1):
			inst = tk.Toplevel(root)
			inst.title("Attendance")
			column = ('date', 'Registration_Number')
			tree = ttk.Treeview(inst, columns=column, show='headings')
			tree.heading('date', text="Date")
			tree.heading('Registration_Number', text="Registration Number")
			# creating tuple list
			selected_date = []
			for i in range(1, len(file[result])):
				selected_date.append((file[result][0],file[result][i]))
			for i in selected_date:
				tree.insert('', 'end', values=i)
			tree.pack()


			# here we add data to the treeview

		else:
			messagebox.showerror("Error", "Record for this date is empty, try adding attendance first.")
	else:
		messagebox.showerror("Error", "Record is empty, try adding attendance first.")



# show_data("12221")
# show_data("12321")
# show_data("12121")