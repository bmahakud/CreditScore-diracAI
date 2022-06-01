import numpy as np






def LoadDataFromTxtFile(InputFile, nCol):
    X = np.zeros((nCol,1))
    Y = np.zeros((1,1))
    with open(InputFile) as file:
       for line in file:
          linedata=line.rstrip()
          linedataArr=linedata.split(" ");
          npArr = np.array([[1]])
          performance = None
          itr=0;
          for var in linedataArr:
              itr=itr+1
              if itr != nCol:
                  element = np.array([[var]])
                  npArr=np.append(npArr, element, axis=1)
              if itr == nCol:
                  element = np.array([[var]])
                  Y=np.append(Y, element, axis=1);
          X=np.append(X, npArr.T, axis=1)

    X = X[:,1:]
    Y = Y[:,1:]
    trainX = np.array(X,dtype=float)
    trainY = np.array(Y,dtype=float)

    return trainX,trainY;









