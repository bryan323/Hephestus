from Tkinter import*


root = Tk()

class HephMenu():


    def buildWindow(self, labelText, equipButton, equipButtonCommand):
        root.geometry("500x500")
	root.configure(background = "black")

	label = Label(text = labelText)
	label.configure(background = "black")
	label.configure(foreground = "lime")
	label.configure(font = ("Times New Roman", 44))
	label.place(x = 100, y = 100 )

        selectEquipment = Button(root, text = equipButton, command = equipButtonCommand)
        selectEquipment.place(x = 220, y = 205)

        root.mainloop()

    
