import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
#np.random.seed(2017)
np.set_printoptions(precision=3, suppress=True)
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

print(tf.__version__)

#df=pd.read_csv('DataFiles/IowaHousingPrices.csv')
df = pd.read_csv('DataFiles/TrainData_v1.csv')
print ("--",df)

seed_value = 42
    
import os
os.environ['PYTHONHASHSEED']=str(seed_value)
import random
random.seed(seed_value)
np.random.seed(seed_value)




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
# 4. Set the `tensorflow` pseudo-random generator at a fixed value
tf.random.set_seed(seed_value)

model = keras.Sequential()
model.add(keras.layers.Dense(1, input_shape=(1,)))
model.compile(keras.optimizers.Adam(learning_rate=0.1), 'mean_squared_error')


#a=np.array(0.5,dtype="float32",ndmin=2)
#b=np.array(0,dtype="float32",ndmin=1)
#model.set_weights([a,b])
#a,b=model.get_weights()
#print("slope=",a[0][0],"intercept=",b[0])

model.fit(attendance,performance, epochs=50, batch_size=30,verbose =1)
print(model.evaluate(attendance,performance))
df.plot(kind='scatter',
       x='Attendance',
       y='Performance', title='Attendance vs Performance Data')
y_pred = model.predict(attendance)

mse = tf.keras.losses.MeanSquaredError()
m=mse(performance, y_pred).numpy()
print(m)
plt.plot(attendance, y_pred, color='red')
plt.show()








#plt.show()



plt.savefig('StraightLinFitKeras3.png')






