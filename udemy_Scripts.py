#In[] PLATZHALTER
pre_name = "Stefan"
last_name = "Pastel"

print('mein Vorname ist: {one}, und mein Nachname ist: {two}'.format(one=pre_name, two=last_name)) 
print('mein Vorname ist: {}, mein Nachname ist: {}'.format(pre_name, last_name))

#In[] Liste erstellen und Verschachtelung
meine_Liste = [1,2,3,4]
meine_Liste.append(pre_name) # add value to list
meine_Liste[-1] = "Neu" # replace the last

liste = [1,2,3,[4,5,6, ["Ziel"]]]
print(liste[3][3])
print(liste[3][3][0])
#In[] Dictionaries und Sets
d = {'key1': 'wert1', 'key2':123}
d_2 = {'k1':{'innerkey' : [1,2,3]}}
print(d_2['k1']['innerkey'][1])

# Sets enthält keine doppelte Zahlen !!!
s = {1,2,3,4,5,6,7,1,2,3,4,5,6,1,2,3,4,5}
s.add(100)

#In[] Konditioneller Code
x = 4
if x < 2:
    print("Hallo")
elif x == 3:
    print("Tschüss")
elif x > 3:
    print("ok")
else:
    print("Ciao")

# For Schleife
seq = [1,2,3,4,5]

for item in seq:
    print(item+item)

# While Schleife
i = 1
while i < 5:
    print("i ist : {}".format(i))
    i = i+1

#In[] Range Funktion
range(5)

autoList = list(range(6))
ergebnisList = []
for item in autoList:
    item *= 3
    ergebnisList.append(item)

c = [item**2 for item in autoList] # Beispiel für eine Lambda Funktion
#In[] Listenassoziation Lambda Funktion

erste_LamFun = lambda var: var*2
erste_LamFun(5)

seq1 = [1,2,3,4,5]
mapVa = list(map(erste_LamFun, seq1)) # Map wendet eine Funktion auf alle Items an
geradeZahlen = list(filter(lambda item: item%2==0, seq1)) # Nur gerade Zahlen herausfiltern 

#In[] Behandlung von Strings
st = 'hallo mein name ist sam'
st.upper()
st.lower()
st.split()
d_2.keys()
lst = [1,2,3]
# Erste Element einer Liste löschen 
first = lst.pop(0)
end = lst.pop()

# Einzelne Elemente einer Liste oder Tupels iterieren !!!
tupel_x = [(1,2),(3,4),(5,6)]
for x,y in tupel_x:
    print(x)
    print(y)

# In[] Aufgaben 
test_lst = [1,2,[3,4],[5,[100,200,['Hallo']],23,11],1,7]
print(test_lst[3][1][2][0])

#In[]
def website(email):
    return email.split("@")[1]

website("nutzer@webseite.de")

#In[]
def findeHund(string):
    return "hund" in string.lower().split()

findeHund("Gibt es einen Hund hier?")

#In[]
def anzahlHund(string):
    anzahl = 0
    for wort in string.lower().split():
        if wort == "hund":
            anzahl+=1
    return anzahl
anzahlHund("Gibt es einen Hund oder gibt es keinen Hund")

#In[]
testSeq = ["suppe", "hund", "salat"]
list(filter(lambda wort: wort[0]=='s', testSeq))

#In[]
def geschwindigkeitskontrolle(ges, geb):
    if geb: 
        messung = ges - 5
    else:
        messung = ges

    if messung > 120:
        return "Großer Strafzettel"
    elif messung > 100:
        return "kleiner Strafzettel"
    else:
        return "kein Strafzettel"

geschwindigkeitskontrolle(110, geb=True)

#In[] NUMPY Modul
import numpy as np
neue_Liste = [1,2,3]
np.array(neue_Liste)
matrix = [[1,2,3],[4,5,6]]
np.array(matrix)
np.arange(1,10)
np.arange(1, 11, 0.5)
np.zeros(4) # Eine bestimme Zahl häufig schreiben: np.zeros(10) + Zahl 
np.ones(4)
first_mat = np.zeros((5,5))
second_mat = np.ones((5,5))
gleichm_Intervalls = np.linspace(0, 10) # gleichmäßig verteilte Werte von bis (automatisch bis 50)
einheits_Matrix = np.eye(5)
zufallsVar = np.random.rand(50) # 50 Werte zwischen 0 und 1
zufallsMat = np.random.rand(5,5)
zufallsInt = np.random.randint(1,6,6) # Zufallszahlen 1-6, 6 Zufallszahlen
arr_1 = np.arange(25)
ran_arr = np.random.randint(0,50,10) # 10 mal eine Zahl zwsichen 0 und 50
# Matrizen aus Arrays erzeugen
arr_1_asMat = arr_1.reshape(5,5)
maxArr = arr_1.max()
minArr = arr_1.min()
pos_maxValue = arr_1.argmax() # Position des maximalen Wertes (Index)
pos_minValue = arr_1.argmin() # Position des minimalen Wertes (Index) --> Wird ersetzt durch idxmin 
# Eigenschaften eines Arrays
arr_1.shape
arr_1_asMat.shape
arr_1.dtype

#In[] NumPy Array Indexing
arr = np.arange(0,11)
arr[0:5] = 100
arr = np.arange(0,11)
teil_arr = arr[0:5]
teil_arr[:] = 99

# Array Kopie
arr_kopie = arr.copy()

arr_2d = np.array(([5,10,15], [20,25,30],[35,40,45]))
# arr_2d[0][0] ist das gleiche wie arr_2d[0,0]
arr_2d_letzte_Zeile = arr_2d[2]
arr_2d_letzte_Spalte = arr_2d[:,2]

# Alle Werte eines Arrays überprüfen auf Bedingung und einen neuen Array erstellen!!!
arr_new = np.arange(1,11)
bool_arr = arr_new > 5
# Neuen Array erstellen mit Boolean Array 
arr_bool = arr_new[bool_arr]

arr_Test = np.arange(50).reshape(5,10)

#In[] Array Operationen
import numpy as np
from numpy import std
arr_oper = np.arange(0,10)

arr_op_add = arr_oper + arr_oper
arr_op_multi = arr_oper * arr_oper
arr_op_sub = arr_oper - arr_oper
arr_op_div = arr_oper / arr_oper
# 1 Wert/Variable durch einen ganzen Array/Liste 
arr_num_arr = 1 / arr_oper
new_arr_exp = arr_oper**3
# mathematische Operationen
square_Arr = np.sqrt(arr_oper)
exp_Arr = np.exp(arr_oper)
max_Arr = np.max(arr_oper) # Oder arr_oper.max()
sinus_Funk = np.sin(arr_oper)
log_Funk = np.log(arr_oper)

# Summe und Standardabweichungen aller Spalten !WICHTIG!
dataSet_Arr = [[1,6,7],[9,7,6],[10,20,9]]
dataSetAsArray = np.asarray(dataSet_Arr)
dataSet_as_Mat = dataSetAsArray.reshape(3,3)

dataSetSumColumns = [sum(dataSet_as_Mat[:,0]), sum(dataSet_as_Mat[:,1]), sum(dataSet_as_Mat[:,2])]
dataSetMeanCol = dataSet_as_Mat.mean(axis=0)
dataSetStdColumns = dataSet_as_Mat.std(axis=0) # Spaltenweise (0) die Standardabweichung berechnen, für Zeilenweise = 1
stdFirstColumn = std(dataSet_as_Mat[:,1])
# %%

#In[] PANDAS Modul
import numpy as np
import pandas as pd

labels = ["a", "b", "c"]
liste = [10,20,30]
arr = np.array(liste)
d = {"a":10, "b":20, "c":30}

# Series erstellen aus einem Array, Dictionaries 
pd.Series(data=liste)
pd.Series(data=liste, index=labels) # Oder pd.Series(liste,labels)
pd.Series(arr,labels)
pd.Series(d)
# Liste mit Funktionen
pd.Series([sum,print,len])
# Inex Nutzung
ser1 = pd.Series([1,2,3,4], index=["USA", "Germany", "Russland", "Japan"])
ser2 = pd.Series([5,6,7,8], index= ["USA", "Germany", "Italien", "Japan"])

serMix = ser1 + ser2

# Eigenständig DataFrame erzeugen: 
from numpy.random import randn
np.random.seed(101)
df = pd.DataFrame(randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
# Einzelne Spalten auslesen : df["W"]
# Mehrere Spalten in eine Liste ausgeben: df[["W","Z"]]
new_List = df[["W","Z"]]

# Neue Spalte hinzufügen
df["neu"] = df["W"] + df["Y"]

# Spalte und Zeile löschen
df.drop("neu",axis=1) # Reihe gleich 0, Spalte = 1, Spalte dauerhaft entfernen = df.drop("neu",axis=1, inplace=True)
df.drop("E",axis=0) # Zeilen/Reihen löschen, dauerhaft erneut inplace=True hinzufügen

# Zeilen ausgeben 
df.loc['A']
df.iloc[0]
# Reihen und Spalten zugleich ausgeben
df.loc['B','Y'] # Erste die Reihe, dann die Spalten

# Ganze DataFrames aus bisherigen Daten (Reihen und Spalten) erstellen
df_neu = df.loc[["A","B","C"],["Y","Z","W"]]

# Bedingungen im DataFrame
df_Bedin = df[df>0]
df_Bedin_Spalte = df[df["W"]>0] # Splate C wurde gelöscht, da diese Werte unter 0 enthielt

# mehrere Bedingungen über die Spalten, Listen von Booleans, in Pandas wird das & verwendet, damit DataFrames verglichen werden können
df_multi = df[(df['W']>0) & (df['Y']>1)]
df_multi_oder = df[(df['W']>0) | (df['Y']>1)]

# Standardindex zurücksetzen oder neu definieren 
new_Df = df.copy()
new_Df.reset_index()
neuind = 'BY NRW HH BB RP'.split()
new_Df["Staaten"] = neuind
new_Df.set_index("Staaten",inplace=True) # Den Datensatz überschreiben und Veränderungen speichern

# Multiindexierung
aussen = ["G1","G1","G1","G2","G2","G2"]
innen = [1,2,3,1,2,3]
hier_index = list(zip(aussen,innen)) # Zip verbindet zwei Listen
hier_index = pd.MultiIndex.from_tuples(hier_index) # Multiindex fügt die Elemente beider Listen in einen Index
art_df = pd.DataFrame(np.random.randn(6,2), index = hier_index, columns= ["A","B"])
print(art_df.loc["G1"].loc[2])
art_df.index.names = ["Gruppe", "Num"]

# Reihen und Spalten zurückgreifen mit der Crosssectio  Funktion
print(art_df.xs(["G1", 1]))
print(art_df.xs(1,level="Num"))
# %%
#In[] Eliminierungsverfahren
import numpy as np
import pandas as pd

df = pd.DataFrame({'A':[1,2,np.nan], 'B':[5, np.nan, np.nan], 'C':[1,2,3]})
# df.dropna() Werte, die Null sind, herauslöschen
df.dropna(axis=1) # Spalten heraussuchen, welche vollständige Datenenthält...Zeilen axis = 0
df.dropna(axis=0, thresh = 2) # Threshold: Wenn mehr als 2 NaN auftauchen, nicht mehr berücksichtigen
df.fillna(value='Füllwert') # leere Daten mit Wert füllen z.Bsp. 0

# Wert aus der Spalte A durch den Mean der anderen ersetzen
df_new = df['A'].fillna(value=df['A'].mean())
# %%

#In[] GroupBY WICHTIG!
import pandas as pd

data = {"Firma":['Adidas','Adidas','Nike','Nike','Puma','Puma'],
'Person':['Emir','Charline','Yana','Vanessa','Carl','Sarah'],
'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
# In Gruppen einteilen und gleichzeitig mean, oder Summe etc ausgeben lassen
mittelwert_Firma = df.groupby('Firma').mean()
summe_Firma = df.groupby('Firma').sum()
# Nach Firmen gegliedert die deskriptive Statistik anzeigen lassen
nach_firma = df.groupby('Firma')
nach_firma.mean()
nach_firma.std()
nach_firma.min() # Für jede Spalte das Minimum, vertauschen der Werte
nach_firma.max() # "
nach_firma.count()
print(nach_firma.describe())

# Durch die Describe Funktion ein neues DataFrame anlegen WICHTIG!!!
df_describe = pd.DataFrame(nach_firma.describe())
df_describe_Transpose = pd.DataFrame(nach_firma.describe().transpose())
df_describe_Transpose.to_csv("C:\\Users\\49176\\Desktop\\Python Udemy Academy\\data.csv")

# Nach nur einer Firma suchen: nach_firma.describe().transpose()['Adidas']

# Automatisch Listen erzeugen für DataFrame 
new_List = []
for i in range(1,4,1):
    new_List.append("Mercedes")
for i in range(1,4,1):
    new_List.append("BMW")

#In[] Merging, Joining Merging
import pandas as pd
import numpy as np

#Bsp 1
df_1 = pd.DataFrame({'A':['A0','A1','A2','A3'],
'B':['B0','B1','B2','B3'],
'C':['C0','C1','C2','C3'],
'D':['D0','D1','D2','D3']},
index = [0,1,2,3])

df_2 = pd.DataFrame({'A':['A4','A5','A6','A7'],
'B':['B4','B5','B6','B7'],
'C':['C4','C5','C6','C7'],
'D':['D4','D5','D6','D7']},
index=[4,5,6,7])

df_3 = pd.DataFrame({'A':['A8','A9','A10','A11'],
'B':['B8','B9','B10','B11'],
'C':['C8','C9','C10','C11'],
'D':['D8','D9','D10','D11']},
index=[8,9,10,11])

df_zusammengefuegt_X = pd.concat([df_1,df_2,df_3]) # Zusammenfügen (X-Achse) der DataFrames nur möglich, wenn die Keys übereinstimmen
df_zusammengefuegt_Y = pd.concat([df_1, df_2, df_3],axis=1)

#Bsp2
links = pd.DataFrame({'key': ['K0','K1','K2','K3'],
'A':['A0','A1','A2','A3'],
'B':['B0','B1','B2','B3']})

rechts = pd.DataFrame({'key': ['K0','K1','K2','K3'],
'C':['C0','C1','C2','C3'],
'D':['D0','D1','D2','D3']})

df_merged = pd.merge(links,rechts,how='inner',on='key')

#Bsp3
links_2 = pd.DataFrame({'key1':['K0','K0','K1','K2'],
'key2':['K0','K1','K0','K1'],
'A':['A0','A1','A2','A3'],
'B':['B0','B1','B2','B3']})

rechts_2 = pd.DataFrame({'key1':['K0','K1','K1','K2'],
'key2':['K0','K0','K0','K0'],
'C':['C0','C1','C2','C3'],
'D':['D0','D1','D2','D3']})

df_merged_2 = pd.merge(links_2,rechts_2, how='outer',on=['key1','key2'])
df_merged_rechts_DF = pd.merge(links_2,rechts_2, how='right',on=['key1','key2'])

#Bsp4
links_3 = pd.DataFrame({'A':['A0','A1','A2'],
'B':['B0','B1','B2']},
index=['K0','K1','K2'])

rechts_3 = pd.DataFrame({'C':['C0','C1','C2'],
'D':['D0','D1','D2']},
index=['K0','K2','K3'])

df_join = links_3.join(rechts_3)
df_join_outer = links_3.join(rechts_3, how = 'outer')

#In[] Operations
import pandas as pd
import numpy as np

df = pd.DataFrame({'spa1':[1,2,3,4],
'spa2':[444,555,666,444],
'spa3':['abc','def','ghi','xyz']})

# df.head() oberste Zeilen
# df['spa2'].unique() Einzigartige Werte innerhalb der zweiten Spalte
# df.['spa2'].nunique() Anzahl der einzigartigen Werte
# df.['spa2].value_counts() Werte der Spalte und deren Anzahl

newdf = df[(df['spa1']>2)] # neuen Datensatz, alle Werte in Spalte 1, die größer als 2 sind
newdf_2 = df[(df['spa1']>2) & (df['spa2']==444)]

# Funktion über einen Datensatz laufen lassen !!!WICHTIG!!!
def mal2(x):
    return x*2

df['spa1'].apply(mal2) # Werte innerhalb der Spalte verdoppeln
df['spa3'].apply(len) # Länge der Inhale der Spalten
df['spa2'].apply(lambda x: x*2) # Lambda Funktion Werte in einer Spalte verdoppeln
df['spa1'].sum() # Sum
df['spa1'].min() # Min
df.drop('spa1',axis=1) # Spalte löschen...falls dauerthaft= ,inplace = True oder del df['spa1']
df.columns # Spalten angeben
df.index # Index ausgeben 
df.sort_values(by='spa2') # Werte innerhalb einer Spalte sortieren, Index bleibt gleich, auch hier: inplace=True
df.isnull() # Nullwerte anzeigen nach Spalten
df.dropna() # Zeilen mit Nullwerte 
# Nullvalues mit anderen Werten fühen
df_Nullwerte = pd.DataFrame({'spa1':[1,2,3,np.nan],'spa2':[np.nan,555,666,444]
,'spa3':['abc','def','ghi','xyz']})
df_Nullwerte.fillna(0) # Alle Werte, welche NaN sind, mit einer 0 füllen

#In[] Pivotieren
import pandas as pd
import numpy as np

data = {'A':['foo','foo','foo','bar','bar','bar'],
'B': ['one','one','two','two','one','one'],
'C': ['x','y','x','y','x','y'],
'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
df.pivot_table(values='D', index=['A','B'],columns=['C']) # Bsp pivotierte Tabelle 

'''
Übungen: die Berufsbezeichnung eines ganz bestimmten Mitarbeiters in einer Liste 
data[data['Name']=='Stefan Pastel']['Job']

Nur die Zeilen ausgeben lasse, die gewisse Bedingungen erfüllen
data[data['Einkommen']==data['maxEinkommen'].max()]

Werte in einem bestimmten Bereich (Jahr)
data.groupby('Year').mean()
data.groupby('Year).mean()['Grundlohn']

Einzigartige Jobbezeichnungen
data['Jobtitle'].unique() oder die Anzahl data['Jobtitle].nunique()

Die 5 höchsten Werte:
data['JobTitle'].value_counts().head(5)

Die Summe aller Personen die nur eine Berufsbezeichnung hatten
sum(data[data['Year']==2013 [Jobtitle].value_counts()==1])

Funktion anwenden über eine Spalte !!!Wichtig!!!

    def chief_string(title):
        if 'chief' in title.lower().split():
            return True
        else:
            return False

    chief_string("Deputy Chief")

    sum(data['Jobtitle'].apply(lambda x: chief_string(x)))

Neue Spalte anlegen und gleichzeitig berechnen
data['mean'] = data['Winkel'].apply(mean)
data[['Name','mean']],corr() # Korrelationen berechnen
'''