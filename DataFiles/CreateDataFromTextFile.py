from DataLoader import LoadDataFromTxtFile
import ROOT
from array import array
import sys 

numExamples=sys.argv[1] 

print ("trainin:;;;;;;;;;",numExamples)


ftrain = open("TrainData_v1.txt", "w")
ftrain2 = open("TrainData_v1.csv", "w")


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
ftrain2.write("Attendance,Performance\n")
for a in xdata:
    itr=itr+1
    print (a)
    attendanceValue =  a;
    performance = round(0.4 * attendanceValue,2)
    ftrain.write(str(attendanceValue)+" "+str(performance)+"\n");
    ftrain2.write(str(attendanceValue)+","+str(performance)+"\n");

    if itr==int(numExamples):
        break
#print ("list Data xdata: ", xdata)
#print ("list Data ydaya: ", ydata)














