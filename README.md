# 🎬 Movie Recommender System

## 📌 Introduction
A **Recommender System** suggests items to users based on their preferences and behavior. This project implements a **Content-Based Movie Recommender System** that recommends movies similar to those a user has liked, based on the movie's attributes.

## 🧠 Types of Recommender Systems
- **Content-Based Filtering:** Suggests items similar to what the user liked before.
- **Collaborative Filtering:** Suggests items liked by similar users.
- **Hybrid Systems:** Combine both approaches for improved recommendations.

## 🔁 Project Flow
The project follows a structured end-to-end ML pipeline:
1. **Data Acquisition**
2. **Data Preprocessing**
3. **Model Building**
4. **Website Development**
5. **Deployment**

## 🗃️ Data Acquisition
- **Dataset Source:** [TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Files Used:**
  - `movies.csv`: General movie information
  - `credits.csv`: Cast and crew information
- Total Movies: 4803  
- Total Features: 20 (movies), 4 (credits)

## 🧹 Data Preprocessing
Key preprocessing steps:
- **Merged** the two datasets on the `title` column.
- **Selected** essential columns: `genres`, `id`, `keywords`, `title`, `overview`, `cast`, `crew`.
- **Dropped** irrelevant columns and rows with missing overviews.
- **Transformed** nested dictionary columns into readable lists.
- **Text Cleaned** the tags by:
  - Removing spaces in names (e.g., `Sam Worthington → SamWorthington`)
  - Converting overviews into word lists
- **Created** a new `tags` feature by concatenating all processed text.

## 🔢 Text Vectorization
To compare movies, we convert tags into numerical vectors using:
- **Bag of Words (BoW)** with 5000 most common words
- **Stemming** (e.g., "running", "ran" → "run")
- **Stopwords Removal**

### ⚙️ Output:
- Each movie is now represented by a **5000-dimensional vector**
- Total similarity comparisons: **4806 x 4806**

## 📐 Similarity Measurement
- We use **Cosine Similarity** to compare vectors.
- A smaller cosine angle indicates higher similarity.
- Similarity Matrix is precomputed for fast lookups.

## 🔁 Recommendation Function
When a user selects a movie:
1. The movie's vector is retrieved.
2. Cosine similarity with all other movies is calculated.
3. Top 5 most similar movies are selected.
4. Recommendations are returned.

## 🌐 Website
- Built using **Streamlit**
- Fetches **movie posters** using **TMDB API** for better visuals
- Fully interactive UI for movie selection and recommendations
