
print("Fathima ST12345 fathima@example.com")
print("Fathima\tST12345\tfathima@example.com")
num1 = 14
num2 = 7
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")

for i in range(1, 6):
    print(i)
print("\"SDK\" stands for \"Software Development Kit\", whereas \"IDE\" stands for \"Integrated Development Environment\".")

print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")  # ASCII code for '5'
print("\x65") # Hexadecimal code for 'e'
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

num = 23
textnum = "57"
decimal = 98.3

# Print types
print(type(num), type(textnum), type(decimal))

# Convert and sum
total = num + int(textnum) + decimal
print(f"Sum: {total}")
print(f"Data type of sum: {type(total)}")
days_in_year = 365
minutes_in_hour = 60
hours_in_day = 24

total_minutes = days_in_year * hours_in_day * minutes_in_hour
print(f"The total number of minutes in a year is: {total_minutes}")

name = input("Please enter your name: ")
print(f"Hi {name}, welcome to Python programming :)")

pounds = float(input("Please enter amount in pounds: "))
conversion_rate = 1.35  # Example rate, adjust as needed
dollars = pounds * conversion_rate
print(f"£{pounds} are ${dollars:.2f}")





