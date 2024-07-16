
# [Data Preprocessing]

'''
     Importing the Libraries

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
    Importing the Dataset

'''
dataset = pd.read_csv(r"C:\Users\ujjwa\Documents\Salary_Data.csv")
X = dataset.iloc[ :  ,  :-1].values
Y = dataset.iloc[ :  , -1].values

'''
    Splitting the dataset into the Training set and Test set

'''
from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size = 0.2 , random_state = 0)

# [Performing Simple Linear Regression]

'''
    Training the Simple Linear Regression model on the Training set

'''

from sklearn.linear_model import LinearRegression 
regressor = LinearRegression() 
regressor.fit(X_train , Y_train) 

'''
    Predicting the Test set results

'''

Y_predict = regressor.predict(X_test) 

'''
    Visualising the Training set results

'''

plt.scatter(X_train , Y_train , color = 'red') 
plt.plot(X_train , regressor.predict(X_train) , color = 'blue') 
plt.title('Salary vs Experience (Training set)') 
plt.xlabel('Years of Experience')
plt.ylabel('Salary')

plt.show()

'''
    Visualising the Test set results

'''
plt.scatter(X_test , Y_test , color = 'green')
plt.plot(X_train , regressor.predict(X_train) , color = 'blue') 
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of experience')
plt.ylabel('Salary')

plt.show()