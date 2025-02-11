import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    filtered = views[views['author_id'] == views['viewer_id']]
    filtered_unique = filtered['author_id'].unique()
    unique_authors = sorted(filtered_unique)
    result = pd.DataFrame({'id' : unique_authors}) 
    return result
