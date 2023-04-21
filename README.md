# Data science with Python3 and its libraries
This project is assessed during the Big Data Technology module in Taylor's University in Malaysia. With using python, we have prepared a dirty, raw unstructured data which is not cleaned yet, cleaned the data and customized to the structured data and created a prediction model due to the structured data.

Below are the Python libraries we have applied for this project:

* **Pandas**
* **Keras**
* **NumPy**
* **Tensorflow**

we have developed a predictive model to anticipate whether the real estate market in Kuala Lumpur would experience inflation in the future by utilizing a couple of factors that indicate strong correlations with the house prices. All those data is involved in `Kuala_Lumpur_house_prices.csv` file of .csv format, but these datasets are not optimized for the accurate, reliable prediction. Therefore, we have read data file, cleaned dirty datasets in the file using `NumPy` and `Pandas`. Finally, the cleaned structured data is saved in `Kuala_Lumpur_house_prices_clean.csv` .csv file. The sequence of works are saved in `clean-data.py` written in Python3.

Once the data is cleaned, build neural prediction model in `predict.py` with source code that is written in Python3. Cleaned datasets are load with `NumPy`, define and develop the neural prediction model using `Keras`. We have applied the prediction model for the real estate anticipation with the prediction model finally. 
