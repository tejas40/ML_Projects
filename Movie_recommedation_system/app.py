import streamlit as st
import pandas as pd
from fuzzywuzzy import process
import pickle
import requests 

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data= response.json()

    return "https://image.tmdb.org/t/p/w500/"+ data["poster_path"]

def recommend(movie):
    matches = process.extract(movie, movie_title['title'], limit=len(movie_title))
    threshold = 80
    try:
        close_matches = [match for match in matches if match[1] >= threshold]
        close_name = close_matches[0][0]
    except:
        close_name=matches[0][0]
        

    movie_index= movie_title[movie_title['title']==close_name].index[0]
    distances = similarities[movie_index]
    movie_list = sorted( list(enumerate(distances)), key=(lambda X: X[1])  , reverse=True)[0:6]
    
    recommed_movies=[]
    recommended_movies_posters=[]
    for i in movie_list:

       movie_id=movie_title['movie_id'][i[0]]
       recommed_movies.append(movie_title['title'][i[0]])
       # featch poster from api
       recommended_movies_posters.append(fetch_poster(movie_id)) 
    return recommed_movies , recommended_movies_posters
    




movie_title=pd.read_csv("model\Movie_clean_data.csv")

similarities= pickle.load(open("model\similarities.pkl","rb"))

st.title("Movie Recommender System") 

selected_movie_name = st.selectbox("How would you like to be contacted?" , movie_title["title"] )


if st.button ("Recommend"):
    names , posters  = recommend(selected_movie_name)
   
    col1, col2,col3 ,col4 ,col5 =st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])