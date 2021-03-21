
import datetime


month, year = input('Enter the month & year: ').split()
print('Yes' if datetime.datetime.strptime('13 '+' '+month+' '+year, '%d %m %Y').weekday()==4 else 'No')
