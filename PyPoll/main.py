import os
import pandas as pd

df = pd.read_csv("election_data.csv")

print("Total Votes: " + str(df["Voter ID"].size))
print(df['Candidate'].value_counts())
print("Percentage of Total Votes:")
print(df["Candidate"].value_counts()/df["Voter ID"].size)
print("Winner: " + df["Candidate"].mode())

file = open('output.txt', 'w+')

file.write('Total Votes: ' + str(df['Voter ID'].size))
file.write("\nCandidates Votes: ")
file.write("\n" + str(df['Candidate'].value_counts()))
file.write("\nPercentage of Votes:\n" + str(df['Candidate'].value_counts()/df["Voter ID"].size))
file.write('\nWinner:\n' + str(df['Candidate'].mode()))


file.close()