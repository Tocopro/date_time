
import calendar
from datetime import datetime, timedelta

import time
from datetime import datetime


date_str = "Mar 1 2022 6:20PM"
date_obj = datetime.strptime(date_str, '%b %d %Y %I:%M%p')
print(date_obj)

given_d = datetime(2022, 3, 2)
print("Given Date")
print(given_d)

days_2_sub = 30
res_date = given_d - timedelta(days=days_2_sub)
print("New Date")
print(res_date)

given_date1 = datetime(2022, 3, 30)
print("Given date is")
print(given_date1.strftime('%A %dth %B %Y'))

given_date2 = datetime(2022, 4, 24)
print(given_date2.today().weekday())

print(given_date2.strftime('%A'))

given_date3 = datetime(2022, 4, 25)
weekday = calendar.day_name[given_date3.weekday()]
print(weekday)

given_date4 = datetime(2022, 4, 25, 8, 00, 00)
print(given_date4)
days_2_add = 7
new_date = given_date4 + timedelta(days=days_2_add, hours=12)
print('New Date and Time')
print(new_date)

milliseconds = int(round(time.time() * 1000))
print("Milliseconds", milliseconds)

given_date5 = datetime(2022, 4, 25)
str_date = given_date5.strftime("%Y-%m_%d %H:%M:%S")
print(str_date)

given_date_6 = datetime(2022, 4, 25).date()
