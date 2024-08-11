import random
import time
import matplotlib.pyplot as plt

# Sorting Algorithms

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def counting_sort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    output = [0] * len(arr)
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1
    
    return output

def radix_sort(arr):
    if not arr:
        return arr

    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    
    return arr

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

# Testing function

def test_sorting_algorithm(sort_func):
    # Test case 1: Random list
    test_case1 = random.sample(range(1000), 100)
    sorted_case1 = sort_func(test_case1.copy())
    if sorted_case1 != sorted(test_case1):
        return False

    # Test case 2: Already sorted list
    test_case2 = list(range(100))
    sorted_case2 = sort_func(test_case2.copy())
    if sorted_case2 != test_case2:
        return False

    # Test case 3: Reverse sorted list
    test_case3 = list(range(100, 0, -1))
    sorted_case3 = sort_func(test_case3.copy())
    if sorted_case3 != sorted(test_case3):
        return False

    # Test case 4: List with duplicate values
    test_case4 = [1, 5, 2, 8, 2, 1, 5, 9, 8, 2]
    sorted_case4 = sort_func(test_case4.copy())
    if sorted_case4 != sorted(test_case4):
        return False

    # Test case 5: Empty list
    test_case5 = []
    sorted_case5 = sort_func(test_case5.copy())
    if sorted_case5 != []:
        return False

    # If all test cases passed, return True
    return True

# Performance comparison function

def plot_sorting_performance(algorithms):
    input_sizes = [100, 500, 1000, 2000, 3000, 4000, 5000]
    times = {name: [] for name in algorithms.keys()}
    
    for size in input_sizes:
        arr = [random.randint(1, 1000) for _ in range(size)]
        
        for name, func in algorithms.items():
            start_time = time.time()
            func(arr.copy())
            end_time = time.time()
            
            times[name].append(end_time - start_time)
    
    plt.figure(figsize=(12, 8))
    for name, execution_times in times.items():
        plt.plot(input_sizes, execution_times, label=name, marker='o')
    
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Sorting Algorithms Performance Comparison')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('sorting_performance_comparison.png')
    plt.close()

    print("The graph has been saved as 'sorting_performance_comparison.png'")

# Main execution

if __name__ == "__main__":
    print("Testing the correctness of algorithms:")
    print("Bubble Sort:", test_sorting_algorithm(bubble_sort))
    print("Quick Sort:", test_sorting_algorithm(quick_sort))
    print("Merge Sort:", test_sorting_algorithm(merge_sort))
    print("Counting Sort:", test_sorting_algorithm(counting_sort))
    print("Radix Sort:", test_sorting_algorithm(radix_sort))

    algorithms = {
        "Bubble Sort": bubble_sort,
        "Quick Sort": quick_sort,
        "Merge Sort": merge_sort,
        "Counting Sort": counting_sort,
        "Radix Sort": radix_sort
    }

    plot_sorting_performance(algorithms)