import pandas as pd
df = pd.read_csv('articles.csv')
df = df.sort_values('total_events' , ascending = False)
output = df[['original_title' , 'poster_link' , 'runtime', 'release_date' , 'total_events' ]].head(20)