from datetime import datetime


class time:
    def __init__(self):
        pass

    # Function to get current time as (hh:mm AM/PM)
    def current_time(self):
        return datetime.now().strftime("%I:%M %p")

    # Function to get current date as (Y:m:d)
    def current_date(self):
        return datetime.now().strftime("%Y:%m:%d")
