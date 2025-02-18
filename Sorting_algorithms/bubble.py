import tkinter as tk


def bubbleSortStep(
    data: list, index: int, number_of_comparisons: int, number_of_swaps: int
) -> tuple:
    """
    Makes exactly one step in the bubble sort.
    So it either swaps two elements or does nothing.
    Either way, it increments the number of comparisons by 1.

    Args:
        data (list): The list of elements to be sorted.
        index (int): The current index in the list.
        number_of_comparisons (int): The current number of comparisons made.
        number_of_swaps (int): The current number of swaps made.

    Returns:
        tuple: Updated number of comparisons and number of swaps
    """
    number_of_comparisons += 1  # Increment the number of comparisons
    if data[index] > data[index + 1]:  # Compare adjacent elements
        data[index], data[index + 1] = data[index + 1], data[index]  # Swap if needed
        number_of_swaps += 1  # Increment the number of swaps

    return number_of_comparisons, number_of_swaps  # Return updated counts


def drawBubble(
    window, data: list, index: int, number_of_comparisons: int, number_of_swaps: int
) -> tuple:
    """
    Draw the partially sorted list after one step of the bubble sort.

    Args:
        window: The Tkinter window where the drawing will be displayed.
        data (list): The list of elements to be sorted.
        index (int): The current index in the list.
        number_of_comparisons (int): The current number of comparisons made.
        number_of_swaps (int): The current number of swaps made.

    Returns:
        tuple: Updated number of comparisons, number of swaps.
    """
    global width, height
    window.update_idletasks()  # Update the window to get the latest dimensions
    width = window.winfo_width() // 2 - 25  # Calculate canvas width
    height = window.winfo_height() // 2 - 25  # Calculate canvas height
    canvas_bubble = tk.Canvas(window, width=width, height=height)  # Create a canvas
    canvas_bubble.place(x=0, y=26)  # Place the canvas in the window
    max_data = max(data)  # Get the maximum value in the data list

    # Display the number of comparisons and swaps
    tk.Label(
        canvas_bubble, text=f"Number of comparisons: {number_of_comparisons}"
    ).place(x=0, y=0)
    tk.Label(canvas_bubble, text=f"Number of swaps:       {number_of_swaps}").place(
        x=0, y=25
    )

    # Display the title "Bubble sort"
    tk.Label(canvas_bubble, text="Bubble sort", font=("Helvetica", 16)).place(
        x=width // 2 - 50, y=0
    )

    # Draw each rectangle representing the data
    for i, j in enumerate(data):
        if i == index:
            drawRectangle(
                canvas_bubble, len(data), i, "green", max_data, j
            )  # Current element
        elif i == index + 1:
            drawRectangle(
                canvas_bubble, len(data), i, "red", max_data, j
            )  # Next element
        else:
            drawRectangle(
                canvas_bubble, len(data), i, "blue", max_data, j
            )  # Other elements

    window.update()  # Update the window to reflect changes
    return bubbleSortStep(
        data, index, number_of_comparisons, number_of_swaps
    )  # Perform a bubble sort step


def drawRectangle(
    canvas, number_of_rects: int, position: int, color, max_data: int, cur_data: int
) -> None:
    """
    Draw a single rectangle on the canvas.

    Args:
        canvas: The canvas where the rectangle will be drawn.
        number_of_rects (int): The total number of rectangles to be drawn.
        position (int): The position of the current rectangle.
        color: The color of the rectangle.
        max_data (int): The maximum value in the data list.
        cur_data (int): The current value of the element being drawn.

    Returns:
        None
    """
    rect_width = width // number_of_rects  # Calculate the width of each rectangle
    height_scaling = height // max_data  # Calculate the height scaling factor
    canvas.create_rectangle(
        (position) * rect_width,
        400 - height_scaling * cur_data,
        (position + 1) * rect_width,
        400,
        fill=color,
    )  # Draw the rectangle
