print("Welcome to the rollercoaster ride!")

height = int(input("Enter your height: "))


if height >= 120:
    print("You can ride the rollercoaster:")
    age = int(input("Enter your age: "))
    if age < 12:
        print("Your ticket price is 5$.")
    elif  age <= 18:
        print("Your ticket price is 7$.")
    else:
        print("Your ticket price is 12$.")
else:
    print("You have to grow up to ride the rollercoaster.")
