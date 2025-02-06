import tkinter as tk
from Sorting_algorithms import *
import random
from copy import deepcopy
import time

WIDTH = 1000
HEIGHT = 800


def main(master, data):
    """
    Main function used to run all the functionality of the code.
    """
    selection_loop(deepcopy(data), master)
    bubble_loop(deepcopy(data), master)
    master.mainloop()


def bubble_loop(data, master):
    number_of_comparisons = number_of_swaps = 0
    for i in range(len(data) - 1):
        for j in range(0, len(data) - 1 - i):
            number_of_comparisons, number_of_swaps = drawBubble(
                master, data, j, number_of_comparisons, number_of_swaps
            )


def selection_loop(data, master):
    number_of_comparisons = 0
    minimum_index = number_of_swaps = 0
    for i in range(len(data)):
        for j in range(i, len(data)):
            number_of_comparisons, minimum_index, number_of_swaps = drawSelection(
                master,
                data,
                j,
                number_of_comparisons,
                minimum_index,
                i,
                number_of_swaps,
            )
