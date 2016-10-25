from foodcalculator import *;
import datetime;

weekdayArray = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

userPlan = " ";
currentDate = datetime.datetime.now();
fallSemesterStart = datetime.datetime(2016, 9, 6);
fallSemesterEnd = datetime.datetime(2016, 12, 12);
semesterLength = fallSemesterEnd - fallSemesterStart;
semesterElapsed = fallSemesterEnd - currentDate;

print("The current date is " + currentDate.strftime("%m/%d/%Y") + ", which is a " +\
      weekdayArray[currentDate.weekday()] + ".");
print("There are a total of %d days in the current semester. Today is day %d.\n"
      % (semesterLength.days, semesterElapsed.days));
# if date is between Sept 6 - Dec 12, it's fall semester
# if date is between Jan 19 - May 12, it's spring semester
# But since I can't scrape semester dates from BU website,
# they'll have to be magic dates

print("Hello! Which of the following meal plans are you currently using?");
print("1. Unlimited Plan\n2. 14-Plus Plan\n3. 9-Plus Plan\n4. 330 Plan\n" +\
	"5. 250 Plan\n6. Kosher Plan");

while userPlan not in "123456":
    userPlan = input("Type a number 1-6: ");
    if userPlan == "1":
        print("\nThe Unlimited Plan has no limit on dining hall meals and $195 dining dollars per semester.");
        print("");
        getDiningStatus(195, currentDate, fallSemesterStart, fallSemesterEnd);
    elif userPlan == "2":
        print("\nThe 14-Plus Plan has 14 meals per week and $250 dining dollars per semester.\n");
        getWeeklyMealStatus(14, currentDate);
        print("");
        getDiningStatus(250, currentDate, fallSemesterStart, fallSemesterEnd);
    elif userPlan == "3":
        print("\nThe 9-Plus Plan has 9 meals per week and $415 dining dollars per semester.\n");
        getWeeklyMealStatus(9, currentDate);
        print("");
        getDiningStatus(415, currentDate, fallSemesterStart, fallSemesterEnd);
    elif userPlan == "4":
        print("\nThe 330 Plan has 330 meals per semester and $305 dining dollars per semester.\n");
        getStandardMealStatus(330, currentDate, fallSemesterStart, fallSemesterEnd);
        print("");
        getDiningStatus(305, currentDate, fallSemesterStart, fallSemesterEnd);
    elif userPlan == "5":
        print("\nThe 250 Plan has 250 meals per semester and $575 dining dollars per semester.\n");
        getStandardMealStatus(250, currentDate, fallSemesterStart, fallSemesterEnd);
        print("");
        getDiningStatus(575, currentDate, fallSemesterStart, fallSemesterEnd);
    elif userPlan == "6":
        print("\nThe Kosher Plan has 11 Hillel meals per week and $265 dining dollars per semester.\n");
        getWeeklyMealStatus(11, currentDate);
        print("");
        getDiningStatus(265, currentDate, fallSemesterStart, fallSemesterEnd);
    else:
        print("I don't know what " + userPlan + " is.");
