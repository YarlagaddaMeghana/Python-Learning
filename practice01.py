# Scenario: Supermarket Discount System
# A supermarket gives discounts based on the customer's purchase amount:
# If purchase amount is ₹5000 or more → 20% discount
# If purchase amount is ₹3000 or more → 10% discount
# If purchase amount is ₹1000 or more → 5% discount
# Otherwise → No discount

amount=int(input())
if amount>=5000:
  print(amount-amount*(20/100))
elif 3000<=amount<5000:
  print(amount-amount*(10/100))
elif 1000<=amount<3000:
  print(amount-amount*(5/100))
else:
  print(amount)

# Scenario: An online shopping website calculates delivery charges:
# Order amount ≥ ₹2000 → Free delivery
# Order amount ≥ ₹1000 → ₹50 delivery charge
# Otherwise → ₹100 delivery charge

amount=int(input())
if amount>=2000:
    print(amount)
elif 1000<=amount<2000:
    print(amount+50)
else:
    print(amount+100)

# Real-Time Scenario: Electricity Bill Calculation
# An electricity company calculates the bill based on the number of units consumed:
# Units Consumed Rate per Unit
# 0–100.                     ₹2
# 101–200.                 ₹3
# 201–300                  ₹5
# Above 300.               ₹7
# Write a Python program using if-elif-else to:
# Take the number of units consumed as input.
# Calculate the electricity bill based on the applicable rate.
# Print the total bill amount.

units=int(input())
if 0<=units<=100:
   print(units*2)
elif 101<=units<=200:
   print(units*3)
elif 201<units<=300:
   print(units*5)
else:
   print(units*7)
