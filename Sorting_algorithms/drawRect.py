from math import floor


def drawRectangle(
    canvas,
    number_of_rects: int,
    position: int,
    color,
    max_data: int,
    min_data: int,
    cur_data: int,
    width: int,
    height: int,
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
    rect_width = width / number_of_rects  # Calculate the width of each rectangle
    if max_data - min_data == 0:
        # This means all elements are the same
        rect_height = height // 2  # Avoid division by zero

    else:
        height_scaling = (height - 20) / (
            max_data - min_data
        )  # Calculate the height scaling factor
        rect_height = height_scaling * (cur_data - min_data)
    canvas.create_rectangle(
        floor((position) * rect_width),  # x-coordinate of the top-left corner
        floor(height - rect_height),  # y-coordinate of the top-left corner
        floor((position + 1) * rect_width),  # x-coordinate of the bottom-right corner
        height,  # y-coordinate of the bottom-right corner
        fill=color,  # fill color of the rectangle
    )
    canvas.create_text(
        floor((position + 0.5) * rect_width),  # x-coordinate of the text
        floor(height - rect_height - 10),  # y-coordinate of the text
        text=str(cur_data),  # text to display
        fill="black",  # color of the text
    )
