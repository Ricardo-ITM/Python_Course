# Python comund interest calculator

principle = 0
rate = 0
time = 0

# Enter data and check for invalid inputs
while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest can't be less than or equal to zero")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")
    else:
        break

# Calculate the amount
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")