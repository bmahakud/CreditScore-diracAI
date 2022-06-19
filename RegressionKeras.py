import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
np.set_printoptions(precision=3, suppress=True)
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

print(tf.__version__)

#df=pd.read_csv('DataFiles/IowaHousingPrices.csv')
df = pd.read_csv('DataFiles/TrainData_v1.csv')
print ("--",df)





#squareFeet = df[['SquareFeet']].values
#salePrice = df[['SalePrice']].values

attendance = df[['Attendance']].values
performance = df[['Performance']].values




#print ("shapeX: ",squareFeet.shape)
#print ("shapeY: ",salePrice.shape)


print ("shapeX: ",attendance.shape)
print ("shapeY: ",performance.shape)



#from DataLoader import LoadDataFromTxtFile
#trainingDataFile = "DataFiles/TrainData_v1.txt"
#nCol =2
#Xtrain,Ytrain = LoadDataFromTxtFile(trainingDataFile, nCol)



#print ("Xtrain.shape: ",Xtrain)
#print ("Ytrain.shape: ",Ytrain.shape)

#XtrainNew = np.delete(Xtrain, 0, 0).T
#YtrainNew = Ytrain.T
#print ("Xtrain new : ", XtrainNew.shape);
#print ("Ytrain new : ", YtrainNew.shape);



#define model to fit
model = keras.Sequential()
model.add(keras.layers.Dense(1, input_shape=(1,)))
model.compile(keras.optimizers.Adam(lr=1), 'mean_squared_error')

model.fit(attendance,performance, epochs=30, batch_size=10)
df.plot(kind='scatter',
       x='Attendance',
       y='Performance', title='Attendance vs Performance Data')
y_pred = model.predict(attendance)
plt.plot(attendance, y_pred, color='red')









#plt.show()



plt.savefig('StraightLinFitKeras3.png')






