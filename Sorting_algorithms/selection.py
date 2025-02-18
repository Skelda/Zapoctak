import tkinter as tk


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

    window.update_idletasks()  # Update the window to get the latest dimensions

    # Calculate the width and height for the canvas
    width = window.winfo_width() // 2 - 25
    height = window.winfo_height() // 2 - 25

    # Create a canvas for drawing the selection sort visualization
    canvas_selection = tk.Canvas(window, width=width, height=height)
    canvas_selection.place(x=width + 1, y=26)  # Place the canvas in the window

    max_data = max(data)  # Get the maximum value in the data list for scaling purposes

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
            drawRectangle(canvas_selection, len(data), i, "green", max_data, j)
        elif i == minimum_index:
            # Highlight the current minimum index in red
            drawRectangle(canvas_selection, len(data), i, "red", max_data, j)
        elif i == first_element_index:
            # Highlight the first element index in purple
            drawRectangle(canvas_selection, len(data), i, "purple", max_data, j)
        else:
            # Draw the rest of the elements in blue
            drawRectangle(canvas_selection, len(data), i, "blue", max_data, j)

    window.update()  # Update the window to reflect the changes

    # Perform one step of the selection sort and return the updated values
    return selectionSortStep(
        data,
        index,
        number_of_comparisons,
        minimum_index,
        first_element_index,
        number_of_swaps,
    )


def drawRectangle(
    canvas, number_of_rects: int, position: int, color, max_data: int, cur_data: int
) -> None:
    """
    Draw a rectangle representing an element in the list.

    Args:
        canvas (tk.Canvas): The canvas where the rectangle will be drawn.
        number_of_rects (int): The total number of rectangles to be drawn.
        position (int): The position of the current rectangle.
        color (str): The color of the rectangle.
        max_data (int): The maximum value in the data list.
        cur_data (int): The current value of the element being drawn.
    """
    rect_width = width // number_of_rects  # Calculate the width of each rectangle

    height_scaling = height // max_data  # Calculate the height scaling factor

    # Draw the rectangle on the canvas with the specified position, size, and color
    canvas.create_rectangle(
        (position) * rect_width,  # x-coordinate of the top-left corner
        400 - height_scaling * cur_data,  # y-coordinate of the top-left corner
        (position + 1) * rect_width,  # x-coordinate of the bottom-right corner
        400,  # y-coordinate of the bottom-right corner
        fill=color,  # fill color of the rectangle
    )
