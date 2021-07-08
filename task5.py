'''
Task5. Date objects adding subtracting.
'''
from datetime import datetime, time
from datetime import timedelta
from dateutil.relativedelta import relativedelta

import sys

def main(argv):
    datestring  = argv[0]
    date = datetime.strptime(datestring, "%y-%m-%d")
    print("Date 7 days and 12 hours from now is {}".format(date + timedelta(days=7)+ relativedelta(hours=12)))
    print("Date 4 months from now is {}".format(date + relativedelta(months=4)))

if __name__ == "__main__": 
    
    main(sys.argv[1:])