# Sorting Algorithms Visualization

This project visualizes various sorting algorithms using Tkinter in Python. The visualizations include Bubble Sort, Selection Sort, and Insertion Sort.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [License](#license)

## Introduction

This project provides a visual representation of different sorting algorithms. It helps in understanding how these algorithms work by showing the step-by-step process of sorting a list of elements.

## Features

- Visualize Bubble Sort, Selection Sort, and Insertion Sort.
- Compare the performance of different sorting algorithms.
- Option to run the visualizations asynchronously.
- Ability to use randomized data or import data from a file.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Skelda/Zapoctak
    ```
2. Navigate to the project directory:
    ```sh
    cd sorting-visualization
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script to start the application:
    ```sh
    python main.py
    ```
2. Select whether or not the sorting algorithms should be run at the same time (check the box "Run async") or one at a time.
3. Select whether you want to import data from your computer (check the box "Data from file") or not, in which case the data will be randomized.
4. Start the sorting by clicking the button "Start sorting".
5. The "Show Sorting Times" button will display a plot comparing the performance of all three sorting algorithms. The algorithms will sort arrays of random data ranging in size from 100 to 1000. Note: This data is not related to the data used by the visualizer and will always be randomly generated.

## Code Structure

- [main.py](https://github.com/Skelda/Zapoctak/blob/main/main.py): The main script to run the application.
    - **Functions**:
        - `initializeScreen()`: Initializes the Tkinter window and starts the main function.
        - `main()`: Main function to run the sorting visualizations.
        - `start_sorting()`: Starts the sorting process based on user selection.
        - `show_sorting_times()`: Displays the sorting times plot.

- [Sorting_algorithms](https://github.com/Skelda/Zapoctak/tree/main/Sorting_algorithms): Directory containing the sorting algorithm implementations and visualization functions.
    - [bubble.py](https://github.com/Skelda/Zapoctak/blob/main/Sorting_algorithms/bubble.py): Contains the Bubble Sort implementation and visualization.
        - **Functions**:
            - `bubbleSortStep()`: Performs one step of the Bubble Sort algorithm.
            - `drawBubble()`: Draws the Bubble Sort visualization.
            - `drawRectangle()`: Draws a rectangle representing an element in the list.
    - [selection.py](https://github.com/Skelda/Zapoctak/blob/main/Sorting_algorithms/selection.py): Contains the Selection Sort implementation and visualization.
        - **Functions**:
            - `selectionSortStep()`: Performs one step of the Selection Sort algorithm.
            - `drawSelection()`: Draws the Selection Sort visualization.
            - `drawRectangle()`: Draws a rectangle representing an element in the list.
    - [insertion.py](https://github.com/Skelda/Zapoctak/blob/main/Sorting_algorithms/insertion.py): Contains the Insertion Sort implementation and visualization.
        - **Functions**:
            - `insertionSortStep()`: Performs one step of the Insertion Sort algorithm.
            - `drawInsertion()`: Draws the Insertion Sort visualization.
            - `drawRectangle()`: Draws a rectangle representing an element in the list.
    - [__init__.py](https://github.com/Skelda/Zapoctak/blob/main/Sorting_algorithms/__init__.py): Initializes the Sorting_algorithms module.

- [run_normal.py](https://github.com/Skelda/Zapoctak/blob/main/run_normal.py): Script to run the sorting visualizations synchronously.
    - **Functions**:
        - `main()`: Main function to run the sorting visualizations synchronously.
        - `bubble_loop()`: Visualizes the Bubble Sort algorithm.
        - `selection_loop()`: Visualizes the Selection Sort algorithm.
        - `insertion_loop()`: Visualizes the Insertion Sort algorithm.

- [run_async.py](https://github.com/Skelda/Zapoctak/blob/main/run_async.py): Script to run the sorting visualizations asynchronously.
    - **Functions**:
        - `startAsyncMain()`: Starts the main function using asyncio.
        - `main()`: Main function to run the sorting visualizations asynchronously.
        - `bubble_loop()`: Visualizes the Bubble Sort algorithm asynchronously.
        - `selection_loop()`: Visualizes the Selection Sort algorithm asynchronously.
        - `insertion_loop()`: Visualizes the Insertion Sort algorithm asynchronously.

- [time_actual_sorting.py](https://github.com/Skelda/Zapoctak/blob/main/time_actual_sorting.py): Script to measure and plot the performance of the sorting algorithms.
    - **Functions**:
        - `bubbleSort()`: Sorts the data using the Bubble Sort algorithm.
        - `selectionSort()`: Sorts the data using the Selection Sort algorithm.
        - `insertionSort()`: Sorts the data using the Insertion Sort algorithm.
        - `sorting_times()`: Measures the sorting times for different algorithms.
        - `plot_sorting_times()`: Plots the sorting times for different algorithms.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
