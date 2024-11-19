import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import streamlit as st
linreg = LinearRegression()

def getData():
  df = pd.read_csv("data/stadat-jov0001-14.1.1.1-hu.csv",sep=';',encoding='ansi',header=1)
  return df


dataFrame = getData()

yPS = dataFrame.iloc[0,1:].str.replace(' ','').map(int)
xPS = dataFrame.set_index('Megnevezés').columns

yArray = yPS.values.reshape(-1, 1)
xArray = xPS.map(int).values.reshape(-1, 1)

#x_train,x_test,y_train,y_test = train_test_split(xArray,yArray,test_size=0.2,random_state=0)
linreg.fit(xArray,yArray)
linreg.predict(xArray)


#Visu
fig, ax = plt.subplots()
#plot def data
plt.title("A háztartások egy főre jutó éves nettó jövedelme")
plt.ylabel("mFt / év")
ax.plot(xArray,yArray,"bo")

#plot linreg
ax.plot(xArray,linreg.predict(xArray),"o:r")

futureXArr = [[2023],[2024],[2025],[2026]]
ax.plot(futureXArr,linreg.predict(futureXArr),"o:g")

#Regression Error score
r2 = r2_score(yArray,linreg.predict(xArray))
print("Linear regression error score:" + str(r2))

#plt.show()

dataFrame = dataFrame.set_index(dataFrame.columns[0]).T.rename_axis("Év").rename_axis("",axis="columns").reset_index()
with st.expander("Adatok"):
  st.dataframe(dataFrame)

#st.write(type(dataFrame))
#dataFrame.sort_values("A háztartások egy főre jutó éves nettó jövedelme, forint", ascending=True)
st.line_chart(dataFrame,x="Év",y="A háztartások egy főre jutó éves nettó jövedelme, forint")
st.write(fig)
#st.line_chart(dataFrame,x="Év",y="A háztartások egy főre jutó éves nettó jövedelme, forint")
#st.write(dataFrame)
