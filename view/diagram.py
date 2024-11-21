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
    self.ax.legend(shadow=True,fontsize = "x-small") #Diagram nevek mérete

  def buildDataChart(self,xArray,yArray):
    self.ax.plot(xArray,yArray,"o",color="orange", label = "Tényleges") #Eredeti adatok
    
  def buildRegressionChart(self,xArray,yArray):
    self.ax.plot(xArray,yArray,"o",color="orange", label = "Tényleges") #Eredeti adatok
    
  def buildFutureChart(self,xArray,yArray):
    self.ax.plot(xArray,yArray,"o",color="orange", label = "Tényleges") #Eredeti adatok
    
  
    