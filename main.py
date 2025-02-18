import tkinter as tk
from Sorting_algorithms import *
import random
from copy import deepcopy
from run_normal import main as run_normal
from run_async import startAsyncMain as run_async
from time_actual_sorting import plot_sorting_times

# Constants for window dimensions
WIDTH = 1000
HEIGHT = 800


def initializeScreen():
    """
    Function that is called exactly once at the start of the program to ensure everything is set up correctly.
    """
    global master
    master = tk.Tk()  # Create the main window
    master.geometry(f"{WIDTH}x{HEIGHT}")  # Set window size
    master.title("Sorting Algorithms")  # Set window title

    main()  # Call the main function


def main():
    """
    Main function used to run all the functionality of the code.
    """
    data = list(
        random.randint(1, 100) for i in range(25)
    )  # Generate random data for sorting
    # data = list(i for i in range(25))  # Uncomment to use sequential data

    # Draw initial sorting visualizations
    drawBubble(master, deepcopy(data), 0, 0, 0)
    drawSelection(master, deepcopy(data), 0, 0, 0, 0, 0)
    drawInsertion(master, deepcopy(data), 0, 0, 0)

    def start_sorting():
        """
        Function to start the sorting process based on the selected mode (normal or async).
        """
        if data_file_var.get():
            file_path = tk.filedialog.askopenfilename(
                title="Select Data File",
                filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")),
            )
            if file_path:
                with open(file_path, "r") as file:
                    data = []
                    for line in file.readlines():
                        data.extend([int(num) for num in line.strip().split()])
        else:
            data = list(
                random.randint(1, 100) for i in range(25)
            )  # Generate random data for sorting
        if async_var.get():
            run_async(master, deepcopy(data))  # Run async sorting
        else:
            run_normal(master, deepcopy(data))  # Run normal sorting

    async_var = tk.BooleanVar()  # Variable to store the state of the async checkbox
    async_var.set(False)  # Default to normal sorting
    data_file_var = (
        tk.BooleanVar()
    )  # Variable to store the state of the data file checkbox
    data_file_var.set(False)

    switch_frame = tk.Frame(master)  # Frame to hold the control buttons
    switch_frame.pack()

    async_button = tk.Checkbutton(
        switch_frame, text="Run Async", variable=async_var
    )  # Checkbox to toggle async mode
    async_button.pack(side=tk.LEFT)

    data_file_checkbox = tk.Checkbutton(
        switch_frame, text="Data from file", variable=data_file_var
    )  # Checkbox to toggle async mode
    data_file_checkbox.pack(side=tk.LEFT)

    start_button = tk.Button(
        switch_frame, text="Start Sorting", command=start_sorting
    )  # Button to start sorting
    start_button.pack(side=tk.LEFT)

    def show_sorting_times():
        """
        Function to display the sorting times.
        """
        plot_sorting_times(master)  # Plot sorting times

    times_button = tk.Button(
        switch_frame, text="Show Sorting Times", command=show_sorting_times
    )  # Button to show sorting times
    times_button.pack(side=tk.LEFT)

    master.mainloop()  # Start the Tkinter event loop


if __name__ == "__main__":
    initializeScreen()  # Initialize and start the program
