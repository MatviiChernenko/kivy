import pandas as pd

# Завантажуємо датафрейм 
df = pd.read_csv('GoogleApps.csv')

df.info()
#print(df.head())
print(df.tail())
#print(df[df["Rating"]>4.9]&(df["Type"]=="Free"["Installs"].mean())
print(df[(df["Rating"]>4.9)&(df["Type"]=="Free")]["Installs"].mean())
print(round(df['Installs'].median()))
print(df[(df["Rating"]>4.9)&(df["Type"]=="Free")]["App"].min())
# Як називається програма, розташована першим у наборі даних?
result = round(df["Content Rating"].value_counts()["Teen"]/df["Content Rating"].value_counts()["Everyone 10+"],3)
#s = (df["Category"] == ["COMICS"]["Size"].min())
#print(df[(df["Category"] == ["COMICS"])]["Size"].min())
print(df[df["Category"] == "COMICS"]["Size"].agg(["max","min"]))
#d = (df[(df["Type"]=="Free")&(df["Rating"].agg(["max","min"]]))
#b = (len(df[(df["Type"]=="Paid")&(df["Rating"] > 4.9)&(df["Category"] == "GAME")].value_counts()))
#print(d/b)
print(round(df.groupby(by = "Type")["Rating"].agg(["max","min","mean"])),2)
#print(s)
#print(result)
#a = round((df[(df["Type"]=="Paid")]["Rating"].mean()),3)
#b = round((df[(df["Type"]=="Free")]["Rating"].mean()),3)
#h = round((b/a),3)
#print(h)
# До якої категорії відноситься додаток, розташований останнім у наборі даних?


# Скільки стовпців міститься у наборі даних?
# Дані якого типу зберігаються у кожному зі стовпців?


# Вкажіть середнє арифметичне та медіану розміру додатків (Size)
# Скільки коштує найдорожчий додаток?
# *Вкажіть середнє арифметичне та медіану кількості установок програм (Installs)
