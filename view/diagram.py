import matplotlib.pyplot as plt
import matplotlib as mpl

class Diagram:
  def __init__(self):
    self.fig, self.ax = plt.subplots()
    self.fig.set_figwidth(8) #Grafikon szélesség

    plt.title("A háztartások egy főre jutó éves nettó jövedelme")
    plt.ylabel("mFt / év")
    plt.xlabel("Év")
    plt.grid(linestyle = '--') #Háttér vonalazás
    self.ax.yaxis.set_major_formatter(mpl.ticker.EngFormatter()) #Ez segít Y tengely milliós érték megjelenítésben

  def build_data_chart(self,xArray,yArray):
    self.ax.plot(xArray,yArray,"o",color="orange", label = "Tényleges") #Eredeti adatok
    
  def build_regression_chart(self,xArray,yArrayPredict):
    self.ax.plot(xArray,yArrayPredict,"o:",color="magenta",label = "Lineáris regresszió") #Eredeti X tengely adatok mentén Linreg

  def build_future_chart(self,future_xArray,future_yArray):
    self.ax.plot(future_xArray,future_yArray,"o:", color = "darkturquoise", label = "Prediktív") #Változtatható X tengely adat menti Linreg

  def add_legends(self):
    self.ax.legend(shadow=True,fontsize = "x-small") #Diagram nevek mérete
    
  
    