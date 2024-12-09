no_of_books_purchased = int(input("Enter the no. of books you have purchased this month. \n"))
points_earned = 0

# Check the range of purchased books to determine the points earned.
if no_of_books_purchased >= 8:
	points_earned = 60
elif no_of_books_purchased >= 6:
	points_earned = 30
elif no_of_books_purchased >= 4:
	points_earned = 15
elif no_of_books_purchased >= 2:
	points_earned = 5

print(f"You have earned {points_earned} points.")