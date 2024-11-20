import pandas as pd

def get_futureList(selected_year,futureYear):
  list = []
  if selected_year > futureYear:
    for year in range(futureYear,selected_year+1):
      list+= [[year]]
  else:
    list+= [[selected_year]]
  return list

def get_dfFromCsv(path):
  df = pd.read_csv(path,sep=';',encoding='ansi',header=1)
  return df

def dfManipulation(df):
  df = df.set_index(df.columns[0]).T.rename_axis("Év").rename_axis("",axis="columns").reset_index().iloc[0:,0:2] #Tábla forgatás, manupulálás.
  return df