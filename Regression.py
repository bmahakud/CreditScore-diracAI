import numpy as np
import matplotlib.pyplot as plt
import h5py
import scipy
from PIL import Image
from scipy import ndimage
#%matplotlib inline
#import ROOT


#hCost = ROOT.TH1F("hCost", "hCost", 30, 0, 30);



import ROOT


hCost = ROOT.TH1F("hCost", "hCost", 500, 0, 500)


hWeights = ROOT.TH1F("hWeights","hWeights",4,0,4)


#X = np.array()


X = np.zeros((4,1))
Y = np.zeros((1,1))
with open('TrainData.txt') as file:
    for line in file:
        linedata=line.rstrip()
        linedataArr=linedata.split(" "); 
        print ("linedata: ", linedataArr)
        attendance = linedataArr[0]
        alertness = linedataArr[1]
        homework = linedataArr[2]
        performance = linedataArr[3]
        print ("--atte---alert--home:  ",attendance, alertness, homework, performance)      
        arr = np.array([[1, attendance, alertness, homework]]).T
        X=np.append(X, arr, axis=1)
        yarr=np.array([[performance]]).T
        Y=np.append(Y, yarr, axis=1)

X=X[:,1:]
Y=Y[:,1:]

Theta = np.random.rand(4,1)

print ("X.shape : ", X.shape);

print ("Theta.shape: ",Theta.shape)

print ("Y.shape: ", Y.shape)


trainX=np.array(X,dtype=float)
Theta=np.array(Theta,dtype=float)
trainY=np.array(Y,dtype=float)


hx = np.dot(Theta.T,trainX);

print ("hx.shape: ", hx.shape)

print ("hx: ", hx)

print ("trainY: ", trainY)

#diff = (hx - trainY)


#print ('diff.shape: ',diff)


#cost = (1./2000)*diff*diff

#print ("cost.shape: ", cost.shape)


#print ("cost: ", np.sum(cost))


alpha=0.01;

#print ("X shape: ",X.shape)
#print ("diff.T shape", diff.T.shape)





for iteration in range(1,500):
    hx = np.dot(Theta.T,trainX);
    diff = (hx - trainY)
    Theta = Theta - (alpha/2000) * (np.dot(trainX , diff.T)) 
    cost = (1./4000)*diff*diff
    avgCost = np.sum(cost)
    #print ("cost: ", avgCost)
    hCost.SetBinContent(iteration,avgCost);




#hWeights


hCost.Draw();



print ("Theta: ", Theta)



teX = np.zeros((4,1))
teY = np.zeros((1,1))
with open('TestData.txt') as file:
    for line in file:
        linedata=line.rstrip()
        linedataArr=linedata.split(" ");
        attendance = linedataArr[0]
        alertness = linedataArr[1]
        homework = linedataArr[2]
        performance = linedataArr[3]
        print ("TestData: --atte---alert--home:  ",attendance, alertness, homework, performance)      
        arr = np.array([[1, attendance, alertness, homework]]).T
        teX=np.append(teX, arr, axis=1)
        yarr=np.array([[performance]]).T
        teY=np.append(teY, yarr, axis=1)


testX=np.array(teX,dtype=float)
testY=np.array(teY,dtype=float)

testX=testX[:,1:]
testY=testY[:,1:]



print ('Theta.T.shape', Theta.T.shape)
print ('testX.shape: ',testX.shape)
print ('testY.shape: ',testY.shape)


hXTest = np.dot(Theta.T,testX);
hXTrain = np.dot(Theta.T,trainX);

diffTest = (hXTest - testY)
diffTrain = (hXTrain - trainY)

costTest = (1./2000)*diffTest*diffTest;
costTrain = (1./4000)*diffTrain*diffTrain;


avgCostTest = np.sum(costTest)
avgCostTrain = np.sum(costTrain)

print ("Theta.T: ", Theta.T)

print ("cost Test: ", avgCostTest)
print ("cost Train: ", avgCostTrain)





