#In[]
import pandas as pd
import numpy as np
from statistics import mean
from statistics import median
from statistics import stdev
import os

pathWayUnity = "C:\\Users\\49176\\Desktop\\Python_Scripts\\Außreißer_Indentifizierung\\Auswertung Basti\\Unity"

listPathwaysUnity = []
for entry in os.listdir(pathWayUnity):
    listPathwaysUnity.append(entry)

number = 0
numExc = listPathwaysUnity[number]

def runAllData(number,numExc):
    df = pd.read_csv("C:\\Users\\49176\\Desktop\\Python_Scripts\\Außreißer_Indentifizierung\\Auswertung Basti\\Unity\\"+numExc)

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
        dataFrame_without_Outliers.to_csv("C:\\Users\\49176\\Desktop\\Python_Scripts\\Außreißer_Indentifizierung\\angles_withOut\\Unity\\"+numExc)    
    func_outliers(angles)
    
runAllData(number, numExc)

for i in range(1,len(listPathwaysUnity),1):
    number = number + 1
    numExc  = listPathwaysUnity[number]
    runAllData(number, numExc)
# %%
