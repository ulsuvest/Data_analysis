#In[] Importieren der Bibliotheken 
import numpy as np
import pandas as pd
import math
from math import acos
from math import sqrt
import statistics
import matplotlib.pyplot as plt
from matplotlib import style
from VerbesserterCode import verbesserterCode 

#In[] Einlesen des Datensatzes von Vicon
df = pd.read_csv("Vicon.csv", sep=";", skiprows=1, encoding='latin1')
fig_Name = 1

# Globale Funktion: Längenberechnung der Richtungsvektoren a,b,c
def wholeCalculation(df, fig_Name):
    kneeTracker = (df.iloc[:,3], df.iloc[:,4], df.iloc[:,5])
    feetTracker = (df.iloc[:,6], df.iloc[:,7], df.iloc[:,8])
    hipTracker = (df.iloc[:,0], df.iloc[:,1], df.iloc[:,2])

    def funcDirectionVectors():
        xKT = kneeTracker[0]
        xFT = feetTracker[0]
        xHT = hipTracker[0]
        yKT = kneeTracker[1]
        yFT = feetTracker[1]
        yHT = hipTracker[1]
        zKT = kneeTracker[2]
        zFT = feetTracker[2]
        zHT = hipTracker[2]

        # Berechnung der Länge jedes einzelnen Vektors
        def funcVec_a():
            vector1 = list()
            for i in range(df.shape[0]):
                vecKneeToFeet = sqrt((xKT[i]-xFT[i])**2+(yKT[i]-yFT[i])**2+(zKT[i]-zFT[i])**2)
                vector1.append(vecKneeToFeet)
            return vector1
        vector_a = pd.DataFrame(funcVec_a())
        vector_a_Arr = vector_a.to_numpy()

        def funcVec_b():
            vector2 = list()
            for i in range(df.shape[0]):
                vecKneeToHip = sqrt((xKT[i]-xHT[i])**2+(yKT[i]-yHT[i])**2+(zKT[i]-zHT[i])**2)
                vector2.append(vecKneeToHip)
            return vector2
        vector_b = pd.DataFrame(funcVec_b())
        vector_b_Arr = vector_b.to_numpy()

        def funcVec_c():
            vector3 = list()
            for i in range(df.shape[0]):
                vecHipToFeet = sqrt((xFT[i]-xHT[i])**2+(yFT[i]-yHT[i])**2+(zFT[i]-zHT[i])**2)
                vector3.append(vecHipToFeet)
            return vector3
        vector_c = pd.DataFrame(funcVec_c())
        vector_c_Arr = vector_c.to_numpy()

        # Abspeichern der Richtungsvektoren a, b, c in einem Array
        directVectors_3D = (vector_a_Arr, vector_b_Arr, vector_c_Arr)
        return (directVectors_3D)   

    # Berechnung des Kniewinkels
    time_Vicon = df.iloc[:,9]
    directionVEcData = funcDirectionVectors()

    def angleCalc():
        a = directionVEcData[0]
        b = directionVEcData[1]
        c = directionVEcData[2]

        angles = list()
        for i in range (df.shape[0]):
            angle_trials = (acos((a[i]**2 + b[i]**2 - c[i]**2)/(2*a[i]*b[i])))
            angles.append(angle_trials)
        return angles

    result = pd.DataFrame(angleCalc())
    resultArr = result.to_numpy()

    # Umwandlung Bogenmaß in Degree 
    angleList = list()
    for i in resultArr:
        i = math.degrees((i))
        angleList.append(i)

    # Zeit- und Winkelveränderungen plotten
    colors = ("black","green","blue","red")
    style.use('ggplot')
    fig, ax = plt.subplots(figsize=(8,6))
    plt.plot(time_Vicon, angleList, linewidth=2, alpha=0.75, color=colors[fig_Name])
    ax.grid(True, color="k")
    plt.title('Angle Time Measurements Vicon System')
    plt.ylabel('Angle in °')
    plt.xlabel('Time in Frames')
    plt.ylim(50,150)
    plt.savefig('C:\\Users\\49176\\Desktop\\Winkelberechnungen\\Figures\\Angle_Velocity_Vicon' + str(fig_Name) + '.png', dpi=300, bbox_inches='tight')
    #plt.show()

    # Excel Tabelle schreiben
    col1 = "Time"
    col2= "Angles"
    angleList = pd.DataFrame(angleList)
    dataAngles = pd.DataFrame({col1:time_Vicon,col2:angleList[0]})
    dataAngles.to_csv('C:\\Users\\49176\\Desktop\\Winkelberechnungen\\Angles\\anglesVicon' + str(fig_Name) + '.csv')
    angleCalc()

wholeCalculation(df, fig_Name)

#In[] Neuen Vicon-Datansatz einlesen 
df = pd.read_csv("Vicon2.csv", sep=";", skiprows=1, encoding='latin1')
fig_Name += 1
wholeCalculation(df, fig_Name)

#In[] Neuen Unity_Datensatz einlesen und umwandeln
df_Unity_Feet = pd.read_csv("C:\\Users\\49176\Desktop\\Winkelberechnungen\\Unity_Data\\Fußtracker_Unity.csv", sep=";", decimal=",", skiprows=1, encoding='latin1')
df_Unity_Hip = pd.read_csv("C:\\Users\\49176\Desktop\\Winkelberechnungen\\Unity_Data\\Huefttracker_Unity.csv", sep=";", decimal=",", skiprows=1, encoding='latin1')
df_Unity_Knee = pd.read_csv("C:\\Users\\49176\Desktop\\Winkelberechnungen\\Unity_Data\\KnieTracker_Unity.csv", sep=";", decimal=",", skiprows=1, encoding='latin1')
fig_Name_VR = 1

def wholeCalculationVR(df_Unity_Feet,df_Unity_Hip,df_Unity_Knee, fig_Name_VR):
    
    time_Unity = df_Unity_Feet.iloc[:,0]

    kneeTracker_VR = (df_Unity_Knee.iloc[:,3], df_Unity_Knee.iloc[:,2], df_Unity_Knee.iloc[:,1]) # x, y, z
    feetTracker_VR = (df_Unity_Feet.iloc[:,3], df_Unity_Feet.iloc[:,2], df_Unity_Feet.iloc[:,1])
    hipTracker_VR = (df_Unity_Hip.iloc[:,3], df_Unity_Hip.iloc[:,2], df_Unity_Hip.iloc[:,1])

    xKT_VR = kneeTracker_VR[0]
    xFT_VR = feetTracker_VR[0]
    xHT_VR = hipTracker_VR[0]
    yKT_VR = kneeTracker_VR[1]
    yFT_VR = feetTracker_VR[1]
    yHT_VR = hipTracker_VR[1]
    zKT_VR = kneeTracker_VR[2]
    zFT_VR = feetTracker_VR[2]
    zHT_VR = hipTracker_VR[2]

    def funcVec_a():
        vector1 = list()
        for i in range(df_Unity_Feet.shape[0]):
            vecKneeToFeet = sqrt((xKT_VR[i]-xFT_VR[i])**2+(yKT_VR[i]-yFT_VR[i])**2+(zKT_VR[i]-zFT_VR[i])**2)
            vector1.append(vecKneeToFeet)
        return vector1
    vector_a = pd.DataFrame(funcVec_a())
    vector_a_Arr_VR = vector_a.to_numpy()

    def funcVec_b():
        vector2 = list()
        for i in range(df_Unity_Feet.shape[0]):
            vecKneeToHip = sqrt((xKT_VR[i]-xHT_VR[i])**2+(yKT_VR[i]-yHT_VR[i])**2+(zKT_VR[i]-zHT_VR[i])**2)
            vector2.append(vecKneeToHip)
        return vector2
    vector_b = pd.DataFrame(funcVec_b())
    vector_b_Arr_VR = vector_b.to_numpy()

    def funcVec_c():
        vector3 = list()
        for i in range(df_Unity_Feet.shape[0]):
            vecHipToFeet = sqrt((xFT_VR[i]-xHT_VR[i])**2+(yFT_VR[i]-yHT_VR[i])**2+(zFT_VR[i]-zHT_VR[i])**2)
            vector3.append(vecHipToFeet)
        return vector3
    vector_c = pd.DataFrame(funcVec_c())
    vector_c_Arr_VR = vector_c.to_numpy()

    directVectors_3D_VR = (vector_a_Arr_VR, vector_b_Arr_VR, vector_c_Arr_VR)

    a_VR = directVectors_3D_VR[0]
    b_VR = directVectors_3D_VR[1]
    c_VR = directVectors_3D_VR[2]
    anglesVR = list()
    for i in range (df_Unity_Feet.shape[0]):
        angle_trials = (acos((a_VR[i]**2 + b_VR[i]**2 - c_VR[i]**2)/(2*a_VR[i]*b_VR[i])))
        anglesVR.append(angle_trials)

    angleList_VR = list()
    for i in anglesVR:
        i = math.degrees((i))
        angleList_VR.append(i)

    colors = ("black","green","blue","red")
    style.use('ggplot')
    fig, ax = plt.subplots(figsize=(8,6))
    plt.plot(time_Unity, angleList_VR, linewidth=2, alpha=0.75, color=colors[fig_Name_VR])
    ax.grid(True, color="k")
    plt.title('Angle Time Measurements Unity')
    plt.ylabel('Angle in °')
    plt.xlabel('Time in Seconds')
    plt.ylim(50,150)
    plt.savefig('C:\\Users\\49176\\Desktop\\Winkelberechnungen\\Figures\\Angle_Velocity_Unity' + str(fig_Name_VR) + '.png', dpi=300, bbox_inches='tight')

    col1 = "Time"
    col2= "Angles"
    angleList_VR = pd.DataFrame(angleList_VR)
    dataAngles = pd.DataFrame({col1:time_Unity,col2:angleList_VR[0]})
    dataAngles.to_csv('C:\\Users\\49176\\Desktop\\Winkelberechnungen\\Angles\\anglesUnity' + str(fig_Name_VR) + '.csv')

wholeCalculationVR(df_Unity_Feet,df_Unity_Hip,df_Unity_Knee, fig_Name_VR)

df_Unity_Feet = pd.read_csv("C:\\Users\\49176\\Desktop\\Winkelberechnungen\\Unity_Data\\Unity_2\\Fuss 90 80 n 2.csv", sep=";", decimal=",", skiprows=1, encoding='latin1')
df_Unity_Hip = pd.read_csv("C:\\Users\\49176\\Desktop\\Winkelberechnungen\\Unity_Data\\Unity_2\\Huefte 90 80 n 2.csv", sep=";", decimal=",", skiprows=1, encoding='latin1')
df_Unity_Knee = pd.read_csv("C:\\Users\\49176\\Desktop\\Winkelberechnungen\\Unity_Data\\Unity_2\\Knie 90 80 n 2.csv", sep=";", decimal=",", skiprows=1, encoding='latin1')
fig_Name_VR += 1

wholeCalculationVR(df_Unity_Feet,df_Unity_Hip,df_Unity_Knee, fig_Name_VR)
#specialLine = df_Unity.iloc[:,1]
#specialLine_as_Arr = np.asarray(specialLine)
#editColumn = []
#for i in specialLine_as_Arr:
#    #if i > 1.5:
#       #continue
#    i = i.replace(',', '.')
#    editColumn.append(i)
#df1 = pd.DataFrame(data=editColumn)
#df1.to_csv("unityDataCorr.csv", sep=';', encoding='latin1', decimal='.')
# %%
