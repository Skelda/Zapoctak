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

- [main.py](http://_vscodecontentref_/0): The main script to run the application.
- [Sorting_algorithms](http://_vscodecontentref_/1): Directory containing the sorting algorithm implementations and visualization functions.
  - [bubble.py](http://_vscodecontentref_/2): Contains the Bubble Sort implementation and visualization.
  - [selection.py](http://_vscodecontentref_/3): Contains the Selection Sort implementation and visualization.
  - [insertion.py](http://_vscodecontentref_/4): Contains the Insertion Sort implementation and visualization.
- [run_normal.py](http://_vscodecontentref_/5): Script to run the sorting visualizations synchronously.
- [run_async.py](http://_vscodecontentref_/6): Script to run the sorting visualizations asynchronously.
- [time_actual_sorting.py](http://_vscodecontentref_/7): Script to measure and plot the performance of the sorting algorithms.
