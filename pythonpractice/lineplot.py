import plotly.express as px
import pandas as pd
df = pd.read_excel('/Users/ashfi/Documents/R projects/activity.xlsx')
fig = px.line(df, x="Date", y='Amount',
              hover_data={"Date": "|%B"},
              title='custom tick labels')
fig.update_xaxes(
    dtick="M1",
    tickformat="%b\n%Y")
fig.show()
