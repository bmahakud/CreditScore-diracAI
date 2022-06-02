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

df = pd.read_csv('DataFiles/TrainData_v1.txt')

print ("--",df)










