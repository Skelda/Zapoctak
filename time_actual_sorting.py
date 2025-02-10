from copy import deepcopy
import random
import time
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


def bubbleSort(data):
    """
    Sort the data using the bubble sort algorithm.
    """
    for i in range(len(data) - 1):
        for j in range(0, len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return


def selectionSort(data):
    """
    Sort the data using the selection sort algorithm.
    """
    for i in range(len(data)):
        minimum_index = i
        for j in range(i, len(data)):
            if data[j] < data[minimum_index]:
                minimum_index = j
        data[i], data[minimum_index] = data[minimum_index], data[i]
    return


def insertionSort(data):
    """
    Sort the data using the insertion sort algorithm.
    """
    for i in range(0, len(data) - 1):
        for j in range(i, -1, -1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            else:
                break
    return


def sorting_times():
    elements = []
    bubble_sort_times = []
    selection_sort_times = []
    insertion_sort_times = []
    for i in range(100, 1001, 25):
        # Generate random data
        data = [random.randint(0, 1000) for _ in range(i)]

        # Deepcopy data for each sort to ensure they all sort the same data
        data_bubble = deepcopy(data)
        data_selection = deepcopy(data)
        data_insertion = deepcopy(data)

        # Measure time for bubble sort
        start_time = time.time()
        bubbleSort(data_bubble)
        bubble_sort_time = time.time() - start_time

        # Measure time for selection sort
        start_time = time.time()
        selectionSort(data_selection)
        selection_sort_time = time.time() - start_time

        # Measure time for insertion sort
        start_time = time.time()
        insertionSort(data_insertion)
        insertion_sort_time = time.time() - start_time

        # Store the results
        elements.append(i)
        bubble_sort_times.append(bubble_sort_time)
        selection_sort_times.append(selection_sort_time)
        insertion_sort_times.append(insertion_sort_time)

    # Plotting the results
    plt.plot(elements, bubble_sort_times, "bo-", label="Bubble Sort")
    plt.plot(elements, selection_sort_times, "go-", label="Selection Sort")
    plt.plot(elements, insertion_sort_times, "ro-", label="Insertion Sort")

    plt.xlabel("Number of elements")
    plt.ylabel("Time (seconds)")
    plt.title("Sorting Algorithm Performance")
    plt.legend()


def plot_sorting_times(window):
    sorting_times()
    fig = plt.gcf()
    window.update_idletasks()
    width = window.winfo_width() // 2 - 25
    height = window.winfo_height() // 2 - 25
    canvas_plot = FigureCanvasTkAgg(fig, window)
    canvas_plot.draw()
    canvas_plot.get_tk_widget().place(
        x=width + 26, y=height + 26, width=width, height=height
    )
    window.update()
    plt.clf()
