#In[]
import numpy as np
import pandas as pd
import seaborn as sns

df_Unity = pd.read_csv("Unity.csv",delimiter =",",decimal=".")
df_Vicon = pd.read_csv("Vicon.csv",delimiter =",",decimal=".")

angles_unity = df_Unity.iloc[:,2]
angles_vicon = df_Vicon.iloc[:,2]

arr_Ang_Unity = list(angles_unity)
arr_Ang_Vicon = list(angles_vicon)
arr_comb = arr_Ang_Unity + arr_Ang_Vicon

list_measurement_System = []
for i in range(0,int(len(angles_unity)),1):
    list_measurement_System.append("Unity")
for i in range(0,int(len(angles_vicon)),1):
    list_measurement_System.append("Vicon")

dataSet = {"Angles": arr_comb, "Unity_Vicon":list_measurement_System}
dataSet_df = pd.DataFrame(dataSet)
dataSet_df.to_csv("DataSet_Groupby.csv")

sr1 = pd.Series(angles_unity)
sr2 = pd.Series(angles_vicon)

df_new = {"unity":sr1,"vicon":sr2}
df_new_df = pd.DataFrame(df_new)

#In[] Pairplots 
sns.pairplot(dataSet_df, hue='Unity_Vicon')

#fig1 = sns.distplot(df_Unity["Angles"], bins=50)
#fig2 = sns.distplot(df_Vicon["Angles"], bins=50)
#
#In[]
sns.jointplot(x="unity", y="vicon",data=df_new_df,kind="scatter")
#In[]
sns.jointplot(x="unity", y="vicon",data=df_new_df,kind="hex")
#In[]
sns.jointplot(x="unity", y="vicon",data=df_new_df,kind="reg")
#In[]
sns.jointplot(x="unity", y="vicon",data=df_new_df,kind="kde")
# %%
