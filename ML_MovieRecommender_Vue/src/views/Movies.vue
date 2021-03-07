<template>
  <div>
    <Loading></Loading>
    <div class="container">
      <div class="row">
        <div class="w-100">
          <h2>Movies Recommender</h2>
          <Autocomplete></Autocomplete>
          <MovieTable ref="movieTable" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieTable from "@/components/MovieTable.vue";
import Autocomplete from "@/components/Autocomplete.vue";
import Loading from "@/components/Overlay_loading.vue";

export default {
  name: "Movies",
  components: {
    MovieTable,
    Autocomplete,
    Loading
  }
};
</script>
