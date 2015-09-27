"""
birthday.py
Author: Dina
Credit: Mr.Dennison, Jazzy, Anoushka
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

name = input (" Hello, what is your name?")
month = input (" Hi "+ name +", what was the name of the month you were born in?")
month = month.lower()
year = input (" And what year were you born in, " + name + "?")
day = input (" And the day?")
monthdate = month_name[todaymonth]
monthNow = monthdate.lower()

if month == "december" or month=="february" or month=="january":
    season = "winter"
elif month == "march" or month =="april" or month=="may":
    season = "spring"
elif month == "june" or month=="july" or month=="august":
    season = "summer"
elif month == "september" or month=="october" or month=="november":
    season = "fall"
else:
    print("I don't understand")
    
if month == "october" and day == "31":
    print("You were born on Halloween!")
elif month == monthNow and int(day) == todaydate:
    print("Happy Birthday!")
elif int(year) < 1980:
    print(name + ", you are a "+ season +" baby of the stone age.")
elif int(year) < 1990:
    print(name + ", you are a "+ season +" baby of the eighties.")
elif int(year) < 2000:
    print(name + ", you are a "+ season +" baby of the nineties.")
elif int(year) > 2000:
    print( " " + name + ", you are a "+ season +" baby of the two thousands.")