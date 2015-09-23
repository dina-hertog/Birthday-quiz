"""
birthday.py
Author: Dina
Credit: <list sources used, if any>
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
name = input ("Hello, what is your name?")
month = input ("Hi "+ name +", what was the name of the month you were born in?")
year = input ("And what year were you born in, " + name + "?")
day = input ("And the day?")

if month == "october" and day == "31":
    print("You were born on Halloween!")
elif month == "september" and day == "23":
    print("Happy Birthday!")
elif month == "december" or month=="february" or month=="january":
    season = "winter"
elif month == "march" or month =="april" or month=="may":
    season = "spring"
elif month == "june" or month=="july" or month=="august":
    season = "summer"
elif month == "september" or month=="october" or month=="november":
    season = "fall"
    
if int(year) < int(1980):
    era= " stone age"
elif int(year) < 1989:
    era = " eighties"
elif int(year) < int(1999):
    era = " nineties"
elif int(year) >= int(2000):
    era = " two thousands"
    
print(name + ", you are a "+ season +" baby of the"+ era +".")
