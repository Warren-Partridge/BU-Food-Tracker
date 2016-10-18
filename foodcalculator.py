import time;
WEEKDAY_DICT = {"Saturday": 0,
                "Sunday": 1,
                "Monday": 2,
                "Tuesday": 3,
                "Wednesday": 4,
                "Thursday": 5,
                "Friday": 6};
# This dictionary is indexed from Saturday because Friday is the day that
# meal swipes are reset. This way, getting distance to Friday is easier.

def getMealStatus(mealsPerWeek):
    weekday = time.strftime("%A");
    weekdayNum = WEEKDAY_DICT[weekday];
    print(weekdayNum);
    return mealsPerWeek;
