'''
Task5. Date objects adding subtracting.
'''
from datetime import datetime, time
from datetime import timedelta
from dateutil.relativedelta import relativedelta


datestring  = str(input("Enter date in the format YYYY-MM-DD "))
datestring = datestring.split('-')
date = datetime(int(datestring[0]),int(datestring[1]),int(datestring[2]))
print(date)

print("Date 7 days and 12 hours from now is")
print((date + timedelta(days=7)+ relativedelta(hours=12)))

print("Date 4 months from now is")

newdate = date + relativedelta(months=4)
print(newdate)