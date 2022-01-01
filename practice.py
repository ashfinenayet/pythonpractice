import pandas as pd
df = pd.read_excel('/Users/ashfi/Documents/R projects/activity.xlsx')
# print(df.tail(3))
# print(df.columns)
#print(df[['City/State', 'Category', 'Country']])
df['year'] = (pd.DatetimeIndex(df['Date']).year)
df['month'] = (pd.DatetimeIndex(df['Date']).month)

#print(df.loc[29, 'Category'])
#print(df.sort_values(['Category', 'Amount'], ascending=[1,0]))
print(df.head(5))
