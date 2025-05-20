# task1 - Check if a Number is Even or Odd

num = int(input("Enter the number: "))

if num%2==0: #checks the remainder after dividing the number with 2
    print(num, 'is an even number')
else:
    print(num, 'is an odd number')

# task2 - Sum of Integers from 1 to 50 Using a Loop

total_sum = 0
for number in range(1,51):
    total_sum += number #increases the sum in each iteration for the range mentioned
    print(number)
print("The sum of numbers from 1 to 50 is:", total_sum)