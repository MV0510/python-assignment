
#Task 1: Create a Dictionary of Student Marks
students_marks = {'Mike':80,'Alice':85,'Nick':90}
students_name = input("Enter the student's name: ")

if students_name in students_marks:
    print(f"{students_name}'s marks: {students_marks[students_name]}")
else:
    print(f"Student '{students_name}' not found in records")

#Task 2: Demonstrate List Slicing

list = list(range(1,11))
list1 = list[:5]
print("Extracted first five elements:" , list1)
list2 = list1
list2.reverse()
print("Reversed Extracted elements: ", list2)