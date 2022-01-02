import plotly.express as px
import pandas as pd
df = pd.read_excel('/Users/ashfi/Documents/R projects/activity.xlsx')
fig = px.histogram(df, x = 'Category', y = 'Amount', color='Category')
fig.show()