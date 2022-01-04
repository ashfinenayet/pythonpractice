import calendar
import pandas as pd
df = pd.read_csv('tiktok.csv')
df.drop_duplicates(inplace=True)
# removes duplicates from original data frame
#print(df[['City/State', 'Category', 'Country']])
#df['year'] = (pd.DatetimeIndex(df['Date']).year)
#df['month'] = (pd.DatetimeIndex(df['Date']).month)

#print(df.loc[29, 'Category'])
#print(df.sort_values(['Category', 'Amount'], ascending=[1,0]))
#print(df.head(5))
#df.reset_index(inplace=True)
#df['month_name'] = df['month'].apply(lambda x: calendar.month_abbr[x])
#df.to_excel('modified2.xlsx', index=False)
df.to_excel('modifiedtiktok.xlsx', index=False)