<template>
  <div class="container">
    <button type="button" class="btn btn-primary">{{ msg }}</button>
    <!-- <p>{{ msg }}</p> -->
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "MovieTitle",
  data() {
    return {
      msg: "MOVIES!",
      API_HOST: process.env.VUE_APP_API_URL
    };
  },
  methods: {
    getMessage() {
      const path = API_HOST + "/titles";
      axios
        .get(path)
        .then(res => {
          this.msg = res.data;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
  created() {
    this.getMessage();
  }
};
</script>
