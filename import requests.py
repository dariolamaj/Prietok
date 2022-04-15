import requests
import pandas as pd
import matplotlib.pyplot as plt


url = "https://www.noe.gv.at/wasserstand/kidata/stationdata/207407_DurchflussPrognose_48Stunden.csv"
response = requests.get(url=url)

with open("Data.csv", "wb") as f:
    
   f.write(response.content)

df = pd.read_csv('Data.csv', sep = ';',skiprows=9)
x = list(df['Datum'])
y = list(df['Mittel'])

plt.figure(figsize=(10,10))
plt.plot(x,y)
plt.xlabel("Datum")
plt.ylabel("Priemer")
plt.title("Priemerný prietok")
ax = plt.gca()
ax.axes.xaxis.set_ticklabels([])
plt.show()
