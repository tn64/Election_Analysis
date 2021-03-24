#See problem with line 64

# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete lisst of candidates who received votes
# 3. the percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os
#Assign a variable to load the file from a  path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("Resources", "Analysis", "election_analysis.txt")

#1. Initialize the total vote counter
total_votes = 0

#Declare Candidate options list
candidate_options = []
#Declare candidate votes dictionary
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)

    #Print each row in the csv file
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        #If candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of options
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#Determine the percentage of votes for each candidate by looping through the counts
#Iterate through the candidate list
for candidate_name in candidate_votes:
    #Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    #Determine winning vote count and candidate
    #Determine if the votes is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #If true then set winning_count = votes and winning_percent = vote percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #And set the winning_candidate equal to the candidate's name
        winning_percentage = candidate_name

#3 Print each candidate's name, vote count, and percentage of votes
winning_percentage_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"___________________________\n")
print(winning_percentage_summary)

