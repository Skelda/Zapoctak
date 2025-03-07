import tkinter as tk
from Sorting_algorithms.drawRect import drawRectangle


def insertionSortStep(
    data: list,
    index: int,
    number_of_comparisons: int,
    number_of_swaps: int,
    should_break: bool = False,
) -> tuple:
    """
    Makes exactly one step in the insertion sort.
    So it either swaps two elements or does nothing.
    Either way, it increments the number of comparisons by 1.

    Args:
        data (list): The list of elements to be sorted.
        index (int): The current index in the list.
        number_of_comparisons (int): The current number of comparisons made.
        number_of_swaps (int): The current number of swaps made.
        should_break (bool): Flag to indicate if the sorting should stop.

    Returns:
        tuple: Updated number of comparisons, number of swaps, and should_break flag.
    """
    number_of_comparisons += 1  # Increment the number of comparisons
    if data[index + 1] < data[index]:  # Compare adjacent elements
        data[index], data[index + 1] = (
            data[index + 1],
            data[index],
        )  # Swap if out of order
        number_of_swaps += 1  # Increment the number of swaps
    else:
        should_break = True  # Set should_break to True if no swap is needed
    return number_of_comparisons, number_of_swaps, should_break  # Return updated values


def drawInsertion(
    window, data: list, index: int, number_of_comparisons: int, number_of_swaps: int
) -> tuple:
    """
    Draw the partially sorted list after one step of the insertion sort.

    Args:
        window: The Tkinter window where the drawing will be displayed.
        data (list): The list of elements to be sorted.
        index (int): The current index in the list.
        number_of_comparisons (int): The current number of comparisons made.
        number_of_swaps (int): The current number of swaps made.

    Returns:
        tuple: Updated number of comparisons, number of swaps, and should_break flag.
    """
    global width, height
    ret = insertionSortStep(
        data, index, number_of_comparisons, number_of_swaps
    )  # Perform one step of insertion sort
    window.update_idletasks()  # Update the window to get the latest dimensions
    width = window.winfo_width() // 2 - 25  # Calculate the canvas width
    height = window.winfo_height() // 2 - 25  # Calculate the canvas height
    canvas_insertion = tk.Canvas(
        window, width=width, height=height
    )  # Create a new canvas
    canvas_insertion.place(x=0, y=height + 26)  # Place the canvas in the window
    max_data = max(data)  # Find the maximum value in the data list
    min_data = min(data)  # Get the minimum value in the data list

    tk.Label(
        canvas_insertion, text=f"Number of comparisons: {number_of_comparisons}"
    ).place(
        x=0, y=0
    )  # Display the number of comparisons
    tk.Label(canvas_insertion, text=f"Number of swaps:       {number_of_swaps}").place(
        x=0, y=25
    )  # Display the number of swaps
    tk.Label(canvas_insertion, text="Insertion sort", font=("Helvetica", 16)).place(
        x=width // 2 - 50, y=0
    )  # Display the title "Insertion sort"
    for i, j in enumerate(data):  # Iterate over the data list
        if i == index:
            drawRectangle(
                canvas_insertion,
                len(data),
                i,
                "green",
                max_data,
                min_data,
                j,
                width,
                height,
            )  # Highlight the current index in green
        elif i == index + 1:
            drawRectangle(
                canvas_insertion,
                len(data),
                i,
                "red",
                max_data,
                min_data,
                j,
                width,
                height,
            )  # Highlight the next index in red
        else:
            drawRectangle(
                canvas_insertion,
                len(data),
                i,
                "blue",
                max_data,
                min_data,
                j,
                width,
                height,
            )  # Draw other elements in blue

    window.update()  # Update the window to reflect changes
    return ret
