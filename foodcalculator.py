import datetime;

# What the values of weekdayNum represent:
# "Friday": 1,
# "Saturday": 2,
# "Sunday": 3,
# "Monday": 4,
# "Tuesday": 5,
# "Wednesday": 6,
# "Thursday": 7};
#
# I am indexing them this way because meals are reset on Friday

def getMealStatus(mealsPerWeek, currentDate):
    weekdayNum = (currentDate.weekday() + 3) % 7;
    mealsEaten = (mealsPerWeek/7) * weekdayNum;
    print("At this point, you should have eaten about %.2f meals." % mealsEaten +\
          " That leaves %.2f meals left over the next %d days."
          % (mealsPerWeek-mealsEaten, 7-weekdayNum));
    return;
