from tkinter import *


class Window(Frame):



    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()




    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Memory Manager")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)


		# button
        B = Button(root, text = "Memória", command=showMemory())

        B.place(x = 50,y = 50)

        




root = Tk()

#size of the window
root.geometry("400x300")

app = Window(root)
root.mainloop() 


