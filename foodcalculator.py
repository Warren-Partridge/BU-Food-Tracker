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

def getWeeklyMealStatus(mealsPerWeek, currentDate):
    weekdayNum = (currentDate.weekday() + 3) % 7;
    mealRate = mealsPerWeek/7;
    mealsEaten = mealRate * weekdayNum;
    print("You should be eating about %.1f meals per day. At this point in the week (assuming you ate today), you should have eaten about %.1f meals."
          % (mealRate, mealsEaten) +\
          " That leaves %.1f meals left over the next %d days, until they are reset to %d on Friday morning."
          % (mealsPerWeek-mealsEaten, 7-weekdayNum, mealsPerWeek));
    return None;

def getStandardMealStatus(mealsPerSemester, currentDate, startDate, endDate):
    semesterLength = endDate - startDate;
    semesterElapsed = currentDate - startDate;
    mealRate = mealsPerSemester/semesterLength.days;
    mealsEaten = mealRate * semesterElapsed.days;
    
    print("At this point in the semester (assuming you ate today), you should have eaten %.1f meals so far."
          % mealsEaten +\
          " That leaves %.1f to spend over the next %d days. Statistically, you should eat %.1f per day."
          % (mealsPerSemester-mealsEaten, semesterLength.days-semesterElapsed.days, mealRate));
    return None;

def getDiningStatus(diningPoints, currentDate, startDate, endDate):
    semesterLength = endDate - startDate;
    semesterElapsed = currentDate - startDate;
    pointsRate = diningPoints/semesterLength.days;
    pointsUsed = pointsRate * semesterElapsed.days;
    
    print("At this point in the semester, you should have spent $%.2f dining dollars."
          % pointsUsed +\
          " That leaves $%.2f to spend over the next %d days. Statistically, you should use $%.2f per day."
          % (diningPoints-pointsUsed, semesterLength.days-semesterElapsed.days, pointsRate));
    return None;
