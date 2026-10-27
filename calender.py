import calendar
import datetime

try :
    while True:
        month = int(input('Enter a month:')) 
        year = int(input('enter a year:'))
        if 1 <= month <=12 and year > 0:
            print(calendar.month(year,month))
            
        else :
            print("Invalid month and year !")
        print("Thankyou for using !")
except ValueError:
    print("Invalid!Enter valid year and month")

