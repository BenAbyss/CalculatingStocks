import time
def getCurrentInfo():
    CurrentPrice = int(input("Please enter the current price"))
    CurrentDividend = int(input("Please enter the current dividend payout"))
    ExpectedDividendGrowth = int(input("Please enter the expected dividend growth"))
    return CurrentPrice, CurrentDividend, ExpectedDividendGrowth

def calculateFutureStockPrice(CurrentPrice, CurrentDividend, ExpectedDividendGrowth):
    StockExpectedGrowth = ((CurrentDividend/CurrentPrice) + (ExpectedDividendGrowth/100)) + 1
    FiveYearsOrSpecific = input("Would you like to see the predicted output for the next five years, or for a certain year? F/C")
    return StockExpectedGrowth, FiveYearsOrSpecific

def specificYear(CurrentPrice, ExpectedGrowth):
    YearWanted = input("What year would you like to know?")
    CurrentYear = time.strftime("%Y")
    YearsAway = int(YearWanted) - int(CurrentYear)
    EstimatedPrice = round((ExpectedGrowth**YearsAway)*CurrentPrice, 2)
    print("In", YearsAway, "years, the expected price of this stock is", EstimatedPrice)

def fiveYears(CurrentPrice, ExpectedGrowth):
    print("year  |  1", end="")
    for x in range(2, 6):
        print("      ", x, end="")
    print()
    for x in range(0,50):
        print("-", end="")
    print()
    print("price |", end="")
    for x in range(1, 6):
        print(" ", round((ExpectedGrowth**x)*CurrentPrice, 2), end="")

def main():
    CurrentPrice, CurrentDividend, ExpectedDividendGrowth = getCurrentInfo()
    StockExpectedGrowth, FiveYearsOrSpecific = calculateFutureStockPrice(CurrentPrice, CurrentDividend, ExpectedDividendGrowth)
    if FiveYearsOrSpecific == "F":
        fiveYears(CurrentPrice, StockExpectedGrowth)
    else:
        specificYear(CurrentPrice, StockExpectedGrowth)

main()