import pandas as pd
excel_file = r"C:\Users\Michael\Downloads\Records.csv"

df = pd.read_csv(excel_file)
print(df.head(10))

#Saves the max value in column total profit to variable max_profit_amount
max_profit_amount = (df['Total Profit'].max())
print(max_profit_amount)

#Searches for the row im which Total Profit is equal to max_profit_amount
max_profit_id = df.loc[df['Total Profit'] == max_profit_amount]
print(max_profit_id)

#Converts panda's datafram row to dict where keys are column names, values are lists of column data
dict_max_profit_id = max_profit_id.to_dict('list')
print(dict_max_profit_id)
print(dict_max_profit_id['Order ID']

#print(df.loc[1][1])
#print(df.loc[1]['Country'])