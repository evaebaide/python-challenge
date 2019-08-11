import os
import csv

#Set the path for the CSV file

Budget_csv = os.path.join("budget_data.csv")

#Create the lists to store data.

profit = []
monthly_changes = []
date = []
change_alt = []

# Initialize variables

monthcount = 0
total_profitloss = 0
total_profitChange = 0
initial_profit = 0

# Open and read the CSV

with open(Budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Increase counter for number of months in dataset
    for row in csvreader:
        # Use count to count the number months in this dataset
        monthcount = monthcount + 1

        # Needed for greatest increase and decrease in profits
        date.append(row[0])

        # Append the profit and calculate the total profit
        profit.append(row[1])
        total_profitloss = total_profitloss + int(row[1])

        #Get the verage change in profits from month to month.  And the average change in profits
        final_profit = int(row[1])
        monthly_profitChange = final_profit - initial_profit

        #Store these monthly changes in a list
        monthly_changes.append(monthly_profitChange)

        total_profitChange = total_profitChange + monthly_profitChange
        initial_profit = final_profit

        #Calculate the average profit change
        average_profitChange = total_profitChange/monthcount

        #Find the max and min profit change and the dates.
        greatest_profitIncrease = max(monthly_changes)
        greatest_profitDecrease = min(monthly_changes)

        ProfitIncrease_date = date[monthly_changes.index(greatest_profitIncrease)]
        ProfitDecrease_date = date[monthly_changes.index(greatest_profitDecrease)]

    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(monthcount))
    print("Total Profits: " + "$" + str(total_profitloss))
    print("Average Change: " + "$" + str(int(average_profitChange )))
    print("Greatest Increase in Profits: " + str(ProfitIncrease_date) + " ($" + str(greatest_profitIncrease) + ")")
    print("Greatest Decrease in Profits: " + str(ProfitDecrease_date) + " ($" + str(greatest_profitDecrease)+ ")")
    print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(monthcount) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profitloss ) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_profitChange)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(ProfitIncrease_date) + " ($" + str(greatest_profitIncrease) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(ProfitDecrease_date) + " ($" + str(greatest_profitDecrease) + ")\n")
    text.write("----------------------------------------------------------\n")
