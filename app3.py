import streamlit as st
import pickle
import pandas as pd
import requests
from requests.exceptions import Timeout
def fetch_poster(movie_id):
    for i in range(10,100,10):
        try:
            url = "https://api.themoviedb.org/3/movie/65?api_key=8265bd1679663a7ea12ac168da84d2e8"
            response = requests.get(url,timeout=80)
            data = response.json()
            break
        except Timeout as e:
            print("Timeout Error")
    #print(data)
    else:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    #print("movies_list",movies_list)

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #print("movie_id:",movie_id)
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters
movies_dict = pickle.load(open("C:/Users/Abhishek/Desktop/Machine learning/movie-recommander-system/movie_dict.pkl","rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("C:/Users/Abhishek/Desktop/Machine learning/movie-recommander-system/similarity.pkl","rb"))
st.title("Movie Recommender System")
selected_movie_name = st.selectbox(
    "How would you like to be contacted",
    movies['title'].values)
if st.button("Recommend"):
    names,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.header(names[0])
        st.image(posters[0])
    with col2:
        st.header(names[1])
        st.image(posters[1])
    with col3:
        st.header(names[2])
        st.image(posters[2])
    with col4:
        st.header(names[3])
        st.image(posters[3])
    with col5:
        st.header(names[4])
        st.image(posters[4])