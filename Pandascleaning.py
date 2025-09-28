#Remove Rows
import pandas as pd 
df =pd.read_csv('hoteldata.csv')
print(df.to_string())

#Remove all rows with NULL values:
new_df = df.dropna()
print(new_df.to_string())

#Replace Empty Values
#new_df = df.fillna(0)
#print(new_df.to_string())

#Replace NULL values with the number 130:
#df.fillna(120, inplace=True)
#print(df.to_string())

#Replace NULL values with the number 130:
df.fillna({"booking_date":"21-07-2025"},inplace=True)
print(df.to_string())

#Calculate the MEAN, and replace any empty values with it:
#x = df["revenue"].median()
#df["revenue"].fillna(x, inplace=True)
#print(df.to_string())

#Calculate the MODE, and replace any empty values with it:
x = df["revenue"].median()
df.fillna({"revenue": x}, inplace=True)


