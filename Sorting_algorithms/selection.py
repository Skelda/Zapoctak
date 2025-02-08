import tkinter as tk


def selectionSortStep(
    data: list,
    index: int,
    number_of_comparisons,
    minimum_index,
    first_element_index,
    number_of_swaps,
) -> list:
    """
    Makes exactly one step in the selection sort.
    So it either finds new minimum or does nothing.

    Either way, it increments the number of comparisons by 1.
    """
    number_of_comparisons += 1

    if data[index] < data[minimum_index]:
        minimum_index = index

    if index == len(data) - 1:
        data[first_element_index], data[minimum_index] = (
            data[minimum_index],
            data[first_element_index],
        )
        number_of_swaps += 1
        minimum_index = first_element_index + 1
    return number_of_comparisons, minimum_index, number_of_swaps


def drawSelection(
    window,
    data: list,
    index,
    number_of_comparisons,
    minimum_index,
    first_element_index,
    number_of_swaps,
) -> None:
    """
    Draw the partially sorted list after one step of the selection sort.
    """
    window.update_idletasks()
    width = window.winfo_width() // 2 - 25
    height = window.winfo_height() // 2 - 25
    canvas_selection = tk.Canvas(window, width=width, height=height)
    canvas_selection.place(x=501, y=26)
    max_data = max(data)
    tk.Label(
        canvas_selection, text=f"Number of comparisons: {number_of_comparisons}"
    ).place(x=0, y=0)
    tk.Label(canvas_selection, text=f"Number of swaps:       {number_of_swaps}").place(
        x=0, y=25
    )
    for i, j in enumerate(data):
        if i == index:
            drawRectangle(canvas_selection, len(data), i, "green", max_data, j)
        elif i == minimum_index:
            drawRectangle(canvas_selection, len(data), i, "red", max_data, j)
        elif i == first_element_index:
            drawRectangle(canvas_selection, len(data), i, "purple", max_data, j)
        else:
            drawRectangle(canvas_selection, len(data), i, "blue", max_data, j)

    window.update()
    return selectionSortStep(
        data,
        index,
        number_of_comparisons,
        minimum_index,
        first_element_index,
        number_of_swaps,
    )


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
