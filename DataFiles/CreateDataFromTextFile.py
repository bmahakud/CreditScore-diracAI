from DataLoader import LoadDataFromTxtFile
import ROOT
from array import array




ftrain = open("TrainData_v1.txt", "w")

nCol =4

trainingDataFile = "TrainData.txt"


Xtrain,Ytrain = LoadDataFromTxtFile(trainingDataFile, nCol)
print ("Xtrain.shape: ", Xtrain.shape)
print ("Xtrain: ", Xtrain)
print ("Ytrain.shape: ", Ytrain.shape)
print ("Ytrain: ", Ytrain)


xdata = list(Xtrain[1])
ydata = list(Ytrain[0])
itr=0
for a in xdata:
    itr=itr+1
    print (a)
    attendanceValue = a;
    performance = round(0.4 * attendanceValue,2)
    ftrain.write(str(attendanceValue)+" "+str(performance)+"\n");
    if itr==20:
        break
#print ("list Data xdata: ", xdata)
#print ("list Data ydaya: ", ydata)














