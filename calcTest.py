import sys



attendance = float(sys.argv[1])
alertness = float(sys.argv[2])
homework = float(sys.argv[3])

theta0 = float(sys.argv[4])
theta1 = float(sys.argv[5])
theta2 = float(sys.argv[6])
theta3 = float(sys.argv[7])


pvalue = theta0+(theta1*attendance)+(theta2*alertness)+(theta3*homework)


print ("Performance: ", pvalue)
