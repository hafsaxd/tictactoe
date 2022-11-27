import tkinter as tk
from tkinter import ttk
from random import randint
import game
from bcolors import bcolors
import time

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

        photo = tk.PhotoImage(file='ticcc.png')
        
        self.config(background="pink")#change background color

        label = tk.Label(self, 
                text="Welcome To \nThe Unbeatable \nTic-Tac-Toe ! ",
                font=('Comic Sans MS',25,'bold'),
                fg='blue', 
                bg='#ADD8E6',
                relief=tk.RAISED,
                bd=10,
                padx=20,
                pady=20,
                image=photo,
                compound='bottom' )
        
        label.image = photo # keep a reference!
        label.grid(column=0, row=0, pady=20)
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
                "!\n How to play: \n\n 1)The game is played on a tic-tac-toe grid\n2)You must then select your character: X or O "
                +"\n 3) The computer will be assigned the other character and take turns with you "
                +"\n4) If you pick X , you will go first "
                +"\n5) If you pick O, the computer will go first"
                +"\n 6) The first player to get of their symbols in a row"
                +"\n(accross,down or diagonal) is the winner!")
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


  

class Page2(tk.Frame):
        board = [0,0,0,0,0,0,0,0,0]
        game_over = False 
        userX = True #defines if user chose X or O
        turn = 1
        turns = 0

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.config(background="pink")

            

            tk.Grid.rowconfigure(self, 2, weight=1)
            tk.Grid.rowconfigure(self, 5, weight=1)
            tk.Grid.rowconfigure(self, 6, weight=1)
            tk.Grid.rowconfigure(self, 7, weight=1)
            tk.Grid.columnconfigure(self, 0, weight=1)
            tk.Grid.columnconfigure(self, 1, weight=1)
            tk.Grid.columnconfigure(self, 2, weight=1)
            
            player_select_label = tk.Label(self, 
                                            text="Select the character you wish to play as :",
                                            font=('Comic Sans MS',15,'bold'),
                                            bg='pink')
            x_button = tk.Button(self,text='X', 
                                command= self.x_select,
                                font=('Comic Sans MS',10,'bold'),
                                bg='#62B371')
            o_button = tk.Button(self,text='O', 
                                command= self.o_select,
                                font=('Comic Sans MS',10,'bold'),
                                bg='#62B371')

            player_select_label.grid(row=1,column=0, columnspan=3, pady=(30, 0))
            x_button.grid(row=2,column=0, sticky='ew',padx=(40, 0))
            o_button.grid(row=2,column=2, sticky='ew',padx=(0, 40))
            self.var = tk.IntVar()

        def x_select(self):
            global userX
            player_character = 'X'
            userX = True
            player_label = tk.Label(self, text='You have selected ' + player_character +'\n You will go first!',
                                    font=('Comic Sans MS',10,'bold'),
                                    bg='pink')
            player_label.grid(row=3,column=0,sticky='nesw',columnspan=3)
            start_button = tk.Button(self,text='START',
                                    command=self.draw_board,
                                    font=('Comic Sans MS',10,'bold'),
                                    bg='#D9C21D',
                                    relief=tk.RAISED)
            start_button.grid(row=4,column=1,sticky='nesw')
        
        def o_select(self):
            global userX
            player_character = 'O'
            userX = False
            player_label = tk.Label(self, text='You have selected ' + player_character +'\n Computer will go first!',
                                    font=('Comic Sans MS',10,'bold'),
                                    bg='pink')
            player_label.grid(row=3,column=0,sticky='nesw',columnspan=3)
            start_button = tk.Button(self,text='START',
                                    command=self.draw_board,
                                    bg='#D9C21D',
                                    relief=tk.RAISED,
                                    font=('Comic Sans MS',10,'bold'))
            start_button.grid(row=4,column=1,sticky='nesw')

        def draw_board(self):
            global board
            global turn
            global turns
            global game_over
            turn = 1
            turns = 0
            game_over = False
            board = [0,0,0,0,0,0,0,0,0]
            self.t_l =tk.Button(self, text='', command= lambda: self.update_board(0),bg='#62B371',state='active')
            self.t_l.grid(row=5, column=0,sticky='nesw')
            self.t_m =tk.Button(self, text='', command= lambda: self.update_board(1),bg='#62B371',state='active')
            self.t_m.grid(row=5, column=1,sticky='nesw')
            self.t_r =tk.Button(self, text='', command= lambda: self.update_board(2),bg='#62B371',state='active')
            self.t_r.grid(row=5, column=2,sticky='nesw')
            self.m_l =tk.Button(self, text='', command= lambda: self.update_board(3),bg='#62B371',state='active')
            self.m_l.grid(row=6, column=0,sticky='nesw')
            self.m_m =tk.Button(self, text='', command= lambda: self.update_board(4),bg='#62B371',state='active')
            self.m_m.grid(row=6, column=1,sticky='nesw')
            self.m_r =tk.Button(self, text='', command= lambda: self.update_board(5),bg='#62B371',state='active')
            self.m_r.grid(row=6, column=2,sticky='nesw')
            self.b_l =tk.Button(self, text='', command= lambda: self.update_board(6),bg='#62B371',state='active')
            self.b_l.grid(row=7, column=0,sticky='nesw')
            self.b_m =tk.Button(self, text='', command= lambda: self.update_board(7),bg='#62B371',state='active')
            self.b_m.grid(row=7, column=1,sticky='nesw')
            self.b_r =tk.Button(self, text='', command= lambda: self.update_board(8),bg='#62B371',state='active')
            self.b_r.grid(row=7, column=2,sticky='nesw')

            self.buttons = [self.t_l, self.t_m, self.t_r, self.m_l, self.m_m, self.m_r, self.b_l, self.b_m, self.b_r,]
            
            self.start_game()       


        def update_board(self, position = None):
            global board
            global userX

            if(self.var.get() == 0):
                self.var.set(1)
            else:
                self.var.set(0)

            if(position != None and board[position] == 0):
                board[position] = -1

            for r in range(5,8):
                for c in range(3):
                    if(board[(r-5)*3+c] == 1):
                        tk.Button(self, text='O' if userX else 'X',font=('Comic Sans MS',15,'bold')).grid(row=r,column=c,sticky='nesw')
                    elif(board[(r-5)*3+c] == -1):
                        tk.Button(self, text='X' if userX else 'O',font=('Comic Sans MS',15,'bold')).grid(row=r,column=c,sticky='nesw')


        def start_game(self):
            global board
            global userX
            

            reverse = not userX

            if(not reverse):
                print("You are X and the computer is O")
            else:
                print("You are O and the computer is X")

            while(0 in board and game.gameStatus(board) == 0):
                if(not reverse):
                    self.buttons[0].wait_variable(self.var)
                    game.printBoard(board, reverse)

                    if(0 not in board or game.gameStatus(board)!=0):
                        break

                    print(bcolors.OKBLUE+'Computer thinking...'+bcolors.ENDC)
                    for btn in self.buttons:
                        btn['state'] = 'disabled'
                    board = game.computerMakeMove(board)       
                    for btn in self.buttons:
                        btn['state'] = 'normal'
                    self.update_board()
                    game.printBoard(board, reverse)

                else:
                    print(bcolors.OKBLUE+'Computer thinking...'+bcolors.ENDC)
                    for btn in self.buttons:
                        btn['state'] = 'disabled'
                    board = game.computerMakeMove(board)       
                    for btn in self.buttons:
                        btn['state'] = 'normal'
                    self.update_board()
                    game.printBoard(board, reverse)

                    if(0 not in board or game.gameStatus(board)!=0):
                        break

                    self.buttons[0].wait_variable(self.var)
                    game.printBoard(board, reverse)

            status = game.gameStatus(board) 
            
            if(game.gameStatus(board) != 0):
                if(game.gameStatus(board) == 1):
                    print(bcolors.BOLD+'Computer has won. Better luck next time!'+bcolors.ENDC)
                    self.open_popup()
                    status = 0
                else:
                    print(bcolors.BOLD+'Congratulations! You have won!'+bcolors.ENDC)
                    self.open_popup()
            elif(0 not in board):
                print(bcolors.BOLD+'Draw!'+bcolors.ENDC)
                self.open_popup()
            # exit()
        
  

        def open_popup(self):
            top= tk.Toplevel(self)
            top.geometry("250x100")
            top.config(background='yellow')
            top.title("Result")

            if(game.gameStatus(board) != 0):
                if(game.gameStatus(board) == 1): 
                    win = tk.Label(top,text='Computer has won.\n Better luck next time!',font=('Comic Sans MS',10,'bold'),bg='yellow')
                    win.pack()
                    restart = tk.Button(top,text='Restart', command= lambda : [top.destroy(),self.draw_board()],
                                        font=('Comic Sans MS',10,'bold'),
                                        fg="black",
                                        bg="white",
                                        activeforeground="green",
                                        activebackground="black", )
                    
                    restart.pack(padx=50)
                    #status = 0
                else:
                    win = tk.Label(self,text='Congratulations! You have won!',font=('Comic Sans MS',10,'bold'),bg='yellow').pack()
                    restart = tk.Button(top,text='Restart', command= lambda : [top.destroy(),self.draw_board()] ,
                                        font=('Comic Sans MS',10,'bold'),
                                        fg="black",
                                        bg="white",
                                        activeforeground="green",
                                        activebackground="black",)
                    restart.pack()
            elif(0 not in board):
                    win = tk.Label(self,text='Draw!',font=('Comic Sans MS',10,'bold')).pack()
                    restart = tk.Button(top,text='Restart', command= lambda : [top.destroy(),self.draw_board()] ,
                                        font=('Comic Sans MS',10,'bold'),
                                        fg="black",
                                        bg="white",
                                        activeforeground="green",
                                        activebackground="black",)
                    restart.pack()
            # exit()
        


        

  
# Driver Code
root = tkinterApp()
root.geometry('500x500')
root.resizable(False, False)
root.title("Tic-Tadventure")
root.mainloop()

