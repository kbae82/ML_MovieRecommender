<template>
  <b-table
    sticky-header="500px"
    :items="movies"
    :fields="fields"
    :sort-by.sync="sortBy"
    :sort-desc.sync="sortDesc"
    sort-icon-left
    responsive="sm"
  >
    <template v-slot:cell(show_details)="row">
      <b-button
        variant="outline-primary"
        size="sm"
        @click="row.toggleDetails"
        class="mr-2"
      >
        {{ row.detailsShowing ? "Hide" : "Show" }}
      </b-button>
    </template>
    <template v-slot:row-details="row">
      <b-card>
        <b-row class="mb-2">
          <b-col sm="3" class="text-sm-right"><b>Overview:</b></b-col>
          <b-col>{{ row.item.overview }}</b-col>
        </b-row>
        <b-row class="mb-2">
          <b-col sm="3" class="text-sm-right"><b>Cast:</b></b-col>
          <b-col>{{ row.item.cast }}</b-col>
        </b-row>
        <b-row class="mb-2">
          <b-col sm="3" class="text-sm-right"><b>Poster:</b></b-col>
          <b-col v-if="row.item.poster_url === 'N/A'">
            N/A
          </b-col>
          <b-col v-else>
            <a :href="row.item.poster_url" target="_blank">
              View Poster
            </a>
          </b-col>
        </b-row>
        <b-row class="mb-2">
          <b-col sm="3" class="text-sm-right"><b>Budget:</b></b-col>
          <b-col v-if="row.item.budget < 100">
            N/A
          </b-col>
          <b-col v-else> ${{ row.item.budget.toLocaleString() }} </b-col>
        </b-row>
        <b-row class="mb-2">
          <b-col sm="3" class="text-sm-right"><b>Revenue:</b></b-col>
          <b-col v-if="row.item.revenue < 100">
            N/A
          </b-col>
          <b-col v-else> ${{ row.item.revenue.toLocaleString() }} </b-col>
        </b-row>
      </b-card>
    </template>
  </b-table>
  <!-- </div>
    </div>
  </div> -->
</template>

<script>
import axios from "axios";
import { EventBus } from "./event_bus.js";

export default {
  data() {
    return {
      isBusy: false,
      sortBy: "rank",
      sortDesc: false,
      path: process.env.VUE_APP_API_URL,
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
      movies: []
    };
  },
  methods: {
    loadRecommendedMovies(selectedMovie, selectedLimit) {
      EventBus.$emit("showLoading", "Loading...");
      if (this.isBusy) {
        return;
      }
      this.isBusy = true;
      this.movies = [];
      this.path += "/search?title=";
      this.path += selectedMovie;
      this.path += "&result=";
      this.path += selectedLimit;
      axios
        .get(this.path)
        .then(res => {
          for (var i = 0; i < res.data.length; i++) {
            // console.log(res.data[i]);
            this.movies.push(JSON.parse(res.data[i]));
          }
        })
        .then(() => {
          EventBus.$emit("hideLoading", "Completed...");
          this.isBusy = false;
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
  created() {
    EventBus.$on("loadRecommendedMovies", data => {
      this.loadRecommendedMovies(data.selectedMovie, data.selectedLimit);
    });
  }
};
</script>
