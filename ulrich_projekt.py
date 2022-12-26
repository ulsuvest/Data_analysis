eingabeZahl = int(input("Bitte Geben Sie eine Zahl ein: "))
zahl = eingabeZahl+1
if eingabeZahl+1 == zahl:
    list_1 = [*range(1,zahl,1)]
    print(list_1)
else:
    print("Hallo Ulrich")

list_2 = []
for i in list_1:
    i = i*45
    list_2.append(i)

print(list_2)
