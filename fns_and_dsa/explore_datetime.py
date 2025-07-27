from datetime import datetime, timedelta
now = datetime.now()
def display_current_datetime():
    current_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_datetime}")
display_current_datetime()

def calculate_future_date

def display_future_date():
    number_of_days = int(input("Enter the number of days to add: "))
    future_date = now + timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
display_future_date()