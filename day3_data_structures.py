
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))


print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))


frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("\nFrequency of each number:")
for key, value in frequency.items():
    print(f"{key}: {value}")


reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("\nReversed List:", reversed_list)