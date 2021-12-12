from flask import *
import pandas as pd

app = Flask(__name__)

# import dataset
movie_data = pd.read_csv('machine_learning_model/IMDb_Movie_Dataset.csv', index_col=0)
movie_rec_data = pd.read_csv('machine_learning_model/movie_recommendation_dataset.csv')

def get_recommendation(movie_name):
    # find movie index
    movie_index = df.index[df['Title'] == movie_name].values[0]

    # get list of movies recommendation
    movies = movie_rec_data[movie_index]
    movie_rec = []
    for movie in movies:
        temp = []
        title = movie_data['Title'][movie]
        year = movie_data['Year'][movie]
        genre = movie_data['Genre'][movie]
        rating = movie_data['Rating'][movie]

        temp.append(title)
        temp.append(year)
        temp.append(genre)
        temp.append(rating)
    movie_rec.append(temp)
    return movie_rec

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    input_movie = request.form["input"]
    return render_template('home.html', get_recommendation(input_movie))

if __name__ == '__main__':
    app.run(debug=True)