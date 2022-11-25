import tkinter as tk
from tkinter import ttk
from random import randint

from index import computerMakeMove  

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
                text="Welcome to \nTic-Tac-Toe ! ",
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
                "!\n How to play: \n\n 1)The game is played on a tic-tac-toe grid\n2)You must then select your character: X or O "
                +"\n 3) The computer will be assigned the other character and take turns with you \n 4) The first player to get of their symbols in a row\n(accross,down or diagonal) is the winner!")
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
        player_character = ''
        ai_character = ''
        positions = ['-','-','-','-','-','-','-','-','-']
        game_over = False 
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

            def computer_turn():
                global turn
                global turns 
                global positions
                global ai_character
                
                
                while turn == 0 and turns < 9:
                    #ai_select = computerMakeMove(positions)
                    ai_select = randint(0,8)
                    print(turn,ai_select,positions[ai_select])
                    if positions[ai_select] == '-':
                        positions[ai_select] = ai_character
                        if 0 <= ai_select <= 2:
                            r = 5 
                        elif 3 <= ai_select <= 5:
                            r = 6
                        else:
                            r = 7
                        if ai_select == 0 or ai_select == 3 or ai_select == 6:
                            c = 0
                        elif ai_select == 1 or ai_select == 4 or ai_select == 7:
                            c = 1
                        else :
                            c = 2
                        new_button = tk.Button(self, text=positions[ai_select],font=('Comic Sans MS',15,'bold')).grid(row=r,column=c,sticky='nesw')
                        game_over = check_game_over(positions)
                        turn = 1
                        turns +=1
                

            def check_game_over(pos):
                global game_over
                if pos[0] + pos[1] + pos[2] == 'XXX' or\
                    pos[3] + pos[4] + pos[5] == 'XXX' or\
                    pos[6] + pos[7] + pos[8] == 'XXX' or\
                    pos[0] + pos[3] + pos[6] == 'XXX' or\
                    pos[1] + pos[4] + pos[7] == 'XXX' or\
                    pos[2] + pos[5] + pos[8] == 'XXX' or\
                    pos[0] + pos[4] + pos[8] == 'XXX' or\
                    pos[2] + pos[4] + pos[6] == 'XXX' :
                    game_over =True
                    win_label = tk.Label(self,text='X wins',font=('Comic Sans MS',15,'bold'),bg='pink').grid(row =8,column=1)
                elif pos[0] + pos[1] + pos[2] == 'OOO' or\
                    pos[3] + pos[4] + pos[5] == 'OOO' or\
                    pos[6] + pos[7] + pos[8] == 'OOO' or\
                    pos[0] + pos[3] + pos[6] == 'OOO' or\
                    pos[1] + pos[4] + pos[7] == 'OOO' or\
                    pos[2] + pos[5] + pos[8] == 'OOO' or\
                    pos[0] + pos[4] + pos[8] == 'OOO' or\
                    pos[2] + pos[4] + pos[6] == 'OOO' :
                    game_over =True
                    win_label = tk.Label(self,text='O wins',font=('Comic Sans MS',15,'bold',),bg='pink').grid(row =8,column=1)
                else:
                    if game_over == False and turns == 9:
                        win_label = tk.Label(self,text='Its a draw',font=('Comic Sans MS',15,'bold'),bg='pink').grid(row =8,column=1)

                return game_over


            def x_select():
                global player_character
                global ai_character
                player_character = 'X'
                ai_character = 'O'
                player_label = tk.Label(self, text='You have selected ' + player_character,
                                        font=('Comic Sans MS',10),
                                        bg='pink')
                player_label.grid(row=3,column=0,sticky='nesw',columnspan=3)
                start_button = tk.Button(self,text='START',
                                        command=draw_board,
                                        font=('Comic Sans MS',10,'bold'),
                                        bg='#D9C21D',
                                        relief=tk.RAISED)
                start_button.grid(row=4,column=1,sticky='nesw')
            def o_select():
                global player_character
                global ai_character
                player_character = 'O'
                ai_character = 'X'
                player_label = tk.Label(self, text='You have selected ' + player_character,
                                        font=('Comic Sans MS',10),
                                        bg='pink')
                player_label.grid(row=3,column=0,sticky='nesw',columnspan=3)
                start_button = tk.Button(self,text='START',
                                        command=draw_board,
                                        bg='#D9C21D',
                                        relief=tk.RAISED,
                                        font=('Comic Sans MS',10,'bold'))
                start_button.grid(row=4,column=1,sticky='nesw')

            def player_position(position) :
                global turn
                global turns
                global positions
                global game_over

                if 0 <= position <= 2:
                    r = 5 
                elif 3 <= position <= 5:
                    r = 6
                else:
                    r = 7
                if position == 0 or position == 3 or position == 6:
                    c = 0
                elif position == 1 or position == 4 or position == 7:
                    c = 1
                else :
                    c = 2
                
                if turn == 1 and turns < 9 and game_over == False:
                    if positions[position] == '-':
                        positions[position] =player_character
                        new_button = tk.Button(self, text=positions[position],font=('Comic Sans MS',15,'bold')).grid(row=r,column=c,sticky='nesw')
                        game_over = check_game_over(positions)
                        turn = 0
                        turns +=1
                        print(turn)
                        print(turns)
                        computer_turn()


            def draw_board():
                global positions
                global turn
                global turns
                global game_over
                turn = 1
                turns = 0
                game_over = False
                positions = ['-','-','-','-','-','-','-','-','-']
                t_l =tk.Button(self, text=positions[0], command= lambda: player_position(0),bg='#62B371')
                t_l.grid(row=5, column=0,sticky='nesw')
                t_m =tk.Button(self, text=positions[0], command= lambda: player_position(1),bg='#62B371')
                t_m.grid(row=5, column=1,sticky='nesw')
                t_r =tk.Button(self, text=positions[0], command= lambda: player_position(2),bg='#62B371')
                t_r.grid(row=5, column=2,sticky='nesw')
                m_l =tk.Button(self, text=positions[0], command= lambda: player_position(3),bg='#62B371')
                m_l.grid(row=6, column=0,sticky='nesw')
                m_m =tk.Button(self, text=positions[0], command= lambda: player_position(4),bg='#62B371')
                m_m.grid(row=6, column=1,sticky='nesw')
                m_r =tk.Button(self, text=positions[0], command= lambda: player_position(5),bg='#62B371')
                m_r.grid(row=6, column=2,sticky='nesw')
                b_l =tk.Button(self, text=positions[0], command= lambda: player_position(6),bg='#62B371')
                b_l.grid(row=7, column=0,sticky='nesw')
                b_m =tk.Button(self, text=positions[0], command= lambda: player_position(7),bg='#62B371')
                b_m.grid(row=7, column=1,sticky='nesw')
                b_r =tk.Button(self, text=positions[0], command= lambda: player_position(8),bg='#62B371')
                b_r.grid(row=7, column=2,sticky='nesw')

            
            player_select_label = tk.Label(self, 
                                            text="Select the character you wish to play as :",
                                            font=('Comic Sans MS',15,'bold'),
                                            bg='pink')
            x_button = tk.Button(self,text='X', 
                                command= x_select,
                                font=('Comic Sans MS',10,'bold'),
                                bg='#62B371')
            o_button = tk.Button(self,text='O', 
                                command= o_select,
                                font=('Comic Sans MS',10,'bold'),
                                bg='#62B371')

            player_select_label.grid(row=1,column=0, columnspan=3, pady=(30, 0))
            x_button.grid(row=2,column=0, sticky='ew',padx=(40, 0))
            o_button.grid(row=2,column=2, sticky='ew',padx=(0, 40))
            
        
  
# Driver Code
root = tkinterApp()
root.geometry('500x500')
root.resizable(False, False)
root.title("Tic-Tadventure")
root.mainloop()

