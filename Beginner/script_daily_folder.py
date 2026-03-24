import os
from datetime import datetime, timedelta

# Function to create the directory structure
def create_folder_structure(base_path):
    current_date = datetime.today()  # Get today's date
    current_year = current_date.year  # Current year
    current_month = current_date.month  # Current month
    current_day = current_date.day  # Current day

    # Loop through the current year and create folders for each month
    for year in range(current_year, current_year + 1):
        # Create year folder
        year_folder = str(year)
        year_path = os.path.join(base_path, year_folder)
        if not os.path.exists(year_path):
            os.makedirs(year_path)

        # Loop through each month from the current month to December
        for month in range(current_month, 13):
            # Create month folder (e.g., January, February, etc.)
            month_name = datetime(year, month, 1).strftime('%B')  # Get full month name
            month_path = os.path.join(year_path, month_name)
            if not os.path.exists(month_path):
                os.makedirs(month_path)

            # Create day folders (01, 02, ..., 31) for each month
            # Get the number of days in the current month
            next_month = month + 1 if month < 12 else 1
            next_month_year = year if month < 12 else year + 1
            last_day_of_month = datetime(next_month_year, next_month, 1) - timedelta(days=1)
            days_in_month = last_day_of_month.day

            # Create day folders from the current day to the last day of the month
            start_day = current_day if month == current_month else 1
            for day in range(start_day, days_in_month + 1):
                day_folder = os.path.join(month_path, f"{day:02d}")  # Ensure day is two digits (01, 02, ...)
                if not os.path.exists(day_folder):
                    os.makedirs(day_folder)

        # Reset current_month to 1 (January) for the next year
        current_month = 1

base_path = '/Users/ruchi/PycharmProjects/pythonProject'

create_folder_structure(base_path)

print("Folder structure created successfully!")


'''
The expression 0 0 1 * * is a cron schedule expression, which defines when a cron job should be executed. Let's break it down:

0: The minute part, meaning the job will run at the 0th minute (the start of the hour).
0: The hour part, meaning the job will run at 0 hours, i.e., midnight.
1: The day of the month part, meaning the job will run on the 1st day of the month.
*: The month part, meaning the job will run every month (no restriction).
*: The day of the week part, meaning the job will run regardless of the day of the week (no restriction).
Summary:
0 0 1 * * means the cron job will run at midnight (00:00) on the 1st day of every month, no matter what day of the week it is.

crontab -l

0 0 1 * * python3 /Users/ruchi/PycharmProjects/pythonProject/script_daily_folder.py

'''
