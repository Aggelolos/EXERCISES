year = int(input('What year?'))
if year % 4 == 0 and year % 100 != 0:
    print (year , 'is a leap year')
elif year % 400 == 0 and year % 4 == 0:
    print (year , 'is a leap year')
else:
    print(year , 'is not a leap year')