
N = int(input("Enter the value of N: "))


with open("fizzbuzz_output.txt", "w") as file:
    for i in range(1, N + 1):
        if i % 3 == 0 and i % 5 == 0:
            output = "FizzBuzz"
        elif i % 3 == 0:
            output = "Fizz"
        elif i % 5 == 0:
            output = "Buzz"
        else:
            output = str(i)

        print(output)          # Print to console
        file.write(output + "\n")  # Save to file

print("Output has been saved to 'fizzbuzz_output.txt'")