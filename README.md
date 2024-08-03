Movie Recommender System
Overview
A web-based movie recommender system that suggests movies based on user input. The system uses cosine similarity on movie metadata to generate recommendations.

Features
Movie Data Processing:

Merges movie and credit datasets.
Processes genres, keywords, cast, and crew information.
Stems words and removes spaces for better similarity comparison.
Movie Recommendation:

Utilizes cosine similarity on movie tags.
Recommends top 5 movies similar to the selected or searched movie.
Web Interface:

Dropdown and search bar for movie selection.
Displays recommendations in a table format.
Setup
Prerequisites
Python 3.x
Flask
pandas
nltk
scikit-learn
