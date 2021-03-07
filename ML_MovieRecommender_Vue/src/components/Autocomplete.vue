<template>
  <div class="container">
    <div class="row">
      <div class="w-100">
        <b-alert v-model="showMessage" variant="warning">{{ message }}</b-alert>
        <autocomplete
          data-toggle="tooltip"
          title="Application will find simialr movies based on Genre, Director, Cast, and Keywords!"
          :search="searchRecommendedMovies"
          placeholder="Please type and select a movie"
          aria-label="Please type and select a movie"
          @submit="callLoadRecommendedMovies"
          :debounce-time="500"
          ref="autocomplete_input"
        ></autocomplete>
        <span>Result Limit: </span>
        <select v-model="selectedLimit" label="Result limit">
          <option disabled value="">--</option>
          <option>5</option>
          <option>10</option>
          <option>25</option>
          <option>50</option>
        </select>
        <br />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { EventBus } from "./event_bus.js";

export default {
  data() {
    return {
      sortBy: "rank",
      sortDesc: false,
      fields: [
        { key: "rank", label: "Rank", sortable: true },
        { key: "title", label: "Title", sortable: true },
        { key: "runtime", label: "Runtime", sortable: true },
        { key: "genres", label: "Genres", sortable: true },
        { key: "original_language", label: "Language", sortable: true },
        { key: "director", label: "Direcctor", sortable: true },
        { key: "release_date", label: "Released", sortable: true },
        { key: "show_details", label: "Details", sortable: false }
      ],
      movieTitles: [],
      movies: [],
      showMessage: false,
      message: "",
      selectedMovie: "",
      selectedLimit: 10,
      API_HOST: process.env.VUE_APP_API_URL
    };
  },
  methods: {
    searchRecommendedMovies(input) {
      if (input.length < 2) {
        return [];
      } else {
        return this.movieTitles.filter(movieTitle => {
          return movieTitle.toLowerCase().includes(input.toLowerCase());
        });
      }
    },
    callLoadRecommendedMovies(targetMovie) {
      this.message = "";
      this.showMessage = false;
      if (targetMovie == null) {
        this.message = "Please type and 'select' a movie";
        this.showMessage = true;
        return;
      }
      this.selectedMovie = targetMovie;
      EventBus.$emit("loadRecommendedMovies", {
        selectedMovie: this.selectedMovie,
        selectedLimit: this.selectedLimit
      });
    },
    getMovieTitles() {
      const path = this.API_HOST + "/titles";
      axios
        .get(path)
        .then(res => {
          this.movieTitles = res.data;
          // console.log(res.data);
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
  created() {
    this.getMovieTitles();
    // this.loadRecommendedMovies();
  }
};
</script>
<style>
.autocomplete-input {
  padding: 12px 12px 12px 48px !important;
  margin-bottom: 5px;
  min-width: 450px !important;
}
.autocomplete-result-list {
  z-index: 5 !important;
}
</style>
