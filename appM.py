import streamlit as st
import pickle
import pandas as pd
import requests

# Set page config
st.set_page_config(page_title="Movie Recommender 🎬", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main {
        background-color: #f0f2f6;
    }
    h1 {
        color: #e50914;
        font-family: 'Segoe UI', sans-serif;
        text-align: center;
    }
    .movie-title {
        font-weight: bold;
        color: #333333;
        text-align: center;
        margin-top: 10px;
    }
    .movie-card {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: transform 0.3s;
        text-align: center;
    }
    .movie-card:hover {
        transform: scale(1.05);
    }
    img {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# OMDb API Key
API_KEY = '830d389e'


# Function to fetch movie poster using OMDb API
def fetch_poster(movie_title):
    try:
        url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"
        response = requests.get(url, timeout=5)
        data = response.json()
        poster_url = data.get('Poster')
        if poster_url and poster_url != "N/A":
            return poster_url
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except Exception as e:
        print(f"Error fetching poster for {movie_title}: {e}")
        return "https://via.placeholder.com/500x750?text=Error"


# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_title = movies.iloc[i[0]].title
        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_poster(movie_title))

    return recommended_movies, recommended_posters


# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# App Title
st.markdown("<h1>🍿 Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Get Similar Movie Suggestions Instantly!</h4>",
            unsafe_allow_html=True)
st.markdown("---")

# Select box for movie input
selected_movie_name = st.selectbox("🎥 Select a movie you like:", movies['title'].values)

if st.button('🔍 Recommend'):
    names, posters = recommend(selected_movie_name)
    st.markdown("### 🎯 Top 5 Recommendations for You:")
    st.markdown("<br>", unsafe_allow_html=True)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            col.markdown(f"""
                <div class='movie-card'>
                    <img src="{posters[idx]}" width="100%" height="300px">
                    <div class='movie-title'>{names[idx]}</div>
                </div>
            """, unsafe_allow_html=True)
