from Sorting_algorithms import *
from copy import deepcopy
import asyncio


def startAsyncMain(master, data):
    # Run the main function using asyncio
    asyncio.run(main(master, data))


async def main(master, data):
    """
    Main function used to run all the functionality of the code.
    """
    # Run selection sort, bubble sort, and insertion sort visualizations concurrently
    await asyncio.gather(
        selection_loop(deepcopy(data), master),
        bubble_loop(deepcopy(data), master),
        insertion_loop(deepcopy(data), master),
    )
    await asyncio.sleep(0)  # Yield control to allow other tasks to run
    for task in asyncio.all_tasks():
        task.cancel()  # Cancel all running tasks


async def bubble_loop(data, master):
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
            await asyncio.sleep(0)


async def selection_loop(data, master):
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
            await asyncio.sleep(0)


async def insertion_loop(data, master):
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
            await asyncio.sleep(0)
