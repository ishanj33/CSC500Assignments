def calcAvgRainfall():
    num_years = int(input("Enter the number of years: "))
    while num_years < 1:
        int(input("Please enter a valid number of years: "))
    total_inches = 0
    for year_idx in range(num_years):
        for month_idx in range(12):
            rain_inches = float(input(f"Enter the number of inches of rain for year {year_idx+1} month {month_idx+1}: "))
            while rain_inches < 0:
                rain_inches = float(input(f"Please enter a valid number of inches of rain for year {year_idx+1} month {month_idx+1}: "))
            total_inches += rain_inches
    num_months = num_years * 12
    avg_rainfall = round(total_inches / num_months, 2)
    print("Total Number of Months: ", num_months)
    print("Total Inches of Rainfall", total_inches) 
    print("Average Rainfall per Month: ", avg_rainfall, "inches per month")

def bookClub():
    num_books = int(input("Enter the number of books purchased: "))
    while num_books < 0:
        num_books = int(input("Please Enter a valid number of books purchased: "))
    total_points = 0
    if num_books < 2:
        total_points = 0
    elif num_books == 2 or num_books == 3 :
        total_points = 5
    elif num_books == 4 or num_books == 5:
        total_points = 15
    elif num_books == 6 or num_books == 7:
        total_points = 30
    else:
        total_points = 60
    print("Points earned: ", total_points)

def main():
    calcAvgRainfall()
    bookClub()

if __name__== "__main__":
    main()
