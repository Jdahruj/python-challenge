import pandas as pd

df = pd.read_csv("budget_data.csv")

print("Total Months: " + str(df["Date"].size))
print("Total: $" + str(df["Profit/Losses"].sum()))
print("Average Change: $" + str(df["Profit/Losses"].mean()))
print("Greatest Increase in Profits: $" + str(df['Profit/Losses'].max()))
print("Greatest Decrease in Profits: $" + str(df['Profit/Losses'].min()))

file = open("output.txt", "w+")

file.write("Total Months: " + str(df["Date"].size))
file.write("\nTotal: $" + str(df["Profit/Losses"].sum()))
file.write("\nAverage Change: $" + str(df["Profit/Losses"].mean()))
file.write("\nGreatest Increase in Profits: $" + str(df["Profit/Losses"].max()))
file.write("\nGreatest Decrease in Profits: $" + str(df["Profit/Losses"].min()))


file.close()