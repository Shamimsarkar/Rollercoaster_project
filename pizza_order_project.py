# Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.

# Small pizza (S): $15

# Medium pizza (M): $20

# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2

# Add pepperoni for medium or large pizza (Y or N): +$3

# Add extra cheese for any size pizza (Y or N): +$1


print("Welcome to pizza shop!")

pizza_size = input("Which type of pizza you want? Select s for small m for medium and l for large :")
pepperoni = input("Do you want to add pepperoni? Select y for yes and n for no")
cheese = input("Do you want to add cheese? Select y for yes and n for no")
bill = 0

if pizza_size == "s":
    bill = 15
elif pizza_size == "m":
    bill = 20
elif pizza_size == "l":
    bill = 25
else:
    print("You entered wrong value!")


if pepperoni == "y":
    if pizza_size == "s":
        bill +=2
    else:
        bill +=3

if cheese == "y":
    bill +=1

print(f"You have to pay total bill is :{bill}")