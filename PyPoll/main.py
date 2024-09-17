#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
from pathlib import Path
from datetime import datetime

# Define the relative path to the data file
data_file = Path('Desktop/Data Science Boot/Grade/PC/PyPoll/Resources/election_data.csv')

# Print paths for debugging
print(f"Data file path: {data_file.resolve()}")

try:
    # Read the CSV file using the relative path
    with open(data_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        
        # Skip the header row
        header = next(reader)
        
        if 'Ballot ID' not in header or 'Candidate' not in header:
            raise ValueError("The required 'Voter ID' or 'Candidate' column is missing from the data.")

        # Create a dictionary to store vote counts for each candidate
        vote_counts = {}

        total_votes = 0  # Counter for total number of votes
        
        # Iterate through each row
        for row in reader:
            total_votes += 1
            candidate = row[2].strip()  # Assuming the 'Candidate' is in the 3rd column
            
            if candidate in vote_counts:
                vote_counts[candidate] += 1
            else:
                vote_counts[candidate] = 1
        
        if total_votes == 0:
            raise ValueError("No votes found in the CSV file.")
        
        # Prepare the list of candidates
        candidates = list(vote_counts.keys())

        # Calculate the percentage of votes each candidate won
        percentage_per_candidate = {candidate: (votes / total_votes) * 100 for candidate, votes in vote_counts.items()}
        
        # Determine the winner of the election based on popular vote
        winner = max(vote_counts, key=vote_counts.get)

        # Prepare results for printing
        results = (
            f"Total number of votes cast: {total_votes}\n"
            f"Complete list of candidates: {', '.join(candidates)}\n\n"
        )
        
        results += "Vote Counts and Percentages:\n"
        for candidate in candidates:
            vote_count = vote_counts[candidate]
            vote_percentage = percentage_per_candidate[candidate]
            results += f"{candidate}: {vote_count} votes ({vote_percentage:.2f}%)\n"
        
        results += f"\nThe winner of the election is: {winner}\n"

        # Print results to the terminal
        print(results)
        
        # Define path for output file (relative path)
        output_file = Path('Desktop/Data Science Boot/Grade/PC/PyPoll/analysis/election_analysis.txt')
        
        # Create parent directories for the output file if they don't exist
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Export results to a text file
        with open(output_file, 'w') as file:
            file.write(results)

except FileNotFoundError:
    print("The file was not found. Please check the file path.")
except ValueError as ve:
    print(f"ValueError: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# In[ ]:




