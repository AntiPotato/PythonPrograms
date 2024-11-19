import sys

current_time_in_hours = int(input("Enter current time in hours.\n"))
if(current_time_in_hours < 0 or current_time_in_hours > 23):
	print("Invalid entry. Please run the program again and enter a value within the valid range of [0..23]")
	sys.exit()


no_of_hours_to_wait = int(input("Enter number of hours to wait for the alarm.\n"))
if(no_of_hours_to_wait < 0):
	print("I cannot walk in the past. Please send me to the future.")
	sys.exit()

print("\n")
print("Alarm goes off at", (current_time_in_hours + no_of_hours_to_wait) % 24)
print()
