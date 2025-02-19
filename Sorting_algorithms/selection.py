import tkinter as tk
from Sorting_algorithms.drawRect import drawRectangle


def selectionSortStep(
    data: list,
    index: int,
    number_of_comparisons: int,
    minimum_index: int,
    first_element_index: int,
    number_of_swaps: int,
) -> tuple:
    """
    Makes exactly one step in the selection sort.
    So it either finds new minimum or does nothing.
    Either way, it increments the number of comparisons by 1.

    Args:
        data (list): The list of elements to be sorted.
        index (int): The current index in the list.
        number_of_comparisons (int): The current number of comparisons made.
        minimum_index (int): The index of the current minimum element.
        first_element_index (int): The index of the first element in the unsorted part.
        number_of_swaps (int): The current number of swaps made.

    Returns:
        tuple: Updated number of comparisons, minimum index, and number of swaps.
    """
    number_of_comparisons += 1  # Increment the number of comparisons

    # Check if the current element is less than the current minimum element
    if data[index] < data[minimum_index]:
        minimum_index = index  # Update the minimum index

    # If we have reached the end of the list
    if index == len(data) - 1:
        # Swap the found minimum element with the first element of the unsorted part
        if data[minimum_index] < data[first_element_index]:
            data[first_element_index], data[minimum_index] = (
                data[minimum_index],
                data[first_element_index],
            )
            number_of_swaps += 1  # Increment the number of swaps
        # Update the minimum index to the next element in the unsorted part
        minimum_index = first_element_index + 1

    # Return the updated number of comparisons, minimum index, and number of swaps
    return number_of_comparisons, minimum_index, number_of_swaps


def drawSelection(
    window,
    data: list,
    index: int,
    number_of_comparisons: int,
    minimum_index: int,
    first_element_index: int,
    number_of_swaps: int,
) -> tuple:
    """
    Draw the partially sorted list after one step of the selection sort.

    Args:
        window: The Tkinter window where the drawing will be displayed.
        data (list): The list of elements to be sorted.
        index (int): The current index in the list.
        number_of_comparisons (int): The current number of comparisons made.
        minimum_index (int): The index of the current minimum element.
        first_element_index (int): The index of the first element in the unsorted part.
        number_of_swaps (int): The current number of swaps made.

    Returns:
        tuple: Updated number of comparisons, minimum index, and number of swaps.
    """
    global width, height  # Define global variables for width and height
    ret = selectionSortStep(
        data,
        index,
        number_of_comparisons,
        minimum_index,
        first_element_index,
        number_of_swaps,
    )  # Perform one step of selection sort
    window.update_idletasks()  # Update the window to get the latest dimensions

    # Calculate the width and height for the canvas
    width = window.winfo_width() // 2 - 25
    height = window.winfo_height() // 2 - 25

    # Create a canvas for drawing the selection sort visualization
    canvas_selection = tk.Canvas(window, width=width, height=height)
    canvas_selection.place(x=width + 1, y=26)  # Place the canvas in the window

    max_data = max(data)  # Get the maximum value in the data list
    min_data = min(data)  # Get the minimum value in the data list

    # Display the number of comparisons on the canvas
    tk.Label(
        canvas_selection, text=f"Number of comparisons: {number_of_comparisons}"
    ).place(x=0, y=0)

    # Display the number of swaps on the canvas
    tk.Label(canvas_selection, text=f"Number of swaps:       {number_of_swaps}").place(
        x=0, y=25
    )

    # Display the title "Selection sort" on the canvas
    tk.Label(canvas_selection, text="Selection sort", font=("Helvetica", 16)).place(
        x=width // 2 - 50, y=0
    )

    # Draw rectangles for each element in the data list
    for i, j in enumerate(data):
        if i == index:
            # Highlight the current index in green
            drawRectangle(
                canvas_selection,
                len(data),
                i,
                "green",
                max_data,
                min_data,
                j,
                width,
                height,
            )
        elif i == minimum_index:
            # Highlight the current minimum index in red
            drawRectangle(
                canvas_selection,
                len(data),
                i,
                "red",
                max_data,
                min_data,
                j,
                width,
                height,
            )
        elif i == first_element_index:
            # Highlight the first element index in purple
            drawRectangle(
                canvas_selection,
                len(data),
                i,
                "purple",
                max_data,
                min_data,
                j,
                width,
                height,
            )
        else:
            # Draw the rest of the elements in blue
            drawRectangle(
                canvas_selection,
                len(data),
                i,
                "blue",
                max_data,
                min_data,
                j,
                width,
                height,
            )

    window.update()  # Update the window to reflect the changes

    # Perform one step of the selection sort and return the updated values
    return ret
