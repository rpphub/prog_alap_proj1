import matplotlib.pyplot as plt
import matplotlib as mpl

def buildPlot() -> tuple[plt.Figure, plt.Axes]:
  fig, ax = plt.subplots()
  fig.set_figwidth(8) #Grafikon szélesség

  plt.title("A háztartások egy főre jutó éves nettó jövedelme")
  plt.ylabel("mFt / év")
  plt.xlabel("Év")
  plt.grid(linestyle = '--') #Háttér vonalazás
  
  ax.yaxis.set_major_formatter(mpl.ticker.EngFormatter()) #Ez segít Y tengely milliós érték megjelenítésben
  ax.legend(shadow=True,fontsize = "x-small") #Diagram nevek mérete

  return fig, ax

'''
def buildDataChart() -> tuple[plt.Figure, plt.Axes]:
  ax.plot(xArray,yArray,"o",color="orange", label = "Tényleges") #Eredeti adatok
  
  return fig, ax


'''