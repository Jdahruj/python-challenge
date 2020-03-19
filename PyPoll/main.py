import pandas as pd

# Load csv file in current working directory into dataframe
df = pd.read_csv("election_data.csv")

# Store important values to be used later
totalVotes = df["Voter ID"].size
candidateVotes = df["Candidate"].value_counts()
candidatePercentage = df["Candidate"].value_counts(normalize=True).mul(100).round(1).astype(str) + "%"
winner = df["Candidate"].mode()

# Print intro
print("Election Results")

# Print divider
print("-------------------------------------")

# Print total votes by amount of rows in the table
print("Total Votes: " + str(totalVotes))

# Print total votes per candidate by counting how many cells contain 
# each candidate's name
print(candidateVotes.to_string())

# Print divider
print("-------------------------------------")

# Print each candidate's highest percentage of votes by dividing
# each candidate's total votes by the total amount of votes
print("\nPercentage of Total Votes:")
print(candidatePercentage.to_string())

# Print divider
print("-------------------------------------")

# Print the candidate with the highest number of votes using mode
print("\nWinner: " + winner.to_string(index=False))

# Print divider
print("-------------------------------------")

# Create new text file with read/write permission
file = open("output.txt", "w+")

# Copy all previous terminal outputs and writing them to a text file
file.write("Election Results")
file.write("\n-------------------------------------")
file.write("\nTotal Votes: " + str(totalVotes))
file.write("\nCandidates Votes: ")
file.write("\n" + candidateVotes.to_string())
file.write("\n-------------------------------------")
file.write("\nPercentage of Votes:\n" + candidatePercentage.to_string())
file.write("\n-------------------------------------")
file.write("\nWinner:" + winner.to_string(index=False))
file.write("\n-------------------------------------")


# Close and save file
file.close()