#task1
from datetime import datetime
curr = datetime.now()
print("Current date: ", curr.strftime('%d.%m.%Y'))
year = curr.year
month = curr.month
day = curr.day - 5
if day <= 0:
    month -= 1
    if month == 0:
        month = 12
        year -= 1
        from calendar import monthrange as days
        day += days(year, month)[1]
new = datetime(year, month, day)
print("New date: ", new.strftime('%d.%m.%Y'))

#task2
from datetime import datetime
from calendar import monthrange as days
curr = datetime.now()
year = curr.year
month = curr.month
day = curr.day - 1
if day <= 0:
    month -= 1
    if month == 0:
        month = 12
        year -= 1
        day += days(year, month)[1]
new = datetime(year, month, day)
print("Yesterday: ", new.strftime('%d.%m.%Y'))
print("Today: ", curr.strftime('%d.%m.%Y'))

year = curr.year
month = curr.month
day = curr.day + 1
if day >= days(year, month)[1]:
    day = 1
    month += 1
    if month > 12:
        month = 1
        year += 1
new = datetime(year, month, day)
print("Tomorrow: ", new.strftime('%d.%m.%Y'))

#task3
from datetime import datetime
curr = datetime.now()
#curr.microsecond = 0
print(curr.strftime('%d.%m.%Y %H:%M:%S'))

#task4
from datetime import datetime
def diff(date1: str, date2: str, date_format: str = "%Y-%m-%d %H:%M:%S") -> int:
    dt1 = datetime.strptime(date1, date_format)
    dt2 = datetime.strptime(date2, date_format)
    return abs(int((dt2 - dt1).total_seconds()))

date1 = "2024-02-14 12:01:00"
date2 = "2023-02-15 14:50:00"
print(diff(date1, date2))
            
