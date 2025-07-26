import datetime
now = datetime.datetime.now()
current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current date and time: {current_datetime}")

number_of_days = int(input("Enter the number of days to add: "))
future_date = now + datetime.timedelta(days=number_of_days)
print(f"Future date after adding {number_of_days} days: {future_date.strftime('%Y-%m-%d')}")