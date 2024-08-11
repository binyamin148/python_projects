# Sorting Algorithms Implementation and Performance Comparison

This project implements various sorting algorithms, provides a testing mechanism, and compares their performance.

## Table of Contents
1. [Overview](#overview)
2. [Implemented Algorithms](#implemented-algorithms)
3. [Features](#features)
4. [Requirements](#requirements)
5. [Usage](#usage)
6. [Output](#output)

## Overview

This Python script implements five different sorting algorithms, tests their correctness, and compares their performance across different input sizes. It's designed to help understand the behavior and efficiency of various sorting techniques.

## Implemented Algorithms

1. Bubble Sort
2. Quick Sort
3. Merge Sort
4. Counting Sort
5. Radix Sort

## Features

- Implementation of five sorting algorithms
- Automated testing of each algorithm's correctness
- Performance comparison across different input sizes
- Visualization of performance results

## Requirements

To run this script, you need:

- Python 3.x
- matplotlib library

You can install matplotlib using pip:

```
pip install matplotlib
```

## Usage

1. Ensure you have Python and matplotlib installed.
2. Save the script as `sorting_algorithms.py`.
3. Run the script:

```
python sorting_algorithms.py
```

## Output

The script will produce two types of output:

1. Console output: Shows the results of correctness tests for each algorithm.

Example:
```
Testing the correctness of algorithms:
Bubble Sort: True
Quick Sort: True
Merge Sort: True
Counting Sort: True
Radix Sort: True
```

2. Graph: A PNG file named `sorting_performance_comparison.png` will be saved in the same directory. This graph shows the execution time of each algorithm for different input sizes.

The graph provides a visual representation of how each algorithm's performance scales with increasing input size, allowing for easy comparison of their efficiency.

---

Feel free to modify the code or extend the project to include additional sorting algorithms or performance metrics!