from time import sleep
from tkinter import *
import moves
import cube
import kociemba         # "pip install kociemba"


#Display cube face
def show(side):
    #Get the surrounding faces
    surr = {
        0:"2435",
        1:"2534",
        2:"1405",
        3:"0415",
        4:"2130",
        5:"2031",
    }.get(side,dispcube)

    side = cols[side]

    #Decide which face is to be shown
    face = {
        cols[0]:cube.green,
        cols[1]:cube.blue,
        cols[2]:cube.white,
        cols[3]:cube.yellow,
        cols[4]:cube.red,
        cols[5]:cube.orange,
    }.get(side)
    
    #Place the smaller cubes
    n=0
    for i in range(9):
        colour = {
            "g":cols[0],
            "b":cols[1],
            "w":cols[2],
            "y":cols[3],
            "r":cols[4],
            "o":cols[5],
        }.get(face[int(n/3)][int(n%3)])
        
        smallerCUBES[i].config(bg=colour,state="disabled")
        smallerCUBES[i].grid(row=int(n/3),column=int(n%3),padx=2,pady=2)
        n+=1

    #Place the surrounding faces' centers
    Button(dispcube,width=6,height=3,bg=cols[int(surr[0])],state=DISABLED).grid(row=0,column=2,pady = 40)  #top
    Button(dispcube,width=6,height=3,bg=cols[int(surr[1])],state=DISABLED).grid(row=2,column=4,padx = 40)  #right
    Button(dispcube,width=6,height=3,bg=cols[int(surr[2])],state=DISABLED).grid(row=4,column=2,pady = 40)  #bottom
    Button(dispcube,width=6,height=3,bg=cols[int(surr[3])],state=DISABLED).grid(row=2,column=0,padx = 40)  #left

#Solves the current state of cube
def solve(opt, solveMode):
    opt.config(state = "normal")
    solved = "R L U2 R L' B2 U2 R2 F2 L2 D2 L2 F2"
    try:
        solution = kociemba.solve(current_state())
        opt.delete(0,END)
        if solution == solved:
            opt.insert(0,"Cannot Solve a Solved Cube")
        else:
            opt.insert(0,solution)
            if solveMode == 1:
                solution = solution.split(" ")
                for i in solution:
                    if i[-1] == "'":
                        i = i[0].lower()
                    getattr(moves, i)()
                    show(0)
    except:
        opt.delete(0,END)
        opt.insert(0,"Error, Invalid Input!")
    opt.config(state = "readonly")



#Resets the cube
def reset(opt,mode):
    opt.config(state = "normal")
    opt.delete(0,END)
    opt.config(state = "readonly")
    for i in range(3):
        for j in range(3):
            cube.green[i][j] = Cols[0]
    for i in range(3):
        for j in range(3):
            cube.blue[i][j] = Cols[1]
    for i in range(3):
        for j in range(3):
            cube.white[i][j] = Cols[2]
    for i in range(3):
        for j in range(3):
            cube.yellow[i][j] = Cols[3]
    for i in range(3):
        for j in range(3):
            cube.red[i][j] = Cols[4]
    for i in range(3):
        for j in range(3):
            cube.orange[i][j] = Cols[5]
    if not mode.get():
        show(0)
    else:
        show(0)

#Browse mode
def browse(mode):
    if not mode.get():
        for i in smallerCUBES:
            i.config(state="disabled")
    for i in selectors:
        i.config(text = "")

#Activates the selected colour
def selected_colour(mode,c):
    browse(mode)
    global selected
    selected = c
    if not mode.get():
        show(selected)
    else:
        selectors[c].config(text = "~")



#Read current state of the cube
def current_state():
    state = ""
    for i in cube.white:
        for j in i:
            state+=selecttext(j)
    for i in cube.red:
        for j in i:
            state+=selecttext(j)
    for i in cube.green:
        for j in i:
            state+=selecttext(j)
    for i in cube.yellow:
        for j in i:
            state+=selecttext(j)
    for i in cube.orange:
        for j in i:
            state+=selecttext(j)
    for i in cube.blue:
        for j in i:
            state+=selecttext(j)
    return state

#Convert to kociemba format      
def selecttext(c):
    f = {
        "w":"U",
        "r":"R",
        "y":"D",
        "o":"L",
        "g":"F",
        "b":"B",
    }.get(c)
    return f

def main(root):
    global cols,Cols,selected,smallerCUBES,selectors,dispcube
    cols = ["green","blue","white","yellow","red","orange"]
    Cols = ["g","b","w","y","r","o"]
    selected = 0

    #DEFINING FRAMES
    dispcube = LabelFrame(root,padx = 10,pady = 15,text = "THE CUBE: ")
    colourSel = LabelFrame(root,padx = 35,pady = 10,text = "Change Sides: ")
    scramble = LabelFrame(root,text = "Moves: ")
    options = LabelFrame(root,padx = 80,pady = 10)
    output = LabelFrame(root,padx = 2, pady = 2,text = "Solution(Green Front White Top): ")

    #PLACING FRAMES
    dispcube.grid(row = 1, column = 0, rowspan = 4,padx = 10)
    colourSel.grid(row = 1, column = 1,padx = 10,pady = 5)
    scramble.grid(row = 3, column = 1)
    options.grid(row = 4, column = 1,padx = 10)
    output.grid(row = 5, column = 0,padx = 10,pady = 10)




    #COLOUR SELECTOR
    mode = IntVar()
    selectors = [
        Button(colourSel,width=6,height=2,bg=cols[0],command=lambda:selected_colour(mode,0)),
        Button(colourSel,width=6,height=2,bg=cols[1],command=lambda:selected_colour(mode,1)),
        Button(colourSel,width=6,height=2,bg=cols[2],command=lambda:selected_colour(mode,2)),
        Button(colourSel,width=6,height=2,bg=cols[3],command=lambda:selected_colour(mode,3)),
        Button(colourSel,width=6,height=2,bg=cols[4],command=lambda:selected_colour(mode,4)),
        Button(colourSel,width=6,height=2,bg=cols[5],command=lambda:selected_colour(mode,5)),
    ]
    selectors[0].grid(row=0,column=0,padx=5,pady=2)
    selectors[1].grid(row=0,column=1,padx=5,pady=2)
    selectors[2].grid(row=1,column=0,padx=5,pady=2)
    selectors[3].grid(row=1,column=1,padx=5,pady=2)
    selectors[4].grid(row=2,column=0,padx=5,pady=2)
    selectors[5].grid(row=2,column=1,padx=5,pady=2)

    #SCRAMBLER
    Button(scramble,width=2,text = "R",command=lambda: [moves.R(),show(selected)]).grid(row = 0, column = 0)
    Button(scramble,width=2,text = "L",command=lambda: [moves.L(),show(selected)]).grid(row = 0, column = 1)
    Button(scramble,width=2,text = "F",command=lambda: [moves.F(),show(selected)]).grid(row = 0, column = 2)
    Button(scramble,width=2,text = "B",command=lambda: [moves.B(),show(selected)]).grid(row = 0, column = 3)
    Button(scramble,width=2,text = "U",command=lambda: [moves.U(),show(selected)]).grid(row = 0, column = 4)
    Button(scramble,width=2,text = "D",command=lambda: [moves.D(),show(selected)]).grid(row = 0, column = 5)
    Button(scramble,width=2,text = "R'",command=lambda: [moves.r(),show(selected)]).grid(row = 1, column = 0)
    Button(scramble,width=2,text = "L'",command=lambda: [moves.l(),show(selected)]).grid(row = 1, column = 1)
    Button(scramble,width=2,text = "F'",command=lambda: [moves.f(),show(selected)]).grid(row = 1, column = 2)
    Button(scramble,width=2,text = "B'",command=lambda: [moves.b(),show(selected)]).grid(row = 1, column = 3)
    Button(scramble,width=2,text = "U'",command=lambda: [moves.u(),show(selected)]).grid(row = 1, column = 4)
    Button(scramble,width=2,text = "D'",command=lambda: [moves.d(),show(selected)]).grid(row = 1, column = 5)
    Button(scramble,width=2,text = "R2",command=lambda: [moves.R2(),show(selected)]).grid(row = 2, column = 0)
    Button(scramble,width=2,text = "L2",command=lambda: [moves.L2(),show(selected)]).grid(row = 2, column = 1)
    Button(scramble,width=2,text = "F2",command=lambda: [moves.F2(),show(selected)]).grid(row = 2, column = 2)
    Button(scramble,width=2,text = "B2",command=lambda: [moves.B2(),show(selected)]).grid(row = 2, column = 3)
    Button(scramble,width=2,text = "U2",command=lambda: [moves.U2(),show(selected)]).grid(row = 2, column = 4)
    Button(scramble,width=2,text = "D2",command=lambda: [moves.D2(),show(selected)]).grid(row = 2, column = 5)


    #OPTIONS
    Button(options,width=10,text="RESET CUBE",command=lambda:reset(opt,mode)).grid(row=0,column=0)
    Button(options,width=17,text="GENERATE SOLUTION",command=lambda:solve(opt, 0)).grid(row=1,column=0)
    Button(options,width=10,text="AUTO SOLVE",command=lambda:solve(opt, 1)).grid(row=2,column=0)
    #OUTPUT
    opt = Entry(output,width=71,state = "readonly")
    opt.grid(row = 0, column = 0)

    #EXIT
    ex = Button(root,text = "EXIT",command = root.destroy)
    ex.grid(row = 5, column = 1,padx = 10,pady = 10,sticky = W+E)

    #Cube Holder
    holder = LabelFrame(dispcube,bg="black")
    holder.grid(row = 1,column = 1, rowspan = 3, columnspan = 3)

    # small cubes as buttons disbaled by default
    smallerCUBES = [
            Button(holder,width=6,height=3, state="disabled"),
            Button(holder,width=6,height=3, state="disabled"),
            Button(holder,width=6,height=3, state="disabled"),
            Button(holder,width=6,height=3, state="disabled"),
            Button(holder,width=6,height=3, state="disabled"),
            Button(holder,width=6,height=3, state="disabled"),
            Button(holder,width=6,height=3, state="disabled"),
            Button(holder,width=6,height=3, state="disabled"),
            Button(holder,width=6,height=3, state="disabled")
        ]
    show(selected)

if __name__ == "__main__":
    root = Tk()
    main(root)
    root.mainloop()
