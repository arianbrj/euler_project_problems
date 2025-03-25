# the problem description:
# You are given the following information, but you may prefer to do some research for yourself.

#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

months = """January, February, March, April, May, June, July, August, September, October, November,  December"""


months = months.split(", ")


days = 0
sundays = 0
for year in range(1900, 2001):
    for month in months:
        if month == "February":
            if year % 4 == 0 and year % 100 != 0:
                days += 29
            elif year % 400 == 0:
                days += 29
            else:
                days += 28
        elif month in ["April", "June", "September", "November"]:
            days += 30
        else:
            days += 31
        if year > 1900 and days % 7 == 6:
            sundays += 1

print(sundays)