import tkinter as tk
from Sorting_algorithms import *
import random
from copy import deepcopy
import time
from run_normal import main as run_normal
from run_async import startAsyncMain as run_async


WIDTH = 1000
HEIGHT = 800


def initializeScreen():
    global master
    """
    Function that is called exactly once at the start of the program to ensure everything is set up correctly.
    """
    master = tk.Tk()
    master.geometry(f"{WIDTH}x{HEIGHT}")

    main()


def main():
    """
    Main function used to run all the functionality of the code.
    """
    data = list(random.randint(1, 100) for i in range(25))
    drawBubble(master, deepcopy(data), 0, 0, 0)
    drawSelection(master, deepcopy(data), 0, 0, 0, 0, 0)

    def start_sorting():
        if async_var.get():
            run_async(master, deepcopy(data))
        else:
            run_normal(master, deepcopy(data))

    async_var = tk.BooleanVar()
    async_var.set(False)

    switch_frame = tk.Frame(master)
    switch_frame.pack()

    async_button = tk.Checkbutton(switch_frame, text="Run Async", variable=async_var)
    async_button.pack(side=tk.LEFT)

    start_button = tk.Button(switch_frame, text="Start Sorting", command=start_sorting)
    start_button.pack(side=tk.LEFT)
    master.mainloop()


if __name__ == "__main__":
    initializeScreen()
