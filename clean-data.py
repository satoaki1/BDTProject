import pandas as pd

# import .csv input into Pandas DataFrame
our_data = pd.read_csv("Kuala_Lumpur_house_prices.csv")

# drop the first column which name is "id"
our_data = our_data.drop("id", axis=1)

# drop comma in data of current_price, convert each value from string to float
our_data['current_price'] = our_data['current_price'].str.replace(',', '').astype(float)
pd.options.display.float_format = '{:.2f}'.format

print(our_data.info())

print(our_data.describe())

# Calculate the mean of the ignoring null values
mean_num_of_rooms = our_data['num_of_rooms'].mean(skipna=True)
mean_elapsed_years = our_data['elapsed_years'].mean(skipna=True)
mean_crime_rates = our_data['crime_rates'].mean(skipna=True)

# Replace null values in the columns with the mean value
our_data['num_of_rooms'].fillna(mean_num_of_rooms, inplace=True)
our_data['elapsed_years'].fillna(mean_elapsed_years, inplace=True)
our_data['crime_rates'].fillna(mean_crime_rates, inplace=True)


# Define a function to remove outliers from a column and replace with the mean
def remove_outliers_and_replace(column):
    z_scores = (column - column.mean()) / column.std()
    threshold = 3
    outlier_mask = z_scores.abs() > threshold
    column_copy = column.copy()
    column_copy[outlier_mask] = column.mean()
    return column_copy


# Remove outliers from the 'crime_rates' and 'num_of_rooms' columns and replace with the mean
our_data['crime_rates'] = remove_outliers_and_replace(our_data['crime_rates'])
our_data['num_of_rooms'] = remove_outliers_and_replace(our_data['num_of_rooms'])

# Write the updated DataFrame back to a new CSV file
our_data.to_csv('new_our_data.csv', index=False)

# Drop rows with null values in the 'Expensive' column
our_data.dropna(subset=['Expensive'], inplace=True)

# Write the updated DataFrame back to a new CSV file
our_data.to_csv('Kuala_Lumpur_house_prices_clean.csv', index=False)

print(our_data.info())
print(our_data.describe())

our_data = our_data.isna().sum()
our_data = pd.DataFrame(our_data, columns=["null values"])
print(our_data)
