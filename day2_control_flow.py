try:
    
    marks = float(input("Enter student's marks: "))


    if marks < 0 or marks > 100:
        print("Invalid input! Marks must be between 0 and 100.")

    else:
        
        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        else:
            grade = "Fail"

        
        if marks >= 50:
            result = "Passed"
        else:
            result = "Failed"

        
        print("Grade:", grade)
        print("Result:", result)

except ValueError:
    print("Invalid input! Please enter a valid number.")