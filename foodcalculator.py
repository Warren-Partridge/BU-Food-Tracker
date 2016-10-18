import datetime;
WEEKDAY_DICT = {"Saturday": 0,
                "Sunday": 1,
                "Monday": 2,
                "Tuesday": 3,
                "Wednesday": 4,
                "Thursday": 5,
                "Friday": 6};
# This dictionary is indexed from Saturday because Friday is the day that
# meal swipes are reset. This way, getting distance to Friday is easier.

def getMealStatus(mealsPerWeek, currentDate):
    print((currentDate.weekday() + 2) % 7);
    # This should print the weekday as if the week began on Saturday
    # The reason I want that is so that Friday is the last day of the week,
    # which is the day the meal plan is reset.
    return mealsPerWeek;