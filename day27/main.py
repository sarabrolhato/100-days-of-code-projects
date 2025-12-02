from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=200, height=100)

#Labels
label_1 = Label(text="Miles")
# label_1.config(text="This is new text")
label_1.grid(row=0, column=2)

label_2 = Label(text="is equal to")
# label_2.config(text="This is new text")
label_2.grid(row=1, column=0)

label_3 = Label(text="0")
label_3.grid(row=1, column=1)

label_4 = Label(text="Km")
# label_4.config(text="This is new text")
label_4.grid(row=1, column=2)

#Buttons
def action():
    miles = entry.get()
    km = round(float(miles) * 1.60934)
    label_3.config(text=f"{km}")

#calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(row=2, column=1)


#Entries
entry = Entry(width=10)
#Add some text to begin with
entry.insert(END, string="0")
#Gets text in entry
print(entry.get())
entry.grid(row=0, column=1)


window.mainloop()