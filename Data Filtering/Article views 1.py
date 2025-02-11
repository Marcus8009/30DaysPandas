import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    filtered = views[views['author_id'] == views['viewer_id']]
    filtered_unique = filtered['author_id'].unique()
    unique_authors = sorted(filtered_unique)
    result = pd.DataFrame({'id' : unique_authors}) 
    return result
    
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views.rename(columns = {'author_id' : 'id'})
    filtered_views = (views['id'] == views['viewer_id'])
    views = views.loc[filtered_views, ['id']].drop_duplicates()
    return views.sort_values(by = 'id', ascending = True)
    
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df=views[views.author_id==views.viewer_id].drop_duplicates('author_id')
    df=df.sort_values(by='author_id',ascending=True)
    df.rename(columns={'author_id':'id'},inplace=True)
return pd.DataFrame(df['id'])

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views.query('author_id==viewer_id')[['author_id']].rename(columns={'author_id': 'id'}).drop_duplicates().sort_values(by='id')


'''
First Answer:

Filters the DataFrame to include rows where author_id equals viewer_id.
Extracts unique author_id values, sorts them, and creates a new DataFrame with these sorted values.
Returns the resulting DataFrame.
Second Answer:

Renames the author_id column to id.
Filters the DataFrame to include rows where id equals viewer_id.
Drops duplicate id values and sorts the DataFrame by id.
Returns the resulting DataFrame.
Third Answer:

Filters the DataFrame to include rows where author_id equals viewer_id and drops duplicate author_id values.
Sorts the DataFrame by author_id and renames the author_id column to id.
Returns a new DataFrame with the id column.
Fourth Answer:

Uses the query method to filter the DataFrame where author_id equals viewer_id.
Selects the author_id column, renames it to id, drops duplicates, and sorts the DataFrame by id.
Returns the resulting DataFrame.


'''
