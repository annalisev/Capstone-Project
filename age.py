from datetime import date, datetime
# setting todays date, and telling the user this
today = date.today()
print("Today's date is", today)

# asking user to input their desired date for calculation
new_date = input("Input a date in DD-MM-YYYY format: ")
date1 = date(int(new_date[6:]), int(new_date[3:5]), int(new_date[:2]))

# calculating the difference in days then converting this to years
time_to_date = abs(today - date1)
years = time_to_date.days / 365.25
print(f'It has been {int(years)} years since {new_date}')
