# Kadane's Algorithm
# Find the maximum sum of a contiguous subarray

def max_subarray(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        # Decide whether to start a new subarray
        # or continue the existing one
        current_sum = max(arr[i], current_sum + arr[i])

        # Update maximum sum found so far
        max_sum = max(max_sum, current_sum)

    return max_sum


# Input array
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

result = max_subarray(arr)

print("Array:", arr)
print("Maximum Subarray Sum:", result)