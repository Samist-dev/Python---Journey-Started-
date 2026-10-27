import math
name = input("Enter your full name: ").strip().title()

first, second, third= name.split(" ")

birth_year = input("Enter your birth year: ")
Current_year = input("Enter the current year: ")
age = int(Current_year) - int(birth_year)




print("Your first name is ",first)
print("Your second name is ",second)
print("Your third name is ",third)
print("You are ",age," years old.")

print("The value of pi is approximately ",round(math.pi,7))
print("The value of pi in mythology is approximately ",round(22/7,5))