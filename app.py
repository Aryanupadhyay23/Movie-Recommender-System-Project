import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests

movies_df = pickle.load(open('movies.pkl', 'rb'))
title = movies_df['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key="Your API Key"&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(selected_movie_name , top_n=5):

    movie_index = movies_df[movies_df['title'] == selected_movie_name].index[0]
    distances = similarity[movie_index]

    # Get top-N similar movies (excluding the movie itself)
    recommended_indices = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:top_n+1]

    recommended_movies = []
    recommended_movies_posters = []
    for i in recommended_indices:
        movie_id = movies_df.iloc[i[0]].movie_id
        recommended_movies.append(movies_df.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


st.title('Movie Recommender System')

selected_movie_name = st.selectbox("Input Movie :",title)

if st.button("Recommend"):
    names,posters = recommend(selected_movie_name)

    col1 , col2 , col3 , col4 , col5 = st.columns(5)
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






