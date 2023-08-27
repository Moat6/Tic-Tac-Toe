from tkinter import *

# STARTING VALUES

o_score = 0
x_score = 0
draw_score = 0
user = "O"
last_user = None
board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# --------------------MIND-------------------#

def check() :
    global o_score, x_score, draw_score, user
    game_status = mind()
    if game_status == "WIN" :
        if last_user == "O" :
            o_score += 1
            winning_label.config(text=f"O WINS")
            o_score_label.config(text=f"O: {o_score}")
            user = "O"
        else :
            x_score += 1
            winning_label.config(text=f"X WINS")
            x_score_label.config(text=f"X: {x_score}")
            user = "X"
        disable_board()
        root.after(2000,reset_board)
    if game_status == "DRAW" :
        draw_score += 1
        draw_label.config(text=f"Draw: {draw_score}")
        winning_label.config(text=f"DRAW")
        user = "O"
        disable_board()
        root.after(2000,reset_board)



def reset_board() :
    global board, user, last_user
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    user = last_user
    
    one_one.config(image=white_img)
    one_two.config(image=white_img)
    one_three.config(image=white_img)
    two_one.config(image=white_img)
    two_two.config(image=white_img)
    two_three.config(image=white_img)
    three_one.config(image=white_img)
    three_two.config(image=white_img)
    three_three.config(image=white_img)

    colour_board()

    winning_label.config(text=f"")

    enable_board()


def mind() :
    if board[0][0] == board[0][1] == board[0][2]  \
    or board[1][0] == board[1][1] == board[1][2]  \
    or board[2][0] == board[2][1] == board[2][2]  \
    or board[0][0] == board[1][0] == board[2][0]  \
    or board[0][1] == board[1][1] == board[2][1]  \
    or board[0][2] == board[1][2] == board[2][2]  \
    or board[0][0] == board[1][1] == board[2][2]  \
    or board[0][2] == board[1][1] == board[2][0]  :
        return "WIN"
    
    count=0
    for row in board :
        for value in row :
            if value in range(1,10) :
                count+=1
    if count == 0 :
        return "DRAW"


def one_one_press():
    global board, user, last_user
    if board[0][0] == 1 :
        if user == "O" :
            board[0][0]="O"
            one_one.config(image=o_img)
            last_user = "O"
            user = "X"
            colour_board()
        else :
            board[0][0]="X"
            one_one.config(image=x_img)
            last_user = "X"
            user = "O"
            colour_board()
        check()


def one_two_press():
    global board, user, last_user
    if board[0][1] == 2 :
        if user == "O" :
            board[0][1]="O"
            one_two.config(image=o_img)
            last_user = "O"
            user = "X"
            colour_board()
        else :
            board[0][1]="X"
            one_two.config(image=x_img)
            last_user = "X"
            user = "O"
            colour_board()
        check()


def one_three_press():
    global board, user, last_user
    if board[0][2] == 3 :
        if user == "O" :
            board[0][2]="O"
            one_three.config(image=o_img)
            last_user = "O"
            user = "X"
            colour_board()
        else :
            board[0][2]="X"
            one_three.config(image=x_img)
            last_user = "X"
            user = "O"
            colour_board()
        check()


def two_one_press():
    global board, user, last_user
    if board[1][0] == 4 :
        if user == "O" :
            board[1][0]="O"
            two_one.config(image=o_img)
            last_user = "O"
            user = "X"
            colour_board()
        else :
            board[1][0]="X"
            two_one.config(image=x_img)
            last_user = "X"
            user = "O"
            colour_board()
        check()


def two_two_press():
    global board, user, last_user
    if board[1][1] == 5 :
        if user == "O" :
            board[1][1]="O"
            two_two.config(image=o_img)
            last_user = "O"
            user = "X"
            colour_board()
        else :
            board[1][1]="X"
            two_two.config(image=x_img)
            last_user = "X"
            user = "O"
            colour_board()
        check()


def two_three_press():
    global board, user, last_user
    if board[1][2] == 6 :
        if user == "O" :
            board[1][2]="O"
            two_three.config(image=o_img)
            last_user = "O"
            user = "X"
            colour_board()
        else :
            board[1][2]="X"
            two_three.config(image=x_img)
            last_user = "X"
            user = "O"
            colour_board()
        check()


def three_one_press():
    global board, user, last_user
    if board[2][0] == 7 :
        if user == "O" :
            board[2][0]="O"
            three_one.config(image=o_img)
            last_user = "O"
            user = "X"
            colour_board()
        else :
            board[2][0]="X"
            three_one.config(image=x_img)
            last_user = "X"
            user = "O"
            colour_board()
        check()


def three_two_press():
    global board, user, last_user
    if board[2][1] == 8 :
        if user == "O" :
            board[2][1]="O"
            three_two.config(image=o_img)
            last_user = "O"
            user = "X"
            colour_board()
        else :
            board[2][1]="X"
            three_two.config(image=x_img)
            last_user = "X"
            user = "O"
            colour_board()
        check()


def three_three_press():
    global board, user, last_user
    if board[2][2] == 9 :
        if user == "O" :
            board[2][2]="O"
            three_three.config(image=o_img)
            last_user = "O"
            user = "X"
            colour_board()
        else :
            board[2][2]="X"
            three_three.config(image=x_img)
            last_user = "X"
            user = "O"
            colour_board()
        check()

def colour_board() :
    if user == "O" :
        o_score_label.config(fg="#FF2E63")
        x_score_label.config(fg="#EEEEEE")
    else :
        o_score_label.config(fg="#EEEEEE")
        x_score_label.config(fg="#FF2E63")
        

def disable_board() :
    one_one.config(state="disabled")
    one_two.config(state="disabled")
    one_three.config(state="disabled")
    two_one.config(state="disabled")
    two_two.config(state="disabled")
    two_three.config(state="disabled")
    three_one.config(state="disabled")
    three_two.config(state="disabled")
    three_three.config(state="disabled")

def enable_board() :
    one_one.config(state="normal")
    one_two.config(state="normal")
    one_three.config(state="normal")
    two_one.config(state="normal")
    two_two.config(state="normal")
    two_three.config(state="normal")
    three_one.config(state="normal")
    three_two.config(state="normal")
    three_three.config(state="normal")


# --------------------UI------------------- #


root = Tk()

root.title("Tic Tac Toe")
root.config(bg="#222831", padx=20)

x_img = PhotoImage(file="x.png")
o_img = PhotoImage(file="o.png")
white_img= PhotoImage(file="white.png")

# BUTTON
one_one = Button(width=100, height=100, image=white_img, bg="#00ADB5", command=one_one_press)
one_one.grid(row=1,column=1)

one_two = Button(width=100, height=100, image=white_img, bg="#00ADB5", command=one_two_press)
one_two.grid(row=1,column=2)

one_three = Button(width=100, height=100, image=white_img, bg="#00ADB5", command=one_three_press)
one_three.grid(row=1,column=3)

two_one = Button(width=100, height=100, image=white_img, bg="#00ADB5", command=two_one_press)
two_one.grid(row=2,column=1)

two_two = Button(width=100, height=100, image=white_img, bg="#00ADB5", command=two_two_press)
two_two.grid(row=2,column=2)

two_three = Button(width=100, height=100, image=white_img, bg="#00ADB5", command=two_three_press)
two_three.grid(row=2,column=3)

three_one = Button(width=100, height=100, image=white_img, bg="#00ADB5", command=three_one_press)
three_one.grid(row=3,column=1)

three_two = Button(width=100, height=100, image=white_img, bg="#00ADB5", command=three_two_press)
three_two.grid(row=3,column=2)

three_three = Button(width=100, height=100, image=white_img, bg="#00ADB5", command=three_three_press)
three_three.grid(row=3,column=3)

# LABELS
x_score_label = Label(text=f"X: {x_score}", font=("arial",25,"bold"), bg="#222831", fg="#EEEEEE")
x_score_label.grid(row=0, column=1, sticky=W, pady=5)

o_score_label = Label(text=f"O: {o_score}", font=("arial",25,"bold"), bg="#222831", fg="#FF2E63")
o_score_label.grid(row=0, column=3, sticky=E)

draw_label=Label(text=f"Draw: {draw_score}", font=("arial",20,"bold"), bg="#222831", fg="#00ADB5")
draw_label.grid(row=0, column=1, columnspan=3)

winning_label = Label(font=("arial",35,"bold"), bg="#222831", fg="#EEEEEE")
winning_label.grid(row=4, column=1, columnspan=3)


check()

root.mainloop()

