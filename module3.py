def calculateMealPrice():
    mealPrice = float(input("Enter Meal Price: "))
    tip = round(mealPrice * .18, 2)
    salesTax = round(mealPrice * .07, 2)
    totalPrice = round(mealPrice + tip + salesTax, 2)
    print("Tip: $",tip)
    print("Sales Tax: $",salesTax)
    print("Total Meal Price: $",totalPrice)


def calculateAlarmTime():
    currentTime = int(input("Enter Current Time: "))
    while currentTime > 24 or currentTime < 0:
        currentTime = int(input("Please Enter Valid Current Time: "))
    hoursToAlarm = int(input("Enter Number of Hours to Alarm: "))
    alarmTime = (currentTime + hoursToAlarm) % 24
    print("Time Alarm Will Sound: ", alarmTime)

def main():
    calculateMealPrice()
    calculateAlarmTime()

if __name__== "__main__":
    main()
