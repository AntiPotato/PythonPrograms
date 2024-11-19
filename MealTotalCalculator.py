import math
import sys

# Take prince input from customer.
charge_for_food = float(input("Enter the charge for the food.\n"))
if(charge_for_food <= 0):
    print("Please enter a valid charge.")
    sys.exit()

sales_tax_percentage = 7
tip_percentage = 18

# Calculate the tax, tip and the total. Ceiling the values and capping to two decimal places.
sales_tax = math.ceil(100 * charge_for_food * (1 + sales_tax_percentage / 100)) / 100
tip =  math.ceil(100 * charge_for_food * ( 1 + tip_percentage / 100)) / 100
total = charge_for_food + sales_tax + tip

# Printing in formatted string to have appropriate spacing.
print("\n")
print(f"{"":-<40}")
print(f"{"Food price":<33} {charge_for_food:.2f}")
print(f"{sales_tax_percentage}% {"Sales tax":<30} {sales_tax:.2f}")
print(f"{tip_percentage}% {"Tip":<29} {tip:.2f}")
print(f"{"":-<40}")
print(f"{"Total":<33} {total:.2f}")
print(f"{"":-<40}")
print("\n")

