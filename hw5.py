import cs112_f17_week5_linter
from tkinter import *
from sudoku import *
import string
import copy
#sohan kalva skalva
#########################################################
# Customize these functions
# You will need to write many many helper functions, too.
#########################################################

def init(data):
    #initialize all of the the variables used
    data.high_r = 0
    data.high_c = 0
    data.origin_board = copy.deepcopy(data.board)
    data.margin = 10
    data.over = False
    
def keyPressed(event, data):
    # use event.char and event.keysym
    #checks to see if the board is full and all correct
    if(data.over == False):
        if (event.keysym == "Left"):
            moveLeft(data)
        elif (event.keysym == "Right"):
            moveRight(data)
        elif (event.keysym == "Down"):
            moveDown(data)
        elif (event.keysym == "Up"):
            moveUp(data)
        #checks to see if a number was inserted
        elif (event.keysym in string.digits and not(event.keysym == "0")):
            if(data.board[data.high_c][data.high_r] == 0):
                data.board[data.high_c][data.high_r] = int(event.keysym)
                #checks if the number inserted was legal
                if not (isLegalSudoku(data.board)):
                    data.board[data.high_c][data.high_r] = 0
        #checks if backspace was pressed
        elif(event.keysym == "BackSpace" and 
            data.origin_board[data.high_c][data.high_r] == 0):
                data.board[data.high_c][data.high_r] = 0            

def gameOver(canvas,data):
    #keeps track of if the game is over or not
    if(isLegalSudoku(data.board)):
       zero_count = 0
       for i in data.board:
            for j in i:
                if j == 0:
                    zero_count += 1
    if(zero_count == 0):
        canvas.create_text(data.width/2, data.height/2,
                            text = "CONGRATS YOU WON",font="Arial 30 bold",
        fill = "gold")
        data.over = True  
    
            
def moveLeft(data):
    data.high_r -= 1
    if(data.high_r < 0):
        data.high_r = 8

def moveRight(data):
    data.high_r += 1
    if(data.high_r > 8):
        data.high_r = 0

def moveUp(data):
    data.high_c -= 1
    if(data.high_c < 0):
        data.high_c = 8

def moveDown(data):
    data.high_c += 1
    if(data.high_c > 8):
        data.high_c = 0

def drawBoard(canvas,data):
    x = (data.width) / 9
    y = (data.height)/9
    #loops through the 2D list and creates each individual square
    for i in range(len(data.board)):
        for j in range(len(data.board[i])):
            canvas.create_rectangle((data.width/9*i),
                                    (data.height/9*j),
                                  (data.width/9*(i+1)),
                                  data.height/9*(j+1)
                                  ,fill = 'white')
            if(i == data.high_r and j == data.high_c):
                canvas.create_rectangle((x*i),(y*j),
                                    (x*(i+1)),y*(j+1),
                                    fill = 'yellow')   
    #creates bold border for the whole board
    canvas.create_rectangle(5,5, 500,500,width = 5)
    #creates the bold lines
    #for k in range(3)k),0,(y*3*(k)),500
    #                              ,width = 5)
    #        canvas.create_line(0,x*3*k,500,y*3*k
    #                              ,width = 5)
    

def fill(canvas, data):
    #fills the board with the values from the given sudoku board
    for r in range(len(data.board)):
        for c in range(len(data.board[r])):
            if(data.board[r][c] != 0):
                #differenicates the colors from those that are provided
                #to those the user inputed 
                if(data.board[r][c] == data.origin_board[r][c]):
                    canvas.create_text(data.width/9 * c + 28, data.height/9 * 
                    r + 28,text = data.board[r][c],font="Arial 25 bold",
                    fill = "blue")
                else:
                    canvas.create_text(data.width/9 * c + 28, data.height/9 * 
                    r + 28,text = data.board[r][c],font="Arial 25 bold",
                    fill = "black")

def redrawAll(canvas,data):
    drawBoard(canvas, data)
    fill(canvas,data)
    gameOver(canvas,data)
    
########################################
# Do not modify the playSudoku function.
########################################

def playSudoku(sudokuBoard, width=500, height=500):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.board = sudokuBoard
    # Initialize any other things you want to store in data
    init(data)

    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()

    # set up events
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))

    # Draw the initial screen
    redrawAll(canvas, data)
    # Start the event loop
    root.mainloop()  # blocks until window is closed
    print("bye!")

def main():
    cs112_f17_week5_linter.lint() # check style rules
    
    board = [
            [ 5, 3, 0, 6, 7, 8, 9, 1, 2 ],
            [ 6, 7, 2, 1, 9, 5, 3, 4, 8 ],
            [ 1, 9, 8, 3, 4, 2, 5, 6, 7 ],
            [ 8, 5, 9, 7, 6, 1, 4, 2, 3 ],
            [ 4, 2, 6, 8, 5, 3, 7, 9, 1 ],
            [ 7, 1, 3, 9, 2, 4, 8, 5, 6 ],
            [ 9, 6, 1, 5, 3, 7, 2, 8, 4 ],
            [ 2, 8, 7, 4, 1, 9, 6, 3, 5 ],
            [ 3, 4, 5, 2, 8, 6, 1, 7, 9 ]
        ]
    playSudoku(board)
#test insert
if __name__ == '__main__':
    main()
