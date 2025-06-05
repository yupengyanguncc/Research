import time
import random
import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def improved_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

def simple_exchange_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def measure_sort_time(sort_func, arr, num_runs=100):
    times = []
    for _ in range(num_runs):
        arr_copy = arr.copy()
        start_time = time.time()
        sort_func(arr_copy)
        end_time = time.time()
        times.append(end_time - start_time)
    return np.mean(times)

def main():
    array_size = 1000    
    test_cases = {
        'Random Array': [random.randint(1, 1000000) for _ in range(array_size)],
        'Nearly Sorted': sorted([random.randint(1, 1000000) for _ in range(array_size)])[:array_size-100] + [random.randint(1, 1000000) for _ in range(100)],
        'Reversed Array': sorted([random.randint(1, 1000000) for _ in range(array_size)], reverse=True)
    }
    
    sorting_algorithms = {
        'Bubble Sort': bubble_sort,
        'Improved Bubble Sort': improved_bubble_sort,
        'Simple Exchange Sort': simple_exchange_sort,
        'Insertion Sort': insertion_sort,
        'Selection Sort': selection_sort,
        'Quick Sort': quick_sort
    }
    
    for test_name, test_array in test_cases.items():
        print(f"\nTesting with {test_name}:")
        avg_times = {}
        for name, algorithm in sorting_algorithms.items():
            print(f"Measuring {name}...")
            avg_time = measure_sort_time(algorithm, test_array)
            avg_times[name] = avg_time
            print(f"{name}: {avg_time:.4f} seconds")
        
        plt.figure(figsize=(12, 6))
        algorithms = list(avg_times.keys())
        times = list(avg_times.values())
        
        bars = plt.bar(algorithms, times)
        
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.4f}s',
                    ha='center', va='bottom')
        
        plt.title(f'Average Runtime of Sorting Algorithms (100 runs) - {test_name}')
        plt.xlabel('Sorting Algorithm')
        plt.ylabel('Average Time (seconds)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        plt.savefig(f'sorting_algorithms_comparison_{test_name.lower().replace(" ", "_")}.png')
        plt.close()

if __name__ == "__main__":
    main()