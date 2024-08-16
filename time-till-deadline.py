from datetime import datetime

user_input = input("enter your goal with a deadline (MM.DD.YYYY) separated by colon: ")
goal, deadline = user_input.split(":")

deadline_date = datetime.strptime(deadline, "%m.%d.%Y")

# calculate how many days are left until the deadline
todays_date = datetime.today()
time_left = deadline_date - todays_date
print(f"You have {time_left.days} days left to {goal}.")
