from tkinter import *

root = Tk()
root.iconbitmap(r'newicon.ico')
root.title("Calculator By @Niloy Sikdar")
root.config(bg="#80ed13")
root.resizable(0, 0)

#Define functions

def button_click(number):
	current  = myEntry.get()
	myEntry.delete(0, END)
	myEntry.insert(0, str(current) + str(number))

def button_clear():
	myEntry.delete(0, END)

def button_point():
	normal = myEntry.get()
	myEntry.delete(0, END)
	after = str(normal) + "."
	myEntry.insert(0, after)

def button_add():
	global number_one
	number_one = myEntry.get()
	global func
	func = "add"
	myEntry.delete(0, END)
	history.config(text = str(number_one) + " + ")

def button_sub():
	global number_one
	number_one = myEntry.get()
	global func
	func = "sub"
	myEntry.delete(0, END)
	history.config(text = str(number_one) + " - ")

def button_multi():
	global number_one
	number_one = myEntry.get()
	global func
	func = "multi"
	myEntry.delete(0, END)
	history.config(text = str(number_one) + " * ")

def button_div():
	global number_one
	number_one = myEntry.get()
	global func
	func = "div"
	myEntry.delete(0, END)
	history.config(text = str(number_one) + " / ")

def button_equal():
	number_two = myEntry.get()
	myEntry.delete(0, END)
	if func == "add":
		answer = round( float(number_one) + float(number_two) , 4)
		myEntry.insert(0, answer)
		history.config(text=str(number_one) + " + " + str(number_two) + " = " + str(answer))

	elif func == "sub":
		answer = round( float(number_one) - float(number_two) , 4)
		myEntry.insert(0, answer)
		history.config(text=str(number_one) + " - " + str(number_two) + " = " + str(answer))

	elif func == "multi":
		answer = round( float(number_one) * float(number_two) , 4)
		myEntry.insert(0, answer)
		history.config(text=str(number_one) + " * " + str(number_two) + " = " + str(answer))

	elif func == "div":
		answer = round ( float(number_one) / float(number_two) , 4)
		myEntry.insert(0, answer)
		history.config(text=str(number_one) + " / " + str(number_two) + " = " + str(answer))

#Entry box

myEntry = Entry(root, width=35, borderwidth=10, bg="#cff3ff", font="5")
myEntry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

historyName = Label(root, text="History : ", bg="#ff5e5e", font="20")
historyName.grid(row=1, column=0, padx=8, pady=15)

history = Label(root, bg="#ff7d7d", font="20")
history.grid(row=1, column=1, columnspan=3)

name = Label(root, text="Made by @Niloy Sikdar",pady =15, bg="#80ed13", font=("Times", "15", "bold italic"))
name.grid(row=7, column=1, columnspan=2)


#Define Buttons

button_1 = Button(root, text="1", padx=30, pady=15, font="5", bg="#13cced", borderwidth= 4, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=15, font="5", bg="#13cced", borderwidth= 4, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=15, font="5", bg="#13cced", borderwidth= 4, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=15, font="5", bg="#13cced", borderwidth= 4, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=15, font="5", bg="#13cced", borderwidth= 4, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=15, font="5", bg="#13cced", borderwidth= 4, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=15, font="5", bg="#13cced", borderwidth= 4, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=15, font="5", bg="#13cced", borderwidth= 4, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=15, font="5", bg="#13cced", borderwidth= 4, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=30, pady=15, font="5", bg="#13cced", borderwidth= 4, command=lambda: button_click(0))

button_add = Button(root, text="+", padx=80, pady=15, font="5", bg="#ed9913", borderwidth= 4, command=button_add)
button_sub = Button(root, text="-", padx=30, pady=15, font="5", bg="#ed9913", borderwidth= 4, command=button_sub)
button_multi = Button(root, text="*", padx=30, pady=15, font="5", bg="#ed9913", borderwidth= 4, command=button_multi)
button_div = Button(root, text="/", padx=30, pady=15, font="5", bg="#ed9913", borderwidth= 4, command=button_div)

button_point = Button(root, text=".", padx=31, pady=15, font="5", bg="#13cced", borderwidth= 4, command=button_point)

button_clear = Button(root, text="C", padx=82, pady=15, font="5", bg="red", borderwidth= 4, command=button_clear)
button_equal = Button(root, text="=", padx=80, pady=15, font="5", bg="#1f3fcc", borderwidth= 4, command=button_equal)


#Put the buttons on the screen

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=5, column=0)

button_add.grid(row=5, column=2, columnspan=2)
button_sub.grid(row=4, column=3)
button_multi.grid(row=3, column=3)
button_div.grid(row=2, column=3)

button_point.grid(row=5, column=1)

button_clear.grid(row=6, column=0, columnspan=2)
button_equal.grid(row=6, column=2, columnspan=2)


#Starting mainloop

if __name__ ==  "__main__":
	root.mainloop()