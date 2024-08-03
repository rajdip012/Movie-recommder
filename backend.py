from flask import Flask, request, jsonify, render_template
from recommend import get_movie_titles, recommend

app = Flask(__name__)

@app.route('/')
def index():
    titles = get_movie_titles()
    return render_template('index.html', titles=titles)

@app.route('/recommend', methods=['POST'])
def recommend_movies():
    movie = request.form['movie']
    recommendations = recommend(movie)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
