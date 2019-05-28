import pandas as pd
excel_file = r"C:\Users\Michael\Downloads\Records.csv"

df = pd.read_csv(excel_file)
print(df.head(10))

#Saves the max value in column total profit to variable max_profit_amount
max_profit_amount = (df['Total Profit'].max())

#Order Number
num_max_profit = df.loc[df['Total Profit'] == max_profit_amount, 'Order ID'].item()

#Index Values
#Searches for the row im which Total Profit is equal to max_profit_amount
#Saves the index of the row df_make_profit_id as a value
df_max_profit_id = df.loc[df['Total Profit'] == max_profit_amount]
index_max_profit = (df_max_profit_id.index.item())

#Converts panda's datafram row to dict where keys are column names and values are lists of column data
#Assigns max_profit_id the value of the key Order ID
# dict_max_profit_id = df_max_profit_id.to_dict('list')
# max_profit_id = (dict_max_profit_id['Order ID'])

print(f"The max profit is: ${max_profit_amount}")
print(f"Found in order #:  {num_max_profit}")
print(f"At index value: {index_max_profit}\n")

#print(df.loc[1][1])
#print(df.loc[1]['Country'])


#Saves the max value in column total profit to variable max_profit_amount
min_profit_amount = (df['Total Profit'].min())

#Order Number
num_min_profit = df.loc[df['Total Profit'] == min_profit_amount, 'Order ID'].item()

#Index Values
#Searches for the row im which Total Profit is equal to min_profit_amount
#Saves the index of the row df_make_profit_id as a value
df_min_profit_id = df.loc[df['Total Profit'] == min_profit_amount]
index_min_profit = (df_min_profit_id.index.item())

print(f"The min profit is: ${min_profit_amount}")
print(f"Found in order #:  {num_min_profit}")
print(f"At index value: {index_min_profit}")
