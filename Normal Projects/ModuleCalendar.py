import calendar

# It will return 13 because there are 13 leapdays between 2000 and 2050.
leapdays = calendar.leapdays(2000, 2050)
print(f"Leapdays: {leapdays}")

# It will return either true or false because it takes one year as an argument. And checks that given year is a leap year or not!
is_leap = calendar.isleap(2002)
print(is_leap)


