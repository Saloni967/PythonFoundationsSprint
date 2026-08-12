# Prefix Sum Optimization

def build_prefix_sum(arr):
    prefix = [0] * len(arr)

    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix


def range_sum_brute_force(arr, left, right):
    total = 0

    for i in range(left, right + 1):
        total += arr[i]

    return total


def range_sum_prefix(prefix, left, right):
    if left == 0:
        return prefix[right]

    return prefix[right] - prefix[left - 1]


# Input array
arr = [2, 4, 1, 5, 3, 7, 6]

# Build prefix sum array
prefix = build_prefix_sum(arr)

print("Original Array:", arr)
print("Prefix Sum Array:", prefix)

# Multiple queries
queries = [(1, 3), (2, 5), (0, 4), (3, 6)]

print("\nQuery Results:")

for left, right in queries:
    brute = range_sum_brute_force(arr, left, right)
    optimized = range_sum_prefix(prefix, left, right)

    print(f"Range [{left}, {right}]")
    print("Brute Force:", brute)
    print("Prefix Sum :", optimized)
    print()