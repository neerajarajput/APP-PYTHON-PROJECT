import matplotlib.pyplot as plt
import numpy as np
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr  # Yield the current state of the array for visualization

def visualize_bubble_sort(arr):
    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort Visualization")
    
    # Create a bar container with consistent x range for bars
    bars = ax.bar(range(len(arr)), arr, color='b', alpha=0.6)
    
    generator = bubble_sort(arr.copy())  # Create a generator for the algorithm

    num_bars = len(arr)
    if num_bars <= 20:
        speed_factor = 0.1
    elif num_bars <= 30:
        speed_factor = 0.05
    else:
        speed_factor = 0.01  # Adjust speed based on the number of bars

    for i, sorted_arr in enumerate(generator):
        for bar, val in zip(bars, sorted_arr):
            bar.set_height(val)  # Update bar heights
            if i < len(sorted_arr) and val == sorted_arr[len(sorted_arr) - i - 1]:
                bar.set_color('r')  # Highlight the current element being considered
            else:
                bar.set_color('b')
        
        plt.pause(speed_factor)

    plt.show()

if __name__ == "__main__":
    np.random.seed(42)
    num_bars = int(input("Enter the number of bars: "))
    array_to_sort = list(np.random.randint(1, 100, size=num_bars))  # Create a random array
    visualize_bubble_sort(array_to_sort)
