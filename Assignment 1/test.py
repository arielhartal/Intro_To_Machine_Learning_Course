import numpy as np

def most_common_element(arr):
    # Flatten the array in case it's multi-dimensional
    arr_flat = arr.flatten()
    
    # Find the unique elements and their counts
    unique_elements, counts = np.unique(arr_flat, return_counts=True)
    
    # Identify the index of the maximum count
    max_index = np.argmax(counts)
    
    # Return the most common element
    return unique_elements[max_index]

# Example usage
array = np.array([1, 2, 2, 3, 3, 3, 4, 4])
most_common = most_common_element(array)
print("Most common element:", most_common)
