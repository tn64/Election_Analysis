# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete lisst of candidates who received votes
# 3. the percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os
#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("Resources", "Analysis", "election_analysis.txt")

#Using the with statement open the file as a text file.
with open(file_to_load) as election_data:

#To do: read and analyze the data here

#Read the file object with the reader function
    file_reader = csv.reader(election_data)
    #Print the header row
    headers = next(file_reader)
    print(headers)


