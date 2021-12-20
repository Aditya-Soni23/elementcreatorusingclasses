from tkinter import*
from tkinter import ttk


root = Tk()
root.geometry("900x600")
root.title("Classes")

gui_elements = ["label","button","dropdown"]

dropdown = ttk.Combobox(root,state = "read only",values = gui_elements)
dropdown.pack()

class createElements:
    def __init__(self):
        print("This is create elements classes")
        
    def createlabel(self):
        label = Label(root, text ="A new label is been created using class",fg="red")
        label.pack()
        
    def createbutton(self):
        button = Button(root,text = " Button ",command = self.message)
        button.pack(padx = 20, pady = 10)
        
    def createdropdown(self):
        value = [1,2,3,4,5]
        
        classdropdown = ttk.Combobox(root,state = "read only", values = value)
        classdropdown.pack()

    def choose(self):
        global dropdown
        element = dropdown.get()
        if(element=="label"):
            self.createlabel()
            
        elif (element =="button"):
            self.createbutton()
            
        elif(element=="dropdown"):
            self.createdropdown()
        

    def message(self):
        messagebox.showinfo("showinfo","You clicked the button created using class")
        
obj_of_CreateElements = createElements()
btn = Button(root,text = "Select an element to be created " , command  = obj_of_CreateElements.choose)
btn.pack(padx = 20, pady = 10)

root.mainloop()