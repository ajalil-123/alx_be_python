
import datetime

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.datetime.now()
    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Print the formatted date and time
    print(f"Current Date and Time: {formatted_date}")

# Call the function to display the current date and time
display_current_datetime()


#enter_number = input("Enter the number of days to add to the current date:")


def calculate_future_date(number_of_days):
    # Get the current date and time
    current_date = datetime.datetime.now()
    # Create a timedelta object with the desired number of days
    future_date = current_date + datetime.timedelta(days=number_of_days)
    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date:{formatted_future_date}")


# Prompt the user for the number of days
try:
    enter_number = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(enter_number)
except ValueError:
    print("Please enter a valid integer for the number of days.")
