<img src="https://github.com/tn64/Election_Analysis/blob/main/Resources/vote.png">

# Election Analysis

## Overview of Election Audit: Explain the purpose of this election audit analysis.
In the scenario for this module, we were tasked with creating a program to analyze election data from a recent congressional election with votes from three Colorodo counties. Having already determined the total votes, individual candidate votes, candidate vote percentages, and declared the winner for the election, we were to write code that would now determine the vote count and percentages from the three individual counties and determine which county had the largest turnout. The results of the code were then printed to a .txt file.

## Election-Audit Results: Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.
The program was able to return to following information

- How many votes were cast in this congressional election?
After setting a dictionary and list to hold the total votes and candidate names and votes. The following for loop was created to retrieve the total number of votes while at the same time retrieving the votes for each candidate by name from the provided .csv file:
```
    for row in reader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        county_name = row[1]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
```
This povided the following result for the total number of votes cast in the election:
PHOTO HERE

- The number of votes and the percentage of total votes for each county in the precinct.
Immediately following the if statement above, a second if statement was created to retrieve the county names and vote information from the provided .csv file:
```
        if (county_name) not in (county_options):
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1
```
The provided the county name, percentage of total votes, and the number of votes cast in each county:
PHOTO HERE

- Which county had the largest number of votes?
From the data collected in the above for loop, we were able to determine which county cast the largest number of votes and then print the results using the following:
```
 for county_name in county_votes:
        votes = county_votes[county_name]
        county_votes_percentage = float(votes) / float(total_votes) *100
        county_results = (
            f"{county_name}: {county_votes_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        txt_file.write(county_results)
        if (votes > winning_county_count):
            winning_county_count = votes
            largest_county = county_name
    largest_turnout = (
        f"\n-------------------------\n"
        f"Largest County Turnout: "
        f"{largest_county}\n"
        f"-------------------------\n")
    print (largest_turnout)             
```            
This provided the following result for which county cast the largest number of votes:
PHOTO HERE

- The number of votes and the percentage of the total votes each candidate received.
As stated above, the total number of votes and the number of votes each candidate received were retrieved in the first for loop and added to the dictionary. We were also able to deterine the percentage of votes cast using the following:
```
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"\n{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
```
This provided the following result for the vote percentage and number of votes cast for each candidate:
PHOTO HERE

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
Finally, we were able to determine which candidate won the election, how many votes they received, and the percentage of votes they received from the number of total votes cast:
```
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    winning_candidate_summary = (
        f"\n-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
```
## Election-Audit Summary: 
As demonstrated, the code written for this particular Board of Elections was able to provide the requested information from the provided .csv file. We propose that the Board of Elections (as well as other county boards) purchase this code to use in future elections. Additionally, this script could be modified for other elections as well.

### Modification 1
The script could be modified for use in other state and local elections for more than one office

### Modification 2:
The script could also be modified for use in obtaining the results of ballot initiatives.
