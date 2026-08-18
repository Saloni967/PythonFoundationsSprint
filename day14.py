students = [
    {"name": "Aisha", "marks": 85},
    {"name": "Rahul", "marks": 72},
    {"name": "Sneha", "marks": 91},
    {"name": "Arjun", "marks": 64},
    {"name": "Priya", "marks": 48}
]

# Hashmap to store grade counts
grade_count = {}

total_marks = 0
highest_marks = -1
top_student = ""

# Process the dataset
for student in students:
    name = student["name"]
    marks = student["marks"]

    total_marks += marks

    # Find highest scorer
    if marks > highest_marks:
        highest_marks = marks
        top_student = name

    # Assign grade
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    # Update hashmap
    grade_count[grade] = grade_count.get(grade, 0) + 1


# Calculate average
average = total_marks / len(students)

# Generate insights
print("----- DATA ANALYSIS -----")

print("Total students:", len(students))
print("Average marks:", round(average, 2))
print("Top student:", top_student)
print("Highest marks:", highest_marks)

print("\nGrade Distribution:")

for grade, count in grade_count.items():
    print(grade, ":", count)