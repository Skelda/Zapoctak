import tkinter as tk


def insertionSortStep(
    data: list, index: int, number_of_comparisons, number_of_swaps, should_break=False
) -> list:
    """
    Makes exactly one step in the insertion sort.
    So it either swaps two elements or does nothing.
    Either way, it increments the number of comparisons by 1.
    """
    number_of_comparisons += 1
    if data[index + 1] < data[index]:
        data[index], data[index + 1] = data[index + 1], data[index]
        number_of_swaps += 1
    else:
        should_break = True
    return number_of_comparisons, number_of_swaps, should_break


def drawInsertion(
    window, data: list, index, number_of_comparisons, number_of_swaps
) -> None:
    """
    Draw the partially sorted list after one step of the insertion sort.
    """
    window.update_idletasks()
    width = window.winfo_width() // 2 - 25
    height = window.winfo_height() // 2 - 25
    canvas_bubble = tk.Canvas(window, width=width, height=height)
    canvas_bubble.place(x=0, y=height + 26)
    max_data = max(data)
    tk.Label(
        canvas_bubble, text=f"Number of comparisons: {number_of_comparisons}"
    ).place(x=0, y=0)
    tk.Label(canvas_bubble, text=f"Number of swaps:       {number_of_swaps}").place(
        x=0, y=25
    )
    for i, j in enumerate(data):
        if i == index:
            drawRectangle(canvas_bubble, len(data), i, "green", max_data, j)
        elif i == index + 1:
            drawRectangle(canvas_bubble, len(data), i, "red", max_data, j)
        else:
            drawRectangle(canvas_bubble, len(data), i, "blue", max_data, j)

    window.update()
    return insertionSortStep(data, index, number_of_comparisons, number_of_swaps)


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
