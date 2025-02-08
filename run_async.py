from Sorting_algorithms import *
from copy import deepcopy
import asyncio

WIDTH = 1000
HEIGHT = 800


def startAsyncMain(master, data):
    asyncio.run(main(master, data))


async def main(master, data):
    """
    Main function used to run all the functionality of the code.
    """
    await asyncio.gather(
        selection_loop(deepcopy(data), master), bubble_loop(deepcopy(data), master)
    )
    await asyncio.sleep(0)  # Yield control to allow other tasks to run
    for task in asyncio.all_tasks():
        task.cancel()  # Cancel all running tasks


async def bubble_loop(data, master):
    number_of_comparisons = number_of_swaps = 0
    for i in range(len(data) - 1):
        for j in range(0, len(data) - 1 - i):
            number_of_comparisons, number_of_swaps = drawBubble(
                master, data, j, number_of_comparisons, number_of_swaps
            )
            await asyncio.sleep(0)  # Yield control to allow other tasks to run


async def selection_loop(data, master):
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
            await asyncio.sleep(0)  # Yield control to allow other tasks to run
