import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# 1 ile 9 arasinda 30 adet random sayi
m = np.random.randint(1,9,30)
print(m)
print("\n")

df = pd.DataFrame(m)
df = pd.DataFrame(df[0].value_counts())
print(df)
print("\n")

#kac adet sayi oldugunun saglamasi
length = len(m)
print(length)
print("\n")

#hangi sayidan kac tane oldugu
data = pd.DataFrame(df[0])
print(data)
print("\n")

data.columns = ["Counts"]
print(data)

#her bir sayinin gelme olasiligi
data["Probs"] = data["Counts"]/length
print(data)

#grafik
graphic = sns.barplot(data["Counts"],data["Probs"])

plt.show()
