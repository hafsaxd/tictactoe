import tkinter as tk
from tkinter import ttk
  

LARGEFONT =("Comic Sans MS", 35)
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        photo = tk.PhotoImage(file='ramadan.png')
        
        self.config(background="pink")#change background color

        label = tk.Label(self, 
                text="Ramadan \nTic-Tac-Toe Game ",
                font=('Comic Sans MS',30,'bold'),
                fg='blue', 
                bg='#ADD8E6',
                relief=tk.RAISED,
                bd=10,
                padx=20,
                pady=20,
                image=photo,
                compound='bottom' )
        
        label.image = photo # keep a reference!
        label.grid(column=0, row=0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
  
        button = tk.Button(self,                 
                            text="START",
                            font = ('Comic Sans MS',10,'bold'),
                            fg="black",
                            bg="white",
                            activeforeground="green",
                            activebackground="black",
                            command = lambda : controller.show_frame(Page1),
                            compound='top')
        
        button.grid(padx=10, pady=30)



# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        self.config(background="pink")

        def printInput():
            inp = inputtxt.get(1.0, "end-1c")
            lbl.config(text = "Hello there "+inp + 
                "!\n How to play: \n\n 1)The game is played on a tic-tac-toe\n2) One player uses crescent (☾) and another player uses a star (★)\n 3) The computer will take turns with you \n 4) The first player to get of their symbols in a row\n(accross,down or diagonal) is the winner!")
            button2 = ttk.Button(self, text ="PLAY!",
                                 command = lambda : controller.show_frame(Page2),
                                 )
            button2.pack(pady = 10)

        label = tk.Label(self, 
                text="Assalamualaikum, \nWhat is your name ?",
                font=('Comic Sans MS',15,'bold'),
                fg='black', 
                bg='#62B371',
                relief=tk.GROOVE,
                bd=10,
                padx=20,
                pady=20,
                compound='bottom' )
        
        label.pack(pady = 30)

        # TextBox Creation
        inputtxt = tk.Text(self,
                        height = 1,
                        width = 20)
        
        inputtxt.pack()
        
        # Button Creation
        printButton = tk.Button(self,
                                text = "Submit", 
                                command = printInput,
                                font = ('Comic Sans MS',10,'bold'),
                                fg="black",
                                bg="white",
                                activeforeground="green",
                                activebackground="black",
                                compound='top')
        printButton.pack(pady = 13)
        
        # Label Creation
        lbl = tk.Label(self,
                       text = "", 
                       bg='pink',
                       font = ('Comic Sans MS',10))
        lbl.pack()




        
  
  
  
  
# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(background="pink")

  
        
        # button to show frame 3 with text
        # layout3
        button = tk.Button(self,                 
                            text="Home",
                            font = ('Comic Sans MS',10,'bold'),
                            fg="black",
                            bg="white",
                            activeforeground="green",
                            activebackground="black",
                            command = lambda : controller.show_frame(StartPage),
                            compound='top')
        
        button.grid(padx=10, pady=30)
  
  
# Driver Code
root = tkinterApp()
root.geometry('500x500')
root.resizable(False, False)
root.title("Tic-Tadventure")
root.mainloop()
