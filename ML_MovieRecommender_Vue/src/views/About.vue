<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="w-100">
          <div class="mt-5">
            <h4>Content-Based Recommendation with Machine Learning</h4>
            <p class="ml-4">Common examples: Amazon, Netflix, LinkedIn</p>
            <p class="ml-4">ML Model Concept: Text -> Vector -> Cosine Value</p>
            <p class="ml-4">
              A) Apple Orange Apple <br />
              B) Orange Orange Apple <br />
              Vectorize text values then use cosine distance as relate
              scores.<br />
            </p>
            <img src="@/assets/cosine_distance.png" class="ml-3" />
            <br />
            <br />
            <p class="ml-4">Now apply cosine distance concept to movies</p>
            <img
              src="@/assets/cosine_distance_matrix_movies.png"
              class="ml-3"
            />
            <br />
            <br />
            <p class="ml-4">
              Movie 0 is most similar movie is Movie 2<br />
              Movie 1 is most similar movie is Movie 3<br />
              Movie 2 is most similar movie is Movie 0 <br />
              Movie 3 is most similar movie is Movie 1
            </p>
            <br />
            <h4>ML Model Architecture</h4>
            <ol>
              <li>
                Use 'CountVectorizer' to transform criteria [Keyword, Director,
                Cast, Genre] into Vectors
              </li>
              <li>
                Use 'cosine_similarity' to generate similarity scores.
              </li>
            </ol>
            <h4>Application Architecture</h4>
            <ol>
              <li>CSV data will be extracted/formatted with Python</li>
              <li>
                ML Model
                <a href="https://scikit-learn.org/stable/" target="_blank">
                  with Scikit Learn
                </a>
              </li>
              <li>
                <a
                  href="https://flask.palletsprojects.com/en/1.1.x/"
                  target="_blank"
                >
                  Python Flask</a
                >
                API which is a middle layer to access ML model result
              </li>
              <li>
                <a href="https://vuejs.org/" target="_blank"> Vue JS</a>
                client application to call API and render UI with data
              </li>
            </ol>
            <h4>Possible Uses Case</h4>
            <p class="ml-4">
              This Model can be used for 'Comparing similarities between data of
              uneven size'. For example, we can find similar incident reports
              with specific criteria. (Location, people, type, causes, etc.)
            </p>
            <h4>Future Improvements</h4>
            <ul>
              <li>We can add the weight system to find optimal results.</li>
              <li>
                Adding number value calculation will be an improvement.
              </li>
              <li>UI/UX can be improved with more design time</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
