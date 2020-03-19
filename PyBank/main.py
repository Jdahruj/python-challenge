import pandas as pd

# Load csv file in current working directory into dataframe
df = pd.read_csv("budget_data.csv")

# Store important values to be used later
totalMonths = df["Date"].size
totalPL = df["Profit/Losses"].sum()
averageChange = (totalPL/totalMonths)
PLmax = df["Profit/Losses"].max()
PLmin = df["Profit/Losses"].min()

# Print each answer to terminal
print("Finacial Analysis")
print("------------------------------------------------")
print("Total Months: " + str(totalMonths))
print("Total: $" + str(totalPL))
print("Average Change: $" + str(averageChange))
print("Greatest Increase in Profits: $" + str(PLmax))
print("Greatest Decrease in Profits: $" + str(PLmin))

# Create new text file with read/write permission
file = open("output.txt", "w+")

# Copy all previous terminal outputs and writing them to a text file
file.write("Finacial Analysis\n")
file.write("------------------------------------------------\n")
file.write("Total Months: " + str(totalMonths))
file.write("\nTotal: $" + str(totalPL))
file.write("\nAverage Change: $" + str(averageChange))
file.write("\nGreatest Increase in Profits: $" + str(PLmax))
file.write("\nGreatest Decrease in Profits: $" + str(PLmin))


# Close and save file
file.close()