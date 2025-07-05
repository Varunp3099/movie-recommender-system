# movie-recommender-system
A movie recommendation system using content-based filtering (NLP + cosine similarity) with a Flask web interface.

#  Movie Recommender System

This is a content-based movie recommendation system built with Python and Flask. It suggests similar movies based on the content (overview, cast, crew, genres, and keywords) using Natural Language Processing and cosine similarity.


## Features

- Recommend top 5 similar movies based on user input
- Cleaned and preprocessed TMDB dataset
- Content-based filtering using NLP
- Web UI using Flask (HTML + CSS)
- Data vectorized using CountVectorizer (Bag of Words model)


## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Flask
- HTML, CSS
- Pickle (for saving processed data)

## How It Works

1. TMDB movie and credit data are merged and processed.
2. Tags are created by combining genres, overview, cast, crew, and keywords.
3. Tags are vectorized using CountVectorizer.
4. Cosine similarity is used to compute movie similarity.
5. User inputs a movie name in the web UI.
6. Top 5 similar movies are returned.

## ML & NLP Concepts Used

### 1. **Text Preprocessing (NLP)**
We extract text-based features from:
- Movie **overview**
- **Genres**
- **Cast** (Top 3 actors)
- **Crew** (Director)
- **Keywords**

These are combined into a single textual **"tags"** field for each movie.

### 2. **Feature Engineering**
Using:
- `ast.literal_eval()` to parse JSON-like fields
- Tokenization and whitespace removal (stemming) 
- Lowercasing and cleaning

### 3. **Vectorization (Bag-of-Words)**
We use **`CountVectorizer`** from `sklearn` to convert the tags into numeric vectors:
- Max features = 5000
- English stopwords removed
- Converts text to a sparse matrix of word counts

### 4. **Similarity Measurement**
We compute **pairwise cosine similarity** between movie vectors to quantify how similar two movies are:
- Cosine Similarity ∈ [0, 1]
- Higher value → higher similarity

### 5. **Recommendation Logic**
Given a movie name:
- Find its vector representation
- Retrieve top 5 movies with the highest cosine similarity (excluding itself)
- Return titles of those similar movies


