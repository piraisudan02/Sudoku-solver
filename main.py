from tkinter import *
root=Tk()
root.minsize(500,500)
root.title("Sudoku solver")
frame = Frame(root, highlightthickness=1,padx=30,bg="cyan")
frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=400)
label=Label(frame,text="Fill and Click Solve",font=("fantansy",17),bg="cyan").grid(row=0,column=1,columnspan=10)

errLabel=Label(frame,text="",fg="red",bg="cyan")
errLabel.grid(row=15,column=1,columnspan=10,pady=5)

solvedLabel=Label(frame,text="",fg="green",bg="cyan")
solvedLabel.grid(row=15,column=1,columnspan=10,pady=5)
def validcheck(board,row,col,c):
    column,rows,square=0,0,0
    for i in range(9):
        if board[i][col]==c:
            column+=1
        if board[row][i]==c:
            rows+=1
        if board[3*(row//3)+i//3][3*(col//3)+i%3]==c:
            square+=1
    if column==1 and rows==1 and square==1:
        return True
    return False

def isvalid(board,row,col,c):
    for i in range(9):
        if board[i][col]==c:
            return False
        if board[row][i]==c:
            return False
        if board[3*(row//3)+i//3][3*(col//3)+i%3]==c:
            return False
    return True

def solver(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                for k in range(1,10):
                    if isvalid(board,i,j,k):
                        board[i][j]=k
                        if solver(board):
                            return True
                        else:
                            board[i][j]=0
                return False
    return True

def start(board):
    if solver(board):
        return board
    return False
cells={}

def ValidateNumber(p):
    if (p.isdigit() or p=="") and len(p)<2:
        return True
    return False

reg=frame.register(ValidateNumber)

def draw(row,column,bgcolor,fcolor):
    for i in range(3):
        for j in range(3):
            e=Entry(frame,width=5,bg=bgcolor,foreground=fcolor,insertbackground=fcolor,justify="center",validate="key",validatecommand=(reg,"%P"))
            e.grid(row=row+i+1,column=column+j+1,sticky="nsew",padx=1,pady=1,ipady=5)
            cells[row+i+1,column+j+1]=e

def draw9X9():
    color="black"
    fcolor="white"
    for row in range(1,10,3):
        for col in range(0,9,3):
            draw(row,col,color,fcolor)
            if color=="black":
                color="white"
                fcolor="black"
            else:
                color="black"
                fcolor="white"

def clearValues():
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for r in range(2,11):
        for c in range(1,10):
            cell=cells[(r,c)]
            if cell!="":
                cell.delete(0,"end")

def getValues():
    board=[]
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for r in range(2,11):
        rows=[]
        for c in range(1,10):
            val=cells[(r,c)].get()
            if val=="":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)

    valid(board)

solvebtn=Button(frame,command=getValues,text="Solve",width=10,bg="black",foreground="white")
solvebtn.grid(row=20,column=1,columnspan=5,pady=20)

clearbtn=Button(frame,command=clearValues,text="Clear",width=10,bg="black",foreground="white")
clearbtn.grid(row=20,column=5,columnspan=5,pady=20)



# def update(s):
#     sol=start(s)
#     if sol==False:
#         print("no")
#     else:
#         print(s)

def valid(s):
    for i in range(9):
        for j in range(9):
            if s[i][j]!=0:
                if not validcheck(s,i,j,s[i][j]):
                    errLabel.configure(text="NO solution for the sudoku")
                    return
    update(s)

def changeOnHover1(button, colorOnHover, colorOnLeave):
 
    # adjusting background of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover,
        foreground="black"))
 
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave,
        foreground="white"))    

def update(s):
    sol=start(s)
    for r in range(2,11):
        for c in range(1,10):
            cells[(r,c)].delete(0,"end")
            cells[(r,c)].insert(0,sol[r-2][c-1])
    solvedLabel.configure(text="sudoku solved")

draw9X9()
changeOnHover1(solvebtn, "white", "black")
changeOnHover1(clearbtn, "white", "black")
frame.mainloop()
