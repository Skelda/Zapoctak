import tkinter as tk


def bubbleSortStep(data: list, index: int) -> list:
    """
    Makes exactly one step in the bubble sort.
    So it either swaps two elements or jus increases
    the index.
    """
    if data[index] > data[index + 1]:
        data[index], data[index + 1] = data[index + 1], data[index]

    if index < len(data):
        index += 1
    else:
        index = 0

    return data


def drawBubble(window, data: list, index) -> None:
    """
    Draw the partially sorted list after one step of the bubble sort.
    """
    canvas = tk.Canvas(window, width=500, height=400)
    canvas.place(x=0, y=0)
    rect_width = 500 // len(data)
    height_scaling = 400 // max(data)
    for i, j in enumerate(data):
        canvas.create_rectangle(
            (i) * rect_width,
            400 - height_scaling * j,
            (i + 1) * rect_width,
            400,
            fill="blue",
        )

    canvas.create_rectangle(
        (index) * rect_width,  # x1
        400 - height_scaling * data[index],  # y1
        (index + 1) * rect_width,  # x2
        400,  # y2
        fill="blue",  # Color
    )
    window.update()
    return bubbleSortStep(data, index + 1)
