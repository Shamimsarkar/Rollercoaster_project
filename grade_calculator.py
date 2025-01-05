print("Welcome to grade calculator project!")

number = int(input("Enter your number : "))

if number >= 80:
    print("A+")
elif 70 <= number < 80:
    print("A")
elif 60 <= number < 70:
    print("B")
elif 50 <= number < 60:
    print("C")
elif 40 <= number < 50:
    print("D")
else:
    print("Fail")
