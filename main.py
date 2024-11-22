import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from view.diagram import Diagram
from data.data import Data

df = Data.get_df_from_csv("data/stadat-jov0001-14.1.1.1-hu.csv")
df = Data.data_manipulation(df) #Tábla forgatás, manupulálás.

# dataFrame - > ndarray, így könnyebben emésztik a függvények
yArray = df.iloc[:,1].str.replace(' ','').map(int).values.reshape(-1, 1)
xArray = df.iloc[:,0].map(int).values.reshape(-1, 1)

linreg = LinearRegression()
linreg.fit(xArray,yArray)

r2 = r2_score(yArray,linreg.predict(xArray)) # Regression Error score, ez csak úgy érdekességnek van
print("Lineáris regresszió pontossága:" + str(r2))

# Streamlit View
# Title
st.markdown("<h1 style='text-align: center;'>Programozás alapok beadandó feladat</h1>", unsafe_allow_html=True)
st.markdown("***")

# Slider
regVal = st.slider("Év kiválasztása", 2015, 2050, 2024)
futureXArr = Data.get_future_list(regVal,2023)

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
dg = Diagram()
dg.build_data_chart(xArray,yArray)
dg.build_regression_chart(xArray,linreg.predict(xArray))
dg.build_future_chart(futureXArr,linreg.predict(futureXArr))
dg.add_legends()
st.write(dg.fig) #Grafikon streamlit-ba ágyazása

# Data matrix
with st.expander("Tényleges Adatok"):
  st.dataframe(df)

