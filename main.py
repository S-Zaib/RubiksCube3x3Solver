from tkinter import *
import solver

if __name__ == "__main__":
    window = Tk()
    window.title("Rubiks Cube Solver!")
    window.geometry("800x600")
    solver.main(window)
    window.mainloop()
