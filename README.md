# 🎬 Movie Recommender System

## 1. 📌 Introduction
A **Recommender System** suggests items to users based on their preferences and behavior. This project implements a **Content-Based Movie Recommender System** that recommends movies similar to those a user has liked, based on the movie's attributes.

🗓️ **Project Timeline**: 2 July 2025 – 7 July 2025  
📁 **Tech Stack**: Python, Pandas, Scikit-Learn, NLTK, Streamlit, TMDB API

---

## 2. 🧠 Types of Recommender Systems
- **Content-Based Filtering:** Suggests items similar to what the user liked before.
- **Collaborative Filtering:** Suggests items liked by similar users.
- **Hybrid Systems:** Combine both approaches for improved recommendations.

---

## 3. 🔁 Project Flow
The project follows a structured end-to-end ML pipeline:
1. **Data Acquisition**
2. **Data Preprocessing**
3. **Model Building**
4. **Website Development**

---

## 4. 🗃️ Data Acquisition
- 📦 **Dataset Source:** [TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Files Used:**
  - `movies.csv`: General movie information
  - `credits.csv`: Cast and crew information
- **Total Movies**: 4803  
- **Features**: 20 columns in `movies.csv`, 4 columns in `credits.csv`

---

## 5. 🧹 Data Preprocessing
### 5.1 Merging Datasets
- Merged `movies.csv` and `credits.csv` on the `title` column to create a unified DataFrame.

### 5.2 Feature Selection
- Kept: `genres`, `id`, `keywords`, `title`, `overview`, `cast`, `crew`
- Dropped: `budget`, `homepage`, `original_title`, `popularity`, etc.

### 5.3 Handling Missing Values
- Dropped 3 rows with missing `overview` values.
- No duplicate records found.

### 5.4 Data Transformation
- Converted stringified list-of-dicts to proper Python objects.
- Extracted:
  - Genre names
  - Top 3 cast members
  - Director from `crew` where job == 'Director'

### 5.5 Text Cleaning
- Removed spaces in names: e.g., `"Sam Worthington"` → `"SamWorthington"`
- Converted `overview` into word lists

### 5.6 Creating the `tags` Feature
- Concatenated `overview`, `genres`, `keywords`, `cast`, and `crew` into one unified text column called `tags`.

✅ Final DataFrame contains: `movie_id`, `title`, and `tags`

---

## 6. 🔢 Text Vectorization
We transformed the `tags` text column into numerical vectors using:

- **Bag of Words (BoW)**: Top 5000 most frequent words
- **Stemming**: Reduces words to their root (e.g., "running", "ran" → "run")
- **Stopword Removal**: Eliminated common words like "the", "is", etc.

### ⚙️ Output:
- Each movie → **5000-dimensional vector**
- **Total comparisons**: 4806 × 4806

---

## 7. 📐 Similarity Measurement
We used **Cosine Similarity** to measure movie similarity:
- Smaller angle → higher similarity
- Larger angle → lower similarity
- Precomputed and stored as a **similarity matrix** for fast recommendations

---

## 8. 🎯 Recommendation Function
When a user selects a movie:
1. Retrieve its vector
2. Compute cosine similarity with all movies
3. Sort similarities in descending order
4. Recommend top 5 most similar movies (excluding the selected one)

---

## 9. 🌐 Website
- Developed using **Streamlit**
- Fetches **movie posters** from the **TMDB API**
- Fully interactive UI with:
  - Movie dropdown selector
  - Display of 5 similar movie recommendations
  - Posters and titles shown in a clean layout

---

## 10. 🧾 Learning Outcomes

By completing this project, I gained hands-on experience and a deeper understanding of :

- **Data Acquisition & Integration:**  
  Learned how to work with real-world datasets from platforms like Kaggle and combine multiple sources (movies and credits data) into a unified structure.

- **Data Cleaning & Feature Engineering:**  
  Practiced handling missing values and transforming complex columns into usable formats to create meaningful features like `tags`.

- **Text Processing & Vectorization:**  
  Gained insight into the Bag of Words (BoW) model, stemming, and stopword removal to convert text into numerical vectors.

- **Similarity Measurement:**  
  Applied cosine similarity to evaluate how closely related two movies are based on their vectorized features.

- **Recommendation Systems:**  
  Built a custom content-based recommendation engine that suggests similar movies based on selected movie attributes.

- **User Interface Design (Streamlit):**  
  Designed a clean, interactive web interface that delivers movie recommendations along with poster visuals for a better user experience.

- **Project Structuring & Documentation:**  
  Strengthened my ability to organize machine learning projects effectively, write readable code, and document the workflow clearly.

---

## 11. 🔗 Project Links

| Resource              | Link                                                                 |
|-----------------------|----------------------------------------------------------------------|
| 📂 GitHub Repository  | https://github.com/Aryanupadhyay23/Movie-Recommender-System-Project |
| 📂 Onedrive           | https://1drv.ms/f/s!AnIMLJJR3BeYcN944wrLT0-XUjI?e=Xd48UG |
