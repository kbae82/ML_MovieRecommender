import pandas as pd
import json
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os


# Return the movie title from data frame with index
def get_title_from_index(df, index):
    return df[df.index == index]["title"].values[0]


# Return the movie object from data frame with index
def get_movie_object_from_index(df, index):
    return df[df.index == index]


# Return the index of movie object from data frame with title
def get_index_from_title(df, title):
    check_title = df[df.title.str.lower() == title.lower()]
    if not check_title.empty:
        return df[df.title.str.lower() == title.lower()]["index"].values[0]
    return None


# Read CSV file (movie dataset) and put them into data frame
def read_feature_from_file():
    df = pd.read_csv("movie_dataset.csv")

    # Select Features
    features = ['keywords', 'cast', 'genres', 'director']

    for feature in features:
        df[feature] = df[feature].fillna('')

    return df


# Create a custom column with combined movies attributes
# 'Keywords', 'Cast', 'Genres', 'Director'
def combine_features(row):
    try:
        return row['keywords'] + " " + row['cast'] + " " + row["genres"] + " " + row["director"]
    except():
        print("Error:", row)


# Add the custom column to the data frame
def setup_data_frame():
    df = read_feature_from_file()
    df.fillna('', inplace=True)
    df["combined_features"] = df.apply(combine_features, axis=1)
    return df


def process_data(df, movie_user_likes, result_limit):
    return calculate_data(df, result_limit, movie_user_likes)


# Create count matrix from the new combined column
# Compute the Cosine Similarity based on the count matrix
def calculate_data(df, result_limit, movie_user_likes):
    cv = CountVectorizer()

    counter_matrix = cv.fit_transform(df["combined_features"])
    similarity_cosine = cosine_similarity(counter_matrix)

    # Step 6: Get index of this movie from its title
    movie_index = get_index_from_title(df, movie_user_likes)
    similarity_movies = list(enumerate(similarity_cosine[movie_index]))

    # Step 7: Get a list of similar movies in descending order of similarity score
    sorted_similarity_movies = sorted(similarity_movies, key=lambda x: x[1], reverse=True)

    # Step 8: Print titles of first 10 movies
    # print_result_movie_title(df, sorted_similarity_movies, result_limit)
    return return_result_movies(df, sorted_similarity_movies, result_limit)


def return_result_movies(df, result_list, result_limit):
    result_movies_list = []
    # i = 1
    for index, element in zip(range(result_limit), result_list):
        try:
            json_movie_object = get_movie_object_from_index(df, element[0]).to_json(orient='records')
            json_movie_object = insert_rank_and_poster_url_with_title(json_movie_object, index)
            result_movies_list.append(json_movie_object)
        except():
            print(index)
            print(json_movie_object)
    return result_movies_list


def print_result_movie_title(df, result_list, print_limit):
    i = 0
    for element in result_list:
        # print(get_title_from_index(df, element[0]))
        if i == print_limit:
            return
        i = i + 1


def insert_rank_and_poster_url_with_title(json_movie_object, rank):

    try:
        json_movie_object_to_return = json.loads(json_movie_object)[0]
        json_movie_object_to_return['rank'] = rank + 1
        title_url_encoded = requests.utils.quote(json.loads(json_movie_object)[0]['title'])
        response = requests.get("https://omdbapi.com/?apikey="
                                + os.environ.get('OMDB_APIKEY')
                                + "&t=" + title_url_encoded)
        data = response.json()

        if data['Response'] != "False":
            json_movie_object_to_return['poster_url'] = (data['Poster'])
        else :
            json_movie_object_to_return['poster_url'] = "N/A"

        return json.dumps(json_movie_object_to_return)
    except():
        print("Error")
        print(json_movie_object)
