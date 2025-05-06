import pandas as pd

# Load the first CSV file
data1 = pd.read_csv("Top-Apps-in-Google-Play.csv")
df1 = pd.DataFrame(data1)

# Display the first rows and first column of the third dataset
print("Top Apps in Google Play:")
print(df1.iloc[1, :1])

# Load the second CSV file
data2 = pd.read_csv("BTC_DATA_V3.0.csv")
df2 = pd.DataFrame(data2)

# Display the first rows and first column of the third dataset
print("\nBTC Data:")
print(df2.iloc[1, :1])

# Load the third CSV file
data3 = pd.read_csv("programming language trend over time.csv")
df3 = pd.DataFrame(data3)

# Display the first rows and first column of the third dataset
print("\nProgramming Language Trend Over Time:")
print(df3.iloc[1, :1])