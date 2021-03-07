# ML Movie Recommender
Machine Learning Movie Recommerder is using Open-source ML library Scikit-learn for CountVectorizer feature.
https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html

In order to use textual data for predictive modeling, the text must be parsed to remove certain words – this process is called tokenization. 
These words need to then be encoded as integers, or floating-point values, for use as inputs in machine learning algorithms. 
This process is called feature extraction (or vectorization)

Scikit-learn’s CountVectorizer is used to convert a collection of text documents to a vector of term/token counts. It also enables the ​pre-processing of text data prior to generating the vector representation. This functionality makes it a highly flexible feature representation module for text.

This application vectorizes movie attributes that use entered then returns similar movies.

For details, please browse to /about page. 

## Dependencies
```
OMDB API - Movie Poster information
http://www.omdbapi.com/
http://www.omdbapi.com/apikey.aspx
```
```
docker - https://docs.docker.com/get-docker/
```
```
docker-compose - https://docs.docker.com/compose/install/
```

## Project setup
```
docker-compose build
```

## Run the project
```
docker-compose up
```

You can deploy this to Azure with simple steps

1. Push your image to your Azure container registry using the Docker CLI
https://docs.microsoft.com/en-us/azure/container-registry/container-registry-get-started-docker-cli

2. Modify the docker compose
https://docs.microsoft.com/en-us/azure/app-service/quickstart-multi-container

Addition Azure information
Deploy a container instance in Azure using the Azure portal
https://docs.microsoft.com/en-us/azure/container-instances/container-instances-quickstart-portal
