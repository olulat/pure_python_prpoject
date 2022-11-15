principle = 0
rate = 0
time = 0
monthly_interest = 0
number_of_payment = 0
month_in_year = 12
percent = 100


while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than pr equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the rate amount: "))
    if rate < 0:
        print("Rate can't be less than pr equal to zero")
    else:
        monthly_interest = (rate / percent) / month_in_year
        break

while True:
    time = int(input("Enter the the time in year: "))
    if time < 0:
        print("Time can't be less than pr equal to zero")
    else:
        number_of_payment = time * month_in_year
        break

equation_1 = monthly_interest * pow(1+monthly_interest, number_of_payment)
equation_2 = pow(1+monthly_interest, number_of_payment) - 1

monthly_payment = round(principle * (equation_1 / equation_2))

print(monthly_payment)
