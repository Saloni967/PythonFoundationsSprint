# Day 8 - Understanding Arrays Through Real Data

# Simulated user activity IDs
user_data = [
    1024, 567, 8901, 45, 12345,
    678, 2345, 89, 7654, 321
]

even_digit_numbers = []

for number in user_data:
    # Count the number of digits
    digit_count = len(str(number))

    # Check if the number has even digits
    if digit_count % 2 == 0:
        even_digit_numbers.append(number)

print("User Activity Data:")
print(user_data)

print("\nNumbers with even number of digits:")
print(even_digit_numbers)

print("\nTotal numbers:", len(user_data))
print("Numbers with even digits:", len(even_digit_numbers))