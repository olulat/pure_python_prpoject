sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1
card_number = input("Enter a credit card #: ")

# Removing any space and dashes from user input
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")

# Change the direction of card number
card_number = card_number[::-1]

# Step 2
# Add all digits in the odd places from right to left.
for x in card_number[::2]:
    sum_odd_digits += int(x)

# Step 3
# Double every second digit from right to left.
for x in card_number[1::2]:
    # Note if result is a two-digit number, add the two-digit number together to get a single digit
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += 1 + (x % 10)
    else:
        sum_even_digits += x

# Step 3
# Sum the totals of steps 2 & 3
total = sum_odd_digits + sum_even_digits

# Step 5
# If sum is divisible by 10, the credit card # is valid
if total % 10 == 0:
    print("CARD IS VALID")
else:
    print("INVALID CARD")



