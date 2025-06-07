import streamlit as st

# Sample movie recommendations by genre
movie_db = {
    "Action": ["Mad Max: Fury Road", "John Wick", "Gladiator", "The Dark Knight"],
    "Comedy": ["Superbad", "Step Brothers", "The Hangover", "Anchorman"],
    "Drama": ["The Shawshank Redemption", "Forrest Gump", "Fight Club", "The Godfather"],
    "Sci-Fi": ["Inception", "Interstellar", "The Matrix", "Blade Runner 2049"],
    "Romance": ["Titanic", "The Notebook", "Pride & Prejudice", "La La Land"],
}

# Title
st.title("🎬 Movie Recommendation App")

# Input: User selects a genre
genre = st.selectbox("Choose your favorite movie genre:", list(movie_db.keys()))

# Button to get recommendations
if st.button("Get Recommendations"):
    st.write(f"Here are some great {genre} movies you might like:")
    for movie in movie_db[genre]:
        st.write(f"- {movie}")
