# The month and year determine how many days the program responds with. 
month = input("Enter a month (1-12): ")
year = input("Enter a year (>1000): ")

# We must convert the "month" and "year" inputs from strings to integers in order to analyze them numerically.
if int(month) == 4 or 6 or 9 or 11:
    print("There are 30 days in", month + "/" + year + ".")
elif int(month) == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    print("There are 31 days in", month + "/" + year + ".")
elif int(month) == 2 and int(year) % 4 == 0:
    print("There are 29 days in", month + "/" + year + ". Happy Leap Year!")
elif int(month) == 2:
    print("There are 28 days in", month + "/" + year + ".")
else:
    print("INVALID DATE")

''' The modulus operator on line 10 helps us determine if the given year is a leap year.
Leap years must have a remainder of 0 in order to be divisible by 4! '''