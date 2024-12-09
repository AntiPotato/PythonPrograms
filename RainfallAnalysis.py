no_of_years = int(input("Enter no. of years you want to enter the rainfall data for.\n"))

no_of_months = 0
total_inches_of_rainfall = 0

# Loop through the no. of years.
for year in range(no_of_years):
        # Loop through the no. of months in a year.
	for month in range(12):
		# Take input from user and update the sum.
		total_inches_of_rainfall = total_inches_of_rainfall + float(input(f"Enter inches of rainfall for month number {month + 1} for year number {year + 1}\n"))
		# Update the month count.
		no_of_months = no_of_months + 1

# Calculate average and print results.
print("Number of months:", no_of_months)
print("Total inches of rainfall:", total_inches_of_rainfall)
print("Average rainfall per month for the entire period:", total_inches_of_rainfall / no_of_months)
		
 
