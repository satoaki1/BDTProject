import pandas as pd

# import .csv input into Pandas DataFrame
our_data = pd.read_csv("Kuala_Lumpur_house_prices.csv")

# drop the first column which name is "id"
our_data = our_data.drop("id", axis=1)
print(our_data)

# drop comma in data of current_price, convert each value from string to float
our_data['current_price'] = our_data['current_price'].str.replace(',', '').astype(float)
pd.options.display.float_format = '{:.2f}'.format

print(our_data.info())

print(our_data.describe())

our_data = our_data.dropna()

our_data = our_data.isna().sum()
our_data = pd.DataFrame(our_data, columns=["null values"])
print(our_data)

