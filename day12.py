def reverse_string(text):
    return text[::-1]


text = input("Enter a string: ")

reversed_text = reverse_string(text)

print("Reversed string:", reversed_text)