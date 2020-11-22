# Importing required modules
import os
import csv

# Setting file path to variable
csvpath = os.path.join("Resources", "election_data.csv")

# Creating Lists, dictionaries & variables to store data
votesTotal =[]
candidates = []
candidate_count_dict = {}
winner = None
max_count = 0

# Opening csv file to read file using file-handler
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# Looping through each data row in csvreader and appending data to new lists.
    for row in csvreader:
        votesTotal.append(row[0])

        candidates.append(row[2])

# Calculating Total votes, list of candidates
total_votes = len(votesTotal)
candidates.sort()
# Setting uniques candidates in 'uniqueCandidates' list
uniqueCandidates = set(candidates)

# Populating dictionary by counting repetetions of each 'uniqueCandidates' in 'candidates' lists
candidate_count_dict = {can:candidates.count(can) for can in uniqueCandidates}

# Writing the Results to Results.txt and terminal
with open('Analysis/Results.txt', "w", newline="") as file:

    file.write("\r\n")
    print(" ")

    file.write(f" **  ELECTION RESULTS  **\r\n")
    print(f" **  ELECTION RESULTS   **")

    file.write(" ------------------------\r\n")
    print("------------------------")

    file.write(f" The Total number of votes cast: {total_votes}\r\n")
    print(f" The Total number of votes cast: {total_votes}")

    file.write(" ------------------------\r\n")
    print("------------------------")

    file.write(f" List of candidates: {uniqueCandidates}\r\n")
    print(f" List of candidates: {uniqueCandidates}")

# Calculating percentage of votes won by each candidate and displaying them using for-loop
    for name in candidate_count_dict.keys():

# Using .format formatting percent until 3 decimals
        percent = "{:.3f}".format((candidate_count_dict[name]/total_votes)*100)

        file.write(f" {name}: ({percent}%) {candidate_count_dict[name]} \r\n")
        print(f" {name}: ({percent}%) {candidate_count_dict[name]} ")

# In same loop calculating winner and winning votes using if-conditional.
        if candidate_count_dict[name] > max_count:
            max_count = candidate_count_dict[name]
            winner = name
    
    file.write(" ------------------------\r\n")
    print("------------------------")
# Writing results to file and terminal
    file.write(f" Winner is '{winner}' with '{max_count}' votes !!!\r\n")
    print(f" Winner is '{winner}' with '{max_count}' votes !!!" )

    file.write(" ------------------------\r\n")
    print("------------------------")


   