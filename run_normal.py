from Sorting_algorithms import *
from copy import deepcopy


def main(master, data):
    """
    Main function used to run all the functionality of the code.
    """
    # Run selection sort visualization
    selection_loop(deepcopy(data), master)
    # Run bubble sort visualization
    bubble_loop(deepcopy(data), master)
    # Run insertion sort visualization
    insertion_loop(deepcopy(data), master)


def bubble_loop(data, master):
    """
    Function to visualize the bubble sort algorithm.
    """
    number_of_comparisons = number_of_swaps = 0
    # Loop through each element in the data
    for i in range(len(data) - 1):
        # Loop to compare adjacent elements
        for j in range(0, len(data) - 1 - i):
            # Visualize the bubble sort step and update comparisons and swaps
            number_of_comparisons, number_of_swaps = drawBubble(
                master, data, j, number_of_comparisons, number_of_swaps
            )


def selection_loop(data, master):
    """
    Function to visualize the selection sort algorithm.
    """
    number_of_comparisons = 0
    minimum_index = number_of_swaps = 0
    # Loop through each element in the data
    for i in range(len(data)):
        # Loop to find the minimum element in the unsorted part
        for j in range(i, len(data)):
            # Visualize the selection sort step and update comparisons, minimum index, and swaps
            number_of_comparisons, minimum_index, number_of_swaps = drawSelection(
                master,
                data,
                j,
                number_of_comparisons,
                minimum_index,
                i,
                number_of_swaps,
            )


def insertion_loop(data, master):
    """
    Function to visualize the insertion sort algorithm.
    """
    number_of_comparisons = number_of_swaps = 0
    # Loop through each element in the data
    for i in range(0, len(data) - 1):
        # Loop to insert the element in the correct position
        for j in range(i, -1, -1):
            # Visualize the insertion sort step and update comparisons and swaps
            number_of_comparisons, number_of_swaps, should_break = drawInsertion(
                master, data, j, number_of_comparisons, number_of_swaps
            )
            # Break if the element is in the correct position
            if should_break:
                break
