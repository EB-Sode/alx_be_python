from datetime import datetime, timedelta


def display_current_datetime(): 
    # Get current date and time
    current_date = datetime.now()
    print("Today's date is:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    # Add 7 days (1 week) to get a future date
    current_date = datetime.now()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=number_of_days)

    print(f"{number_of_days} days from now will be:", future_date.strftime("%Y-%m-%d"))


display_current_datetime()
calculate_future_date()