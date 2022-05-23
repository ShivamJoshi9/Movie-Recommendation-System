import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    responce = requests.get("https://api.themoviedb.org/3/movie/{"
                            "}?api_key=2d109c2cf39153f93acc291fde695357&language=en-US".format(movie_id))
    data = responce.json()
    return "http://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    index = movies_list[movies_list['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])

    recommended_movies = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies_list.iloc[i[0]].id
        # fetch poster
        recommended_movies.append(movies_list.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_poster


movies_list = pickle.load(open('movies_list.pkl','rb'))
movies_list = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('MOVIE RECOMMENDATION SYSTEM')

selected_movie = st.selectbox(
'How would you like to be contacted?',
movies_list['title'].values)

st.write('You selected:', selected_movie)

if st.button('Recommend'):
    names,poster = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
