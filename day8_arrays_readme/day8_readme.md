# Day 8 – Understanding Arrays Through Real Data

## 📌 Project Overview

This mini project demonstrates how arrays (Python lists) can be used to store and process real-world data.

For this project, a list of simulated user activity IDs is created. The program checks each number and counts how many numbers contain an even number of digits.

## 🎯 Objective

* Create an array/list containing numbers.
* Check the number of digits in each value.
* Identify numbers with an even number of digits.
* Display the results clearly.
* Understand how arrays are used in real-world software systems.

## 💻 Example Data

```python
user_data = [
    1024, 567, 8901, 45, 12345,
    678, 2345, 89, 7654, 321
]
```

## ⚙️ How It Works

The program goes through each number in the list.

For every number:

1. It converts the number into a string.
2. It counts the number of digits.
3. It checks whether the digit count is even.
4. If it is even, the number is added to a separate list.
5. Finally, the program displays the original data, filtered results, and total count.

## 📊 Sample Output

```text
User Activity Data:
[1024, 567, 8901, 45, 12345, 678, 2345, 89, 7654, 321]

Numbers with even number of digits:
[1024, 8901, 45, 2345, 89, 7654]

Total numbers: 10
Numbers with even digits: 6
```

## 🧠 What I Learned

Through this project, I learned:

* How to create and use lists in Python.
* How to iterate through an array using a `for` loop.
* How to count digits using string conversion.
* How to use conditions to filter data.
* How arrays are used as the foundation for processing real-world data.

