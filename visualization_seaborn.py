#In[]
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
#In[] Test Datensatz
df_csv = pd.read_csv("90Hz_80rpm_01.csv",delimiter =";",decimal=".", skiprows=4)
df_2 = pd.read_csv("90Hz_80rpm_02.csv",delimiter =";",decimal=".", skiprows=4)
data = pd.DataFrame(df_csv)
data2 = pd.DataFrame(df_2)
xs = data.iloc[:,2]
ys = data.iloc[:,3]
zs = data.iloc[:,4]
xs_2 = data2.iloc[:,2]

string_1 = []
for i in range(0,(int(len(ys)/2)),1):
    string_1.append("female")
    string_1.append("male")

string_2 = []
for i in range(0,(int(len(ys)/2)),1):
    string_2.append("Yes")
    string_2.append("No")

tips = sns.load_dataset("tips")
df = pd.DataFrame(tips)

spalte1 = [1,2,3,4,5]
spalte2 = [6,7,8,9,10]
x_data = np.array(xs)
y_data = np.array(ys)
x2_data = np.array(xs_2)
x2_data_new = x2_data[:-640]
dic1 = {"erste Spalte": x_data, "zweite Spalte": y_data, "dritte Spalte": string_1, "vierte Spalte": x2_data_new, "YesNo":string_2}
df_new = pd.DataFrame(dic1)

#In[]
fig1 = sns.distplot(df_new["erste Spalte"], bins=50)
df_new.to_csv("DataFrame.csv")
#In[] Joint Diagramme
sns.jointplot(x="erste Spalte", y="zweite Spalte",data=df_new,kind="scatter")
#In[] 
sns.jointplot(x="erste Spalte", y="zweite Spalte",data=df_new,kind="hex")
#In[] Regressionslinie
sns.jointplot(x="erste Spalte", y="zweite Spalte",data=df_new,kind="reg")
#In[] KDE
sns.jointplot(x="erste Spalte", y="zweite Spalte",data=df_new,kind="kde")
#In[] pair plot
sns.pairplot(df_new)
#In[] pair plot mit kategorischer Variable
sns.pairplot(df_new, hue='dritte Spalte')
#In[] Palette einführen
sns.pairplot(df_new, hue='dritte Spalte', palette='coolwarm')
#In[] Für jeden Punkt einen Strich
sns.rugplot(df_new["erste Spalte"])
#In[] Kerndichteschätzer Kde Gausschen (Normal-) Verteilung, Wahrscheinlichkeitsverteilung einer Zufallsvariable
dataset = np.random.randn(25)
sns.rugplot(dataset)
x_min = dataset.min() - 2
x_max = dataset.max() + 2
x_axis = np.linspace(x_min,x_max,100)
url = 'https://de.wikipedia.org/wiki/Kerndichtesch%C3%A4tzer#Satz_von_Nadaraya'
bandwidth = ((4*dataset.std()**5)/(3*len(dataset)))**.2
kernel_list = []

for data_point in dataset:
    kernel = stats.norm(data_point,bandwidth).pdf(x_axis)
    kernel_list.append(kernel)
    kernel = kernel / kernel.max()
    kernel = kernel * .4
    plt.plot(x_axis,kernel,color = 'grey',alpha=0.5)
plt.ylim(0,1)

sum_of_kde = np.sum(kernel_list,axis=0)
fig = plt.plot(x_axis,sum_of_kde,color='indianred')
sns.rugplot(dataset,c = 'indianred')
plt.yticks([])
plt.suptitle("Summe der Basisfunktionen")
plt.savefig("test.png")

#In[] Normalverteilung drüberlegen !!! WICHTIG !!!
sns.kdeplot(df_new["erste Spalte"])
sns.kdeplot(df_new["vierte Spalte"])
#In[] kdeplot inklusive rugplot
sns.kdeplot(df_new["erste Spalte"])
sns.rugplot(df_new["erste Spalte"])
#In[] Kategorische Daten 
sns.barplot(x="dritte Spalte", y="erste Spalte", data=df_new, estimator=np.std)
#In[] Count Plot Anzahl der kategorischen Variable
sns.countplot(x="dritte Spalte", data=df_new)
#In[] Boxplots
sns.boxplot(x="dritte Spalte", y="erste Spalte", data=df_new, palette="rainbow")
#In[]Ausrichtung der Boxplots = horizontal
sns.boxplot(data=df_new, palette="rainbow",orient="h")
#In[] Verfeinerung
sns.boxplot(x="dritte Spalte", y="erste Spalte", hue="YesNo", data=df_new, palette="coolwarm")
#In[] Violinplot Kde
sns.violinplot(x="dritte Spalte", y = "erste Spalte", data=df_new, palette="rainbow")
#In[] Verfeinerung des ViolinPlots !!! Wichtig !!!
sns.violinplot(x="dritte Spalte", y = "erste Spalte", data=df_new, hue="YesNo", split=True, palette="Set1", dodge=True) # Eigene Violine delete split
#In[] Strip Plots !!!WICHTIG!!!
sns.stripplot(x="erste Spalte", y="vierte Spalte",data=df_new, jitter=True, hue="dritte Spalte", palette="Set1", dodge=True) # Rote und blaue Farben
#In[] Swarmplot
sns.swarmplot(x="dritte Spalte", y="erste Spalte",data=df_new, hue="YesNo", palette="Set1",dodge=True)
#In[] Combination
sns.violinplot(x="zweite Spalte",y="dritte Spalte", data=df_new, palette="rainbow")
sns.swarmplot(x="zweite Spalte",y="dritte Spalte", data=df_new, color="black", size=3)
#In[] Factorplot
sns.factorplot(x="dritte Spalte", y="erste Spalte", data=df_new, kind="bar",estimator=np.std)
#In[] Tracker Datensatz
df_unity = pd.read_csv("C:\\Users\\49176\\Desktop\\Python_Scripts\\Minima_Maxima_Angles\\AuswertungTracker\\90Hz_80rpm_1_angle_maxValues_Unity.csv",delimiter =";",decimal=".")
df_vicon = pd.read_csv("C:\\Users\\49176\\Desktop\\Python_Scripts\\Minima_Maxima_Angles\\AuswertungTracker\\90Hz_80rpm_1_angle_maxValues_Vicon.csv",delimiter =";",decimal=".")

list_Unity = pd.Series(df_unity["value"])
string_unity = []
for i in range(0,(int(len(list_Unity))),1):
    string_unity.append("Unity")

comList = pd.Series(list(zip(list_Unity,string_unity)))
comListasDt = pd.DataFrame(comList)

list_Vicon = pd.Series(df_vicon["value"])
string_vicon = []
for i in range(0,(int(len(list_Vicon))),1):
    string_vicon.append("Vicon")

list_bothSystems = list_Unity.append(list_Vicon)
list_bothStrings = string_unity + string_vicon

df_gesamt = {"Unity":list_Unity, "Vicon":list_Vicon}
df_gesamt_2 = {"Max_Angles": list_bothSystems, "Systems":list_bothStrings}
dataframe_1 = pd.DataFrame(df_gesamt)
dataframe_2 = pd.DataFrame(df_gesamt_2)
#sns.jointplot(x="Unity", y="Vicon",data=dataframe_1, kind="hex")
#sns.jointplot(x="Unity", y="Vicon",data=dataframe_1,kind="kde")
#sns.jointplot(x="Unity", y="Vicon",data=dataframe_1,kind="scatter")
#sns.boxplot(x="Systems", y="Max_Angles", data=dataframe_2, palette="rainbow")
#sns.violinplot(x="Systems", y = "Max_Angles", data=dataframe_2, palette="rainbow")
#In[] Normalverteilung beider Systeme
sns.distplot(dataframe_1["Unity"], bins=50)
sns.distplot(dataframe_1["Vicon"], bins=50)
#In[] Barplot Vicon vs Unity
sns.barplot(x="Systems",y="Max_Angles",data=dataframe_2, estimator=np.std)
#In[] Countplot Unity Vicon Min und Max
sns.countplot(x="Systems", data=dataframe_2)
#In[] Boxplot Vicon Unity
sns.boxplot(x="Systems",y="Max_Angles",data=dataframe_2, palette="rainbow")
# Orientation
#sns.boxplot(data=dataframe_2, palette="rainbow", orient="h")'''
#In[] ViolinPlot
sns.violinplot(x="Systems",y ="Max_Angles", data=dataframe_2, palette="rainbow")
#In[] Strip Plots
sns.stripplot(x="Systems", y="Max_Angles",data=dataframe_2, jitter=True)
#In[] Swarmplot
sns.swarmplot(x="Systems", y="Max_Angles",data=dataframe_2, palette="Set1",dodge=True)
#In[] MATRIX Plots
# Korrelationen erkennen .corr()
sns.heatmap(df_new.corr())
#In[] Heatmap verschönern
sns.heatmap(tips.corr(), cmap="coolwarm", annot=True) # Annot Bezeichnung im Feld
#In[] !!!WICHTIG!!!
fluege = sns.load_dataset("flights")
pv_fluege = fluege.pivot_table(values="passengers",index="month",columns="year")
sns.heatmap(pv_fluege, cmap="magma", linecolor="white", linewidth=1)
#In[] Clustermaps
fluege = sns.load_dataset("flights")
pv_fluege = fluege.pivot_table(values="passengers",index="month",columns="year")
sns.clustermap(pv_fluege, cmap="coolwarm", standard_scale=1)
# %%
