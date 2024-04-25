import UK
import france
import germany
import belgium
import italy

import pandas as pd


# France
france70 = pd.DataFrame(france.france70,columns=['Date','Franc_F'])
france70['date'] = pd.to_datetime(france70['Date'],format='%d-%b-%y')
france70['Franc_F'] = france70['Franc_F'].astype(float)
france70 = france70.groupby(pd.Grouper(key='date',freq='a'))['Franc_F'].mean().reset_index()
france70['year'] = france70.date.dt.year


france90 = pd.DataFrame(france.france90,columns=['Date','Franc_F'])
france90['date'] = pd.to_datetime(france90['Date'],format='%d-%b-%y')
france90['Franc_F'] = france90['Franc_F'].astype(float)
france90 = france90.groupby(pd.Grouper(key='date',freq='a'))['Franc_F'].mean().reset_index()
france90['year'] = france90.date.dt.year

# France combined
France = pd.concat([france70,france90], keys=["Franc_F", "year"]).reset_index()
France = France[['Franc_F','year']]




# Italy 
italy70 = pd.DataFrame(italy.italy70,columns=['Date','Lira'])
italy70['date'] = pd.to_datetime(italy70['Date'],format='%d-%b-%y')
italy70['Lira'] = italy70['Lira'].astype(float)


italy70 = italy70.groupby(pd.Grouper(key='date',freq='a'))['Lira'].mean().reset_index()
italy70['year'] = italy70.date.dt.year

italy90 = pd.DataFrame(italy.italy90,columns=['Date','Lira'])
italy90['date'] = pd.to_datetime(italy90['Date'],format='%d-%b-%y')
italy90['Lira'] = italy90['Lira'].astype(float)


italy90 = italy90.groupby(pd.Grouper(key='date',freq='a'))['Lira'].mean().reset_index()
italy90['year'] = italy90.date.dt.year



# Italy combined
Italy = pd.concat([italy70,italy90], keys=["Lira", "year"]).reset_index()
Italy = Italy[['Lira','year']]






# Germany 
germany70 = pd.DataFrame(germany.germany70,columns=['Date','DeustcheMark'])
germany70['date'] = pd.to_datetime(germany70['Date'],format='%d-%b-%y')
germany70['DeustcheMark'] = germany70['DeustcheMark'].astype(float)


germany70 = germany70.groupby(pd.Grouper(key='date',freq='a'))['DeustcheMark'].mean().reset_index()
germany70['year'] = germany70.date.dt.year

germany90 = pd.DataFrame(germany.germany90,columns=['Date','DeustcheMark'])
germany90['date'] = pd.to_datetime(germany90['Date'],format='%d-%b-%y')
germany90['DeustcheMark'] = germany90['DeustcheMark'].astype(float)


germany90 = germany90.groupby(pd.Grouper(key='date',freq='a'))['DeustcheMark'].mean().reset_index()
germany90['year'] = germany90.date.dt.year



# Germany combined
Germany = pd.concat([germany70,germany90], keys=["DeustcheMark", "year"]).reset_index()
Germany = Germany[['DeustcheMark','year']]
























