import random
import time
import matplotlib.pyplot as plt
from heap_sort import heap_sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def measure_sort_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())  
    end_time = time.time()
    return end_time - start_time

def compare_sorting_algorithms(algorithms, sizes):
    results = {name: [] for name in algorithms.keys()}
    
    for size in sizes:
        arr = generate_random_array(size)
        for name, func in algorithms.items():
            time_taken = measure_sort_time(func, arr)
            results[name].append(time_taken)
    
    return results

def plot_results(results, sizes):
    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        plt.plot(sizes, times, marker='o', label=name)
    
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm Performance Comparison')
    plt.legend()
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()

algorithms = {
    'HeapSort': heap_sort,
    'BubbleSort': bubble_sort,
    'SelectionSort': selection_sort,
    'InsertionSort': insertion_sort,
}

sizes = [100, 500, 1000, 5000, 10000]

results = compare_sorting_algorithms(algorithms, sizes)

plot_results(results, sizes)