import tkinter as tk
from Sorting_algorithms import *
import random
from copy import deepcopy
from run_normal import main as run_normal
from run_async import startAsyncMain as run_async
from time_actual_sorting import plot_sorting_times
import unittest

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
    master.title("AlgoVis")  # Set window title

    main()  # Call the main function


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
            random.randint(-100, 100) for i in range(25)
        )  # Generate random data for sorting
    if async_var.get():
        run_async(master, deepcopy(data))  # Run async sorting
    else:
        run_normal(master, deepcopy(data))  # Run normal sorting


def drawButtons():
    """
    Function to draw the control buttons on the screen.
    """
    global async_var, data_file_var  # Declare the variables as global to access them in another function
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

    test_button = tk.Button(
        switch_frame, text="Run Tests", command=run_tests
    )  # Button to run unittests
    test_button.pack(side=tk.LEFT)


def main():
    """
    Main function used to run all the functionality of the code.
    """
    data = list(
        random.randint(-100, 100) for i in range(25)
    )  # Generate random data for sorting

    # Draw initial sorting visualizations
    drawBubble(master, deepcopy(data), 0, 0, 0)
    drawSelection(master, deepcopy(data), 0, 0, 0, 0, 0)
    drawInsertion(master, deepcopy(data), 0, 0, 0)

    drawButtons()  # Draw the control buttons

    master.mainloop()  # Start the Tkinter event loop


class TestSortingAlgorithms(unittest.TestCase):
    def test_bubble_sort_with_data(self):
        from run_normal import bubble_loop

        data = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        bubble_loop(data, master)
        self.assertEqual(data, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_bubble_sort_without_data(self):
        from run_normal import bubble_loop

        data = []
        bubble_loop(data, master)
        self.assertEqual(data, [])

    def test_bubble_sort_single_element(self):
        from run_normal import bubble_loop

        data = [1]
        bubble_loop(data, master)
        self.assertEqual(data, [1])

    def test_bubble_sort_duplicate_elements(self):
        from run_normal import bubble_loop

        data = [5] * 10
        bubble_loop(data, master)
        self.assertEqual(data, [5] * 10)

    def test_bubble_sort_with_negative_numbers(self):
        from run_normal import bubble_loop

        data = [9, -8, 7, -6, 5, -4, 3, -2, 1]
        bubble_loop(data, master)
        self.assertEqual(data, [-8, -6, -4, -2, 1, 3, 5, 7, 9])

    def test_selection_sort_with_data(self):
        from run_normal import selection_loop

        data = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        selection_loop(data, master)
        self.assertEqual(data, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_selection_sort_without_data(self):
        from run_normal import selection_loop

        data = []
        selection_loop(data, master)
        self.assertEqual(data, [])

    def test_selection_sort_single_element(self):
        from run_normal import selection_loop

        data = [1]
        selection_loop(data, master)
        self.assertEqual(data, [1])

    def test_selection_sort_duplicate_elements(self):
        from run_normal import selection_loop

        data = [5] * 10
        selection_loop(data, master)
        self.assertEqual(data, [5] * 10)

    def test_selection_sort_with_negative_numbers(self):
        from run_normal import selection_loop

        data = [9, -8, 7, -6, 5, -4, 3, -2, 1]
        selection_loop(data, master)
        self.assertEqual(data, [-8, -6, -4, -2, 1, 3, 5, 7, 9])

    def test_insertion_sort_with_data(self):
        from run_normal import insertion_loop

        data = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        insertion_loop(data, master)
        self.assertEqual(data, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_insertion_sort_without_data(self):
        from run_normal import insertion_loop

        data = []
        insertion_loop(data, master)
        self.assertEqual(data, [])

    def test_insertion_sort_single_element(self):
        from run_normal import insertion_loop

        data = [1]
        insertion_loop(data, master)
        self.assertEqual(data, [1])

    def test_insertion_sort_duplicate_elements(self):
        from run_normal import insertion_loop

        data = [5] * 10
        insertion_loop(data, master)
        self.assertEqual(data, [5] * 10)

    def test_insertion_sort_with_negative_numbers(self):
        from run_normal import insertion_loop

        data = [9, -8, 7, -6, 5, -4, 3, -2, 1]
        insertion_loop(data, master)
        self.assertEqual(data, [-8, -6, -4, -2, 1, 3, 5, 7, 9])


def run_tests():  # Run the unittests
    result = unittest.TextTestRunner().run(
        unittest.TestLoader().loadTestsFromTestCase(TestSortingAlgorithms)
    )
    if result.wasSuccessful():
        tk.messagebox.showinfo(
            "Test Results", f"All tests passed!\n\nRan {result.testsRun} tests."
        )

    else:
        error_message = "Tests failed:\n\n"
        for failed_test, traceback in result.failures:
            error_message += f"FAIL: {failed_test.id()}\n\n"
            error_message += f"{traceback.split('AssertionError: ')[-1].strip()}\n\n"
        tk.messagebox.showerror("Test Results", error_message)


if __name__ == "__main__":
    initializeScreen()  # Initialize and start the program
