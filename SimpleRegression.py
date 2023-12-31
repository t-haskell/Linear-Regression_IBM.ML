''' 
Project by -> Thomas Haskell

Topic -> Simple Linear Regression
Source -> IBM Machine Learning with Python Certification Course

Below is a translation of a Jupyter notebook program to Python. Using IBM technologies, 
this program is able to predict the CO2 emissions based on varying features of a car.

The focus of this project is on simple linear regression modeling, where one independent
variable is used to predict the dependent variable (CO2 Emissions).

'''


import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

# Downloading data set from IBM Cloud
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"
path= "/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"
import http.client
import urllib.request
import ssl

global IND_VAR
IND_VAR = "FUELCONSUMPTION_COMB"

# workaround for SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

def download(url, path, filename):
    urllib.request.urlretrieve(url, filename)
    print("Download Complete")
    
# now calling the function to grab the data
download(url, path, "FuelConsumptionCo2.csv")
    
# putting the data into a pandas dataframe
df = pd.read_csv("FuelConsumptionCo2.csv")
print(df.head())

# summarize the data
print(df.describe())

# selecting features
cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
print(cdf.head(9))

# visualize the features
viz = cdf[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
viz.hist()
plt.show()

# Combined Fuel Consumption vs CO2 Emission
plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("FUELCONSUMPTION_COMB")
plt.ylabel("Emission")
plt.show()

# Engine Size vs CO2 Emission
plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

# Number of Cylinders vs CO2 Emission
plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS, color="red")
plt.xlabel("# of Cylinders")
plt.ylabel("Emissions")
plt.show()

###########  Model Training  ###########

# splitting traininng and testing datasets
msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

# Adjusdting indendent vartiable to global value
if IND_VAR == "ENGINESIZE":
    testVariable = test.ENGINESIZE
    trainVariable = train.ENGINESIZE
if IND_VAR == "FUELCONSUMPTION_COMB":
    testVariable = test.FUELCONSUMPTION_COMB
    trainVariable = train.FUELCONSUMPTION_COMB


# visualizing the training data distribution
plt.scatter(trainVariable, train.CO2EMISSIONS,  color='blue')
plt.xlabel(IND_VAR)
plt.ylabel("Emission")
plt.title("Training Data Distribution")
plt.show()

# visualizing the testing data distribution
plt.scatter(testVariable, test.CO2EMISSIONS,  color='blue')
plt.xlabel(IND_VAR)
plt.ylabel("Emission")
plt.title("Testing Data Distribution")
plt.show()

#using sklearn to model the data
from sklearn import linear_model

regrML = linear_model.LinearRegression()
train_x = np.asanyarray(train[[IND_VAR]])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regrML.fit(train_x, train_y)
# printing the found optimal coefficients from line above
print("Coefficients: ", regrML.coef_)
print("Intercept: ", regrML.intercept_)

# plotting line of regression
plt.scatter(trainVariable, train.CO2EMISSIONS,  color='blue')
plt.plot(trainVariable, regrML.coef_[0][0]*trainVariable + regrML.intercept_[0], '-r')
plt.xlabel(IND_VAR)
plt.ylabel("Emission")
plt.title("Linear Regression Line of Best Fit")
plt.show()


####################  Model Testing/Evaluation  ##################

# focusing on Mean Squared Error (MSE)
from sklearn.metrics import r2_score

# Calculating predictions using test data
test_x = np.asanyarray(test[[IND_VAR]])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
predictions = regrML.predict(test_x)    # is vector of dependent variable predictions

mae = np.mean(np.abs(predictions - test_y))
mse = np.mean((predictions - test_y) ** 2)
r2 = r2_score(test_y, predictions)

print(f"Mean Squared Error ('Residual sum of squares'): {round(mse, 2)}")
print(f"Mean Absolute Error: {round(mae, 2)}")
print(f"R-squared: {round(r2, 2)}")


# Q: Is the error worse with fuel consumption or engine size as the indpendent variable?

# A: Yes, the mean absolute error is lower with engine size as the indpendent variable





            
    



