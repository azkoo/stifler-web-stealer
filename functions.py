from datetime import datetime


# get today's year
def get_actual_year():
    current_time = datetime.now()
    year = current_time.year

    return year


# get today's month
def get_actual_month():
    # print(time.ctime(time.time()))
    # print(date.today())
    current_time = datetime.now()
    month = current_time.month

    return month


# get today's day
def get_actual_day():
    # print(time.ctime(time.time()))
    # print(date.today())
    current_time = datetime.now()
    day = current_time.day

    return day


# uses day, month and year value
# to formalize a date format
#dd/mm/yyyy
def formalize_date(day, month, year):
    date = str(day) + str(month) + str(year)

    return date
