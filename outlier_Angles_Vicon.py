#In[]
import pandas as pd
import numpy as np
from statistics import mean
from statistics import median
from statistics import stdev
import os

pathWayVicon = "C:\\Users\\49176\\Desktop\\Python_Scripts\\Außreißer_Indentifizierung\\Auswertung Basti\\Vicon"

listPathwaysVicon = []
for entry in os.listdir(pathWayVicon):
    listPathwaysVicon.append(entry)

number = 0
numExc = listPathwaysVicon[number]

def runAllData(number,numExc):
    df = pd.read_csv("C:\\Users\\49176\\Desktop\\Python_Scripts\\Außreißer_Indentifizierung\\Auswertung Basti\\Vicon\\"+numExc)

    amount_of_Outliers = []
    angles = list(df.iloc[:,2])

    def func_outliers(x):
        # X Data
        meanDiffx = mean(x)
        medianDiffx = median(x)
        stdDiffx = stdev(x)
        borderUpx = medianDiffx + 1.5*stdDiffx
        borderDownx = medianDiffx - 1.5*stdDiffx

        angles_withOut = []

        for i in x:
            if i > borderUpx or i < borderDownx:
                amount_of_Outliers.append(i)
            else:
                angles_withOut.append(i)

        df_without_outliers = {"angle_withOut": angles_withOut}
        dataFrame_without_Outliers = pd.DataFrame(df_without_outliers)
        dataFrame_without_Outliers.to_csv("C:\\Users\\49176\\Desktop\\Python_Scripts\\Außreißer_Indentifizierung\\angles_withOut\\Vicon\\"+numExc)    
    func_outliers(angles)
    
runAllData(number, numExc)

for i in range(1,len(listPathwaysVicon),1):
    number = number + 1
    numExc  = listPathwaysVicon[number]
    runAllData(number, numExc)
# %%
