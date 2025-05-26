#Task 1: Read a File and Handle Errors
try:
    file = open('sample.txt', 'r')
    print("Reading file content:")
    for line in file:
        print(line.strip())  # Remove trailing newline characters
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

#Task 2: Write and Append Data to a File

initial_input = input("Enter initial content to write to the file: ")

with open('output.txt', 'w') as file:
    file.write(initial_input + '\n')

additional_input = input("Enter additional content to append to the file: ")

with open('output.txt', 'a') as file:
    file.write(additional_input + '\n')

with open('output.txt', 'r') as file:
    content = file.read()
    print("\nFinal content of output.txt:\n")
    print(content)