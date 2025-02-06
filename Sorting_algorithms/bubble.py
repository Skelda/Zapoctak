import tkinter as tk


def bubbleSortStep(
    data: list, index: int, number_of_comparisons, number_of_swaps
) -> list:
    """
    Makes exactly one step in the bubble sort.
    So it either swaps two elements or does nothing.
    Either way, it increments the number of comparisons by 1.
    """
    number_of_comparisons += 1
    if data[index] > data[index + 1]:
        data[index], data[index + 1] = data[index + 1], data[index]
        number_of_swaps += 1

    return number_of_comparisons, number_of_swaps


def drawBubble(
    window, data: list, index, number_of_comparisons, number_of_swaps
) -> None:
    """
    Draw the partially sorted list after one step of the bubble sort.
    """
    canvas = tk.Canvas(window, width=500, height=400)
    canvas.place(x=0, y=0)
    max_data = max(data)
    tk.Label(canvas, text=f"Number of comparisons: {number_of_comparisons}").place(
        x=0, y=0
    )
    tk.Label(canvas, text=f"Number of swaps:       {number_of_swaps}").place(x=0, y=25)
    for i, j in enumerate(data):
        if i == index:
            drawRectangle(canvas, len(data), i, "green", max_data, j)
        elif i == index + 1:
            drawRectangle(canvas, len(data), i, "red", max_data, j)
        else:
            drawRectangle(canvas, len(data), i, "blue", max_data, j)

    window.update()
    return bubbleSortStep(data, index, number_of_comparisons, number_of_swaps)


def drawRectangle(canvas, number_of_rects, position, color, max_data, cur_data):
    rect_width = 500 // number_of_rects
    height_scaling = 400 // max_data
    canvas.create_rectangle(
        (position) * rect_width,
        400 - height_scaling * cur_data,
        (position + 1) * rect_width,
        400,
        fill=color,
    )
