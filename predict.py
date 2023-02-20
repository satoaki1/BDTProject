import pandas as pd
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

# import .csv input into Pandas DataFrame
our_data = pd.read_csv("Kuala_Lumpur_house_prices.csv")

our_data['current_price'] = our_data['current_price'].str.replace(',', '').astype(float)
pd.options.display.float_format = '{:.2f}'.format

# drops the null values in the dataset, save them to new .csv file
our_data = our_data.dropna()
our_data.to_csv("Kuala_Lumpur_house_prices_clean.csv", index=False)

# load the dataset
myData = loadtxt("Kuala_Lumpur_house_prices_clean.csv", delimiter=",", skiprows=1, usecols=(1, 2, 3, 4, 5, 6))
x = myData[:, 0:5]
y = myData[:, 5]

# define the keras model
model = Sequential()
model.add(Dense(5, input_dim=5, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the keras model on the dataset
model.fit(x, y, epochs=50, batch_size=10)

# evaluate the keras model
_, accuracy = model.evaluate(x, y)
print('Accuracy: %.2f' % (accuracy*100))

predictions = model.predict_on_batch(x)

for i in range(5):
    print(x[i].tolist(), "predicts", predictions[i], "ACTUAL", y[i])

