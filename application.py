import movie_recommender
import json
from flask import Flask, jsonify, request, Response
from flask_cors import CORS

# Debug Setting
DEBUG = True

# Instantiate the app
app = Flask(__name__)
app.debug = DEBUG

# Enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/')
def root():
    return "API IS RUNNING! "


@app.route('/search')
def show_results():
    title = request.args.get('title', type=str)
    if title is None:
        return "Please enter a title"
    result = request.args.get('result', default=2, type=int)
    json_result_list = movie_recommender.process_data(df, title, result)

    if json_result_list is None:
        return "Sorry, Movie '" + title + "' is not found in our database."

    return Response(json.dumps(json_result_list), mimetype='application/json')


@app.route('/titles')
def get_titles():
    return jsonify(title_list)


if __name__ == '__main__':
    df = movie_recommender.setup_data_frame()
    title_list = df['title'].to_list()
    app.run(host='0.0.0.0', port=5000)
