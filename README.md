# Sorting Algorithms Visualization

This project visualizes various sorting algorithms using Tkinter in Python. The visualizations include Bubble Sort, Selection Sort, and Insertion Sort.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)

## Introduction

This project provides a visual representation of different sorting algorithms. It helps in understanding how these algorithms work by showing the step-by-step process of sorting a list of elements.

## Features

- Visualize Bubble Sort, Selection Sort, and Insertion Sort.
- Compare the performance of different sorting algorithms.
- Option to run the visualizations asynchronously.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Skelda/sorting-visualization.git
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
2. Use the GUI to visualize the sorting algorithms.

## Code Structure

- [main.py](https://github.com/Skelda/Zapoctak/blob/main/main.py): The main script to run the application.
- [Sorting_algorithms](https://github.com/Skelda/Zapoctak/tree/main/Sorting_algorithms): Directory containing the sorting algorithm implementations and visualization functions.
  - [bubble.py](https://github.com/Skelda/Zapoctak/tree/main/Sorting_algorithms/buble.py): Contains the Bubble Sort implementation and visualization.
  - [selection.py](https://github.com/Skelda/Zapoctak/tree/main/Sorting_algorithms/selection.py): Contains the Selection Sort implementation and visualization.
  - [insertion.py](https://github.com/Skelda/Zapoctak/tree/main/Sorting_algorithms/insertion.py): Contains the Insertion Sort implementation and visualization.
- [run_normal.py](https://github.com/Skelda/Zapoctak/blob/main/run_normal.py): Script to run the sorting visualizations synchronously.
- [run_async.py](https://github.com/Skelda/Zapoctak/blob/main/run_async.py): Script to run the sorting visualizations asynchronously.
- [time_actual_sorting.py](https://github.com/Skelda/Zapoctak/blob/main/time_actual_sorting.py): Script to measure and plot the performance of the sorting algorithms.
