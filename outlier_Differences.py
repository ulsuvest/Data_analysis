#In[]
import pandas as pd
import numpy as np
from statistics import mean
from statistics import median
from statistics import stdev
import os

pathWay = "C:\\Users\\49176\\Desktop\\Python_Scripts\\Außreißer_Indentifizierung\\Auswertung Basti\\Differences"

listPathways = []
for entry in os.listdir(pathWay):
    listPathways.append(entry)

number = 0
numExc = listPathways[number]

def runAllData(number,numExc):
    df = pd.read_csv("C:\\Users\\49176\\Desktop\\Python_Scripts\\Außreißer_Indentifizierung\\Auswertung Basti\\Differences\\"+numExc)

    amount_of_Outliers = []
    deltaValue = list(df.iloc[:,1])
    deltaPercentage = list(df.iloc[:,2])
    deltaTime = list(df.iloc[:,3])

    def func_outliers(x,y,z):
        # X Data
        meanDiffx = mean(x)
        medianDiffx = median(x)
        stdDiffx = stdev(x)
        borderUpx = medianDiffx + stdDiffx
        borderDownx = medianDiffx - stdDiffx
        # Y Data
        meanDiffy = mean(y)
        stdDiffy = stdev(y)
        borderUpy = meanDiffy + stdDiffy
        borderDowny = meanDiffy - stdDiffy
        # Z Data
        meanDiffz = mean(z)
        stdDiffz = stdev(z)
        borderUpz = meanDiffz + stdDiffz
        borderDownz = meanDiffz - stdDiffz

        deltaValue_withOut = []
        deltaPercentage_withOut = []
        deltaTime_withOut = []

        for i in x:
            if i > borderUpx or i < borderDownx:
                amount_of_Outliers.append(i)
            else:
                deltaValue_withOut.append(i)

        for j in y:
            if j <= borderUpy or j >= borderDowny:
                deltaPercentage_withOut.append(j)
            else:
                continue

        for k in z:
            if k <= borderUpz or k >= borderDownz:
                deltaTime_withOut.append(k)
            else:
                continue
        
        df_without_outliers = {"deltaValue_withOut": deltaValue_withOut}
        dataFrame_without_Outliers = pd.DataFrame(df_without_outliers)
        dataFrame_without_Outliers.to_csv("C:\\Users\\49176\\Desktop\\Python_Scripts\\Außreißer_Indentifizierung\\Differences_withOut\\"+numExc)
    func_outliers(deltaValue,deltaPercentage,deltaTime)
    
runAllData(number, numExc)

for i in range(1,len(listPathways),1):
    number = number + 1
    numExc  = listPathways[number]
    runAllData(number, numExc)
# %%
