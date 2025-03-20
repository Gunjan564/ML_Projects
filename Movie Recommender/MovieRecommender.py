import streamlit as st
import pandas as pd
import pickle
import requests
import joblib
import time

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=e5278aaeb91f8e36a3e7f82cd57d9b2d"
    
    try:
        start_time = time.time()  # Track API call time
        response = requests.get(url, timeout=5)  # ✅ Timeout set
        elapsed_time = time.time() - start_time
        print(f"API Call Time: {elapsed_time:.2f} sec")  # ✅ Log API time
        
        response.raise_for_status()
        data = response.json()
        
        if "poster_path" in data and data["poster_path"]:
            return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching poster for ID {movie_id}: {e}")  
        return "https://via.placeholder.com/500x750?text=No+Image"  

def recommend(movie):
  index = movies[movies['title'] == movie].index[0]
  distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
  recommended_movie_names = []
  recommended_movie_posters = []
  for i in distances[1:6]:
    movie_id = movies.iloc[i[0]].movie_id
    recommended_movie_posters.append(fetch_poster(movie_id))
    recommended_movie_names.append(movies.iloc[i[0]].title)

  return recommended_movie_names,recommended_movie_posters

# Load the processed data
movies_dict = pickle.load(open(r'Movie Recommender\\new_movies.pkl', 'rb'))
similarity = pickle.load(open(r'Movie Recommender\similarity.pkl','rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Enter the Movie name',
    movies['title'].values
)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)    
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