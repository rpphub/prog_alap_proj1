import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import streamlit as st
import helper

linreg = LinearRegression()
dataFrame = helper.get_dfFromCsv("data/stadat-jov0001-14.1.1.1-hu.csv")
dataFrame = helper.dfManipulation(dataFrame) #Tábla forgatás, manupulálás.

yArray = dataFrame.iloc[:,1].str.replace(' ','').map(int).values.reshape(-1, 1)
xArray = dataFrame.iloc[:,0].map(int).values.reshape(-1, 1) #xPS.map(int).values.reshape(-1, 1)


#x_train,x_test,y_train,y_test = train_test_split(xArray,yArray,test_size=0.2,random_state=0)
linreg.fit(xArray,yArray)

# Streamlit View
# Title
st.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<h1 class="title">Programozás alapok beadandó feladat.</h1>', unsafe_allow_html=True)

# Slider
regVal = st.slider("Év kiválasztása", 2015, 2050, 2024)
futureXArr = helper.get_futureList(regVal,2023)

# Year / Income calculated value
col1,col2 = st.columns(2)
with col1:
  st.metric(
    label="Év:",
    value=regVal
  )
with col2:
  st.metric(
    label="Jövedelem:",
    value=linreg.predict([[int(regVal)]])
  )

# Plot
fig, ax = plt.subplots()
plt.title("A háztartások egy főre jutó éves nettó jövedelme")
plt.ylabel("mFt / év")
plt.xlabel("Év")
ax.yaxis.set_major_formatter(mpl.ticker.EngFormatter()) #Ez segít Y tengely milliós érték megjelenítésben
plt.grid(linestyle = '--') #Háttér vonalazás
ax.plot(xArray,yArray,"o",color="orange", label = "Tényleges") #Eredeti adatok

ax.plot(xArray,linreg.predict(xArray),"o:",color="magenta",label = "Lineáris regresszió") #Eredeti X tengely adatok mentén Linreg
ax.plot(futureXArr,linreg.predict(futureXArr),"o:", color = "darkturquoise", label = "Prediktív") #Változtatható X tengely adat menti Linreg
ax.legend(shadow=True,fontsize = "x-small") #Diagram nevek mérete

fig.set_figwidth(8) #Grafikon szélesség
st.write(fig) #Grafikon streamlit-ba ágyazása

# Data matrix
with st.expander("Tényleges Adatok"):
  st.dataframe(dataFrame)

# Regression Error score
r2 = r2_score(yArray,linreg.predict(xArray))
print("Linear regression error score:" + str(r2))

if __name__ == "__main__":
  print("Teszt")