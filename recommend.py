# %%
import numpy as np
import pandas as pd
import ast

# %%
movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')


# %%
movies = movies.merge(credits,on ='title')


# %%

movies = movies[['movie_id','keywords','genres','title','overview','cast','crew']]


# %%
movies.dropna(inplace =True)
movies.isnull().sum()
movies.duplicated().sum()

# %%
movies.iloc[0].genres


# %%
def convert(obj):
    l=[]
    for i in ast.literal_eval(obj):
        l.append(i['name'])
    return l


# %%
movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)

# %%
def convert3(obj):
    l=[]
    c=0
    for i in ast.literal_eval(obj):
        if c!= 3:
            l.append(i['name'])
            c+=1
        else:
            break
    return l
movies['cast'] = movies['cast'].apply(convert3)

def f(obj):
    l=[]
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            l.append(i['name'])
            break
    return l
#print(movies['crew'].apply(f))
movies['crew'] = movies['crew'].apply(f)

# %%
movies['overview'] = movies['overview'].apply(lambda x:x.split())
movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ","") for i in x ])
movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x ])
movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x ])
movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ","") for i in x ])

# %%
movies['tags']= movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

new_df = movies[['movie_id','title','tags']]
new_df.loc[:, 'tags'] = new_df['tags'].apply(lambda x:" ".join(x))
new_df.loc[:, 'tags'] = new_df['tags'].apply(lambda x:x.lower())


# %%
import nltk 
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)



# %%
new_df.loc[: , 'tags'] = new_df['tags'].apply(stem)

# %%
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()

# %%
cv = CountVectorizer(max_features=5000, stop_words = 'english')
vectors = cv.fit_transform(new_df['tags']).toarray()

# %%
from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vectors)

# %%
new_df.loc[: ,'title'] = movies['title']


# %%
def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)) ,reverse=True,key= lambda x:x[1])[1:6]
    recommended_titles = []
    for i in movie_list:
        recommended_titles.append(new_df.iloc[i[0]].title)   
    return recommended_titles
       



# %%
def get_movie_titles():
    return new_df['title'].tolist()


