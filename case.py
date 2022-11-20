import pandas as pd
import matplotlib.pyplot as plt

 
df = pd.read_csv('IMDB-Movie-Data.csv')
df.info()
#узнать в каком году было сделано больше всего фильмов
y06 = 0
y07 = 0
y08 = 0
y09 = 0
y10 = 0
y11 = 0
y12 = 0
y13 = 0
y14 = 0
y15 = 0
y16 = 0

def year_counter(row):
    global y06, y07, y08, y09, y10, y11, y12, y13, y14, y15, y16
    if row['Year'] == 2006 and row['Metascore'] > 70:
        y06+= 1
    if row['Year'] == 2007 and row['Metascore'] > 70:
        y07+= 1
    if row['Year'] == 2008 and row['Metascore'] > 70:
        y08+= 1
    if row['Year'] == 2009 and row['Metascore'] > 70:
        y09+= 1
    if row['Year'] == 2010 and row['Metascore'] > 70:
        y10+= 1
    if row['Year'] == 2011 and row['Metascore'] > 70:
        y11+= 1
    if row['Year'] == 2012 and row['Metascore'] > 70:
        y12+= 1
    if row['Year'] == 2013 and row['Metascore'] > 70:
        y13+= 1
    if row['Year'] == 2014 and row['Metascore'] > 70:
        y14+= 1
    if row['Year'] == 2015 and row['Metascore'] > 70:
        y15+= 1
    if row['Year'] == 2016 and row['Metascore'] > 70:
        y16+= 1
    return False
df.apply(year_counter, axis = 1)
print(y06, y07, y08, y09, y10, y11, y12, y13, y14, y15, y16)
s = pd.Series(data=[y06, y07, y08, y09, y10, y11, y12, y13, y14, y15, y16],
index = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016'])

s.plot(kind='barh')
plt.show()

print('Больше всего высокрейтинговых фильмов было в 2016', y16, 'а меньше в 2008', y08)


        