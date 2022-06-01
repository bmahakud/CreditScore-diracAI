from DataLoader import LoadDataFromTxtFile
import ROOT
from array import array





nCol =2

trainingDataFile = "TrainDataStLineDecimal.txt"
testDataFile = "TestDataStLine.txt"


Xtrain,Ytrain = LoadDataFromTxtFile(trainingDataFile, nCol)
print ("Xtrain.shape: ", Xtrain.shape)
print ("Xtrain: ", Xtrain)
print ("Ytrain.shape: ", Ytrain.shape)
print ("Ytrain: ", Ytrain)


n = Xtrain.shape[1]



print ("List :   ",list(Ytrain[0]))

xdata = list(Xtrain[1])
ydata = list(Ytrain[0])
x, y = array( 'd' ), array( 'd' )


for i in range( n ):
   x.append( xdata[i] )
   y.append(ydata[i])


gr = ROOT.TGraph( 5, x, y )


gr.Draw();









