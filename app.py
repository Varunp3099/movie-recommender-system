from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
new_df = pickle.load(open(os.path.join(BASE_DIR, 'recommender_new_df.pkl'), 'rb'))
similarity = pickle.load(open(os.path.join(BASE_DIR, 'recommender_similarity.pkl'), 'rb'))

def recommend(movie):
    movie = movie.lower()
    if movie not in new_df['title'].str.lower().values:
        return []
    movie_index = new_df[new_df['title'].str.lower() == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [new_df.iloc[i[0]].title for i in movies_list]
    return recommended_movies

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    movie_name = ""
    if request.method == 'POST':
        movie_name = request.form['movie']
        recommendations = recommend(movie_name)
    return render_template('index.html', recommendations=recommendations, movie_name=movie_name)

if __name__ == '__main__':
    app.run(debug=True)