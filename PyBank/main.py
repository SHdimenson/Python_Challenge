# Importing required modules
import os
import csv

# Setting file path to variable
csvpath = os.path.join("Resources", "budget_data.csv")

# Lists & variables to store data
month = []
change = []
net_PL = 0
previous = 0

# Defining functions for Average, Greatest_Increase & Greatest_Decrease on nested-list
def avg(list):
    sum = 0
    for sl in list:
        sum = sum + int(sl[1])
    return sum/ len(list) 
def max(list):
    max = 0
    for x in list:
        if x[1]>max:
            max = x[1]
            max_date = x[0]
    return [max_date, max]
def min(list):
    min = 0
    for x in list:
        if x[1]<min:
            min = x[1]
            min_date = x[0]
    return [min_date, min]

# Opening csv file to read using file-handler
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        
        # Adding all months to empty list month
        month.append(row[0])

        #Calculating net Profit/Losses by adding net_PL to current observation
        net_PL = int(row[1]) + net_PL

        # Calculationg Profit/Loss change occured between current observation, previous observation & Updating 'previous' to first value if previous observation is 0
        # Creating a nested list 'change' for each timeperiod consisting [month, change]
        if previous != 0:
            change.append([row[0], int(row[1])-int(previous)])
        previous = row[1]
    
# Calculating Total months
months = int(len(month))

# Calculating Average changes of Profit/Loss from nested-list 'change'
avg_change = round(avg(change), 2)

# Calculating Greatest_Increase & Greatest_Decrease using max(), min() on nested-list 'change'
max_list = max(change)
min_list = min(change)

# Writing the Results to Results.txt and printing them in terminal
with open('Analysis/Results.txt', "w", newline="") as file:
    file.write( "** Financial Analysis **\r\n")
    file.write(" ------------------------\r\n")

    print("** Financial Analysis **")
    print("------------------------")

    file.write(" \r\n")    
    print(" ")

    file.write(f"Total Months: {months}\r\n")
    print(f"Total Months: {months}")

    file.write(f"Net Profit/Loss: ${net_PL}\r\n")
    print(f"Net Profit/Loss: ${net_PL}")

    file.write(f"Average Change: ${avg_change}\r\n")
    print(f"Average Change: ${avg_change}")

    file.write(f"Greatest Increase in Profits: {max_list[0]} (${max_list[1]})\r\n")
    print(f"Greatest Increase in Profits: {max_list[0]} (${max_list[1]})")

    file.write(f"Greatest Decrease in Profits: {min_list[0]} (${min_list[1]})\r\n")
    print(f"Greatest Decrease in Profits: {min_list[0]} (${min_list[1]})")
