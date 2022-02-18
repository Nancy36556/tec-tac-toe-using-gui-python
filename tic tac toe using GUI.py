
from email import message
from os import stat
from tkinter import *
from tkinter import messagebox
import click
import numpy as np
import random
from time import sleep
root=Tk()
Clicked =True
Count=0
def disable_all_buttons():
   b1.config(state=DISABLED)
   b2.config(state=DISABLED)
   b3.config(state=DISABLED)
   b4.config(state=DISABLED)
   b5.config(state=DISABLED)
   b6.config(state=DISABLED)
   b7.config(state=DISABLED)
   b8.config(state=DISABLED)
   b9.config(state=DISABLED)
def checkifwon():
    global Winner 
    Winner =False
    if b1["text"] =="O" and  b2["text"] =="O" and b3["text"] =="O"  and b7["text"] =="X" and b8["text"] =="X" and b9["text"] =="X" :
        Winner=True
        messagebox.showinfo("tic tac toe","Congratulations!! O player")
        disable_all_buttons()
    elif b4["text"] =="O" and b5["text"] =="O" and b6["text"] =="O"  :
        Winner=True
        messagebox.showinfo("tic tac toe","Congratulations!! O player")
        disable_all_buttons()    
    elif b7["text"] =="O" and b8["text"] =="O" and b9["text"] =="O"  :
        Winner=True
        messagebox.showinfo("tic tac toe","Congratulations!! O player")
        disable_all_buttons()
    elif b1["text"] =="O" and b4["text"] =="O" and b7["text"] =="O"  :
            Winner=True
            messagebox.showinfo("tic tac toe","Congratulations!! O player")
            disable_all_buttons()
    elif b2["text"] =="O" and b5["text"] =="O" and b8["text"] =="O"  :
            Winner=True
            messagebox.showinfo("tic tac toe","Congratulations!! O player")
            disable_all_buttons()
    elif b3["text"] =="O" and b6["text"] =="O" and b9["text"] =="O"  :
            Winner=True
            messagebox.showinfo("tic tac toe","Congratulations!! O player")
            disable_all_buttons()
    elif b1["text"] =="O" and b5["text"] =="O" and b9["text"] =="O"  :
            Winner=True
            messagebox.showinfo("tic tac toe","Congratulations!! O player")
            disable_all_buttons() 
    elif b3["text"] =="O" and b5["text"] =="O" and b7["text"] =="O"  :
            Winner=True
            messagebox.showinfo("tic tac toe","Congratulations!! O player")  
            disable_all_buttons()  
    #CHICK FOR X'S WIN
    if b1["text"] =="X" and  b2["text"] =="X" and b3["text"] =="X"  and b7["text"] =="X" and b8["text"] =="X" and b9["text"] =="X" :
        Winner=True
        messagebox.showinfo("tic tac toe","Congratulations!! X player") 
        disable_all_buttons()
    elif b4["text"] =="X" and b5["text"] =="X" and b6["text"] =="X"  :
        Winner=True
        messagebox.showinfo("tic tac toe","Congratulations!! X player")   
        disable_all_buttons()  
    elif b7["text"] =="X" and b8["text"] =="X" and b9["text"] =="X"  :
        Winner=True
        messagebox.showinfo("tic tac toe","Congratulations!! X player") 
        disable_all_buttons()
    elif b1["text"] =="X" and b4["text"] =="X" and b7["text"] =="X"  :
            Winner=True
            messagebox.showinfo("tic tac toe","Congratulations!! X player") 
    elif b2["text"] =="X" and b5["text"] =="X" and b8["text"] =="X"  :
            Winner=True
            messagebox.showinfo("tic tac toe","Congratulations!! X player") 
            disable_all_buttons()
    elif b3["text"] =="X" and b6["text"] =="X" and b9["text"] =="X"  :
            Winner=True
            messagebox.showinfo("tic tac toe","Congratulations!! X player") 
            disable_all_buttons()
    elif b1["text"] =="X" and b5["text"] =="X" and b9["text"] =="X"  :
            Winner=True
            messagebox.showinfo("tic tac toe","Congratulations!! X player") 
            disable_all_buttons() 
    elif b3["text"] =="X" and b5["text"] =="X" and b7["text"] =="X"  :
            Winner=True
            messagebox.showinfo("tic tac toe","Congratulations!! X player") 
            disable_all_buttons()     
def b_click(b):
    global Clicked ,Count
    
    if b["text"]==" " and Clicked == True:
        b["text"]="X"
        Clicked=False
        Count +=1
        checkifwon()
    elif b["text"]==" " and Clicked == False:
          b["text"]="O"
          Clicked=True
          Count +=1
          checkifwon()
    
            
        
b1=Button(root,text=" ",font =("Helvetica",20),height=3 ,width=6,command=lambda: b_click(b1))
b2=Button(root,text=" ",font =("Helvetica",20),height=3 ,width=6,command=lambda: b_click(b2))
b3=Button(root,text=" ",font =("Helvetica",20),height=3 ,width=6,command=lambda: b_click(b3))

b4=Button(root,text=" ",font =("Helvetica",20),height=3 ,width=6,command=lambda: b_click(b4))
b5=Button(root,text=" ",font =("Helvetica",20),height=3 ,width=6,command=lambda: b_click(b5))
b6=Button(root,text=" ",font =("Helvetica",20),height=3 ,width=6,command=lambda: b_click(b6))

b7=Button(root,text=" ",font =("Helvetica",20),height=3 ,width=6,command=lambda: b_click(b7))
b8=Button(root,text=" ",font =("Helvetica",20),height=3 ,width=6,command=lambda: b_click(b8))
b9=Button(root,text=" ",font =("Helvetica",20),height=3 ,width=6,command=lambda: b_click(b9))

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)
root.mainloop()

def create_board():
    return (np.array([[0,0,0],
                      [0,0,0],
                      [0,0,0]]))
def possibilities(board):
    l = []
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                l.append((i,j))
    return(l)
def random_place(board, player):
    selection = possibilities(board)
    current_loc = random.choice(selection)
    board[current_loc] = player
    return(board)
def col_win(board, player):
    for x in range(len(board)):
        win=True
        for y in range(len(board)):
          if board[y][x] !=player:
            win=False 
            break
        if win==True:
            return (win)
    return(win)
def row_win(board, player):
    for x in range(len(board)):
        win=True
        for y in range(len(board)):
           if board[x,y] !=player:
             win=False 
             break
        if win==True:
            return (win)
    return (win)
def diag_win(board, player):
    win=True
    y=0
    for x in range(len(board)):
        if board[x,x] != player:
            win =False
        if win :
            return win
        win=True
        if win:
            for x in range(len(board)):
                y = len(board) -1-x
                if board[x,y] != player :
                    win =False
            return win
# def evaluate(board):
#     winner=0
#     for player in [1,2]:
#         if (row_win(board,player) or 
#            col_win(board, player) or
#            diag_win(board, player)):
#             winner = player
#     if np.all(board != 0) and winner==0:
#         winner=-1
#     return winner
def play_game():
    board , winner, counter = create_board() , 0 , 1
    # print(board)
    # sleep(2)
    while winner == 0:
        for player in [1,2]:
            board = random_place(board, player)
            print("board after " + str(counter) + "move")
            print(board)
            sleep(2)
            counter +=1
#             winner= evaluate(board)
#             if winner !=0:
#                 break
#     return (winner)
# print("winner is : " + str(play_game()))

        
        

        