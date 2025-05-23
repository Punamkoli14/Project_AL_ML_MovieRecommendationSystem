# Project_AL_ML_MovieRecommendationSystem

Link: https://drive.google.com/file/d/1KESJffPbqcIopXhssqNib79xoylmzG13/view?usp=drive_link

Due to file size limitations,give the link here,
similarity.pkl is a serialized binary file generated using Python’s pickle module. It stores the cosine similarity matrix of movies used in the Movie Recommendation System.This file is a core part of the recommendation logic. It allows the system to quickly fetch and compare movie similarities without recalculating the entire matrix every time a user selects a movie.

🎬 Movie Recommendation System
This project is a content-based movie recommender system developed during my internship at Elevate Lab. It suggests movies that are similar to the user's choice using metadata such as genre, cast, crew, and plot.

🔍 Project Overview
This system uses machine learning techniques to calculate similarity between movies based on textual information. The model was built in Jupyter Notebook, and the final web interface was created using Streamlit in PyCharm.

🛠️ Tools & Technologies
Python

Pandas, NumPy, Scikit-learn

Streamlit – for web UI

Pickle – for serialization

OMDb API – to fetch movie posters

Jupyter Notebook – model building

PyCharm – web development

⚙️ Project Workflow
Data Preprocessing
Cleaned and combined features like overview, genre, keywords, cast, and crew from the Kaggle dataset.

Vectorization
Used CountVectorizer to convert movie metadata into feature vectors.

Similarity Computation
Applied cosine similarity to measure content similarity between movies.

Model Storage
Saved results into two files:

movie_dict.pkl: Processed movie metadata

similarity.pkl: Precomputed similarity matrix

Web Integration
Developed an interactive web app using Streamlit to recommend top 5 similar movies along with posters.

🌐 Output-https://github.com/Punamkoli14/Project_AL_ML_MovieRecommendationSystem/blob/main/Screenshot2-MovieRecommendationSystem.png


📁 Project Structure

📦 Movie-Recommender-System/
├── appM.py                # Streamlit frontend logic
├── Movie_Recommender_System_Project.ipynb   # Model training & similarity computation
├── movie_dict.pkl         # Pickled movie metadata
├── similarity.pkl         # Pickled similarity matrix (~176MB, hosted externally)
└── Screenshot.png         # UI screenshot
 
🚀 How to Run
pip install streamlit pandas scikit-learn requests
streamlit run appM.py

🤝 Acknowledgements
Grateful to Elevate Lab for the support and mentorship during the internship.



