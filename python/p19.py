#!/usr/bin/env python3

'''You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?'''

total = 0
day = (0 + 365) % 7

MONTHS = [31, 28, 31, 30, 31, 30,
          31, 31, 30, 31, 30, 31]

for year in range(1901, 2001) :
    for month in range(12) :
        if day == 6 : # 6 == Sunday
            total += 1
        if month == 1 and year % 4 == 0 and year % 400 != 0 :
            day = (day + 29) % 7
        else :
            day = (day + MONTHS[month]) % 7

print(total)
