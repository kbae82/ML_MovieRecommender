<template>
  <div class="vld-parent">
    <loading
      :active.sync="isLoading"
      :can-cancel="false"
      :on-cancel="onCancel"
      :is-full-page="fullPage"
    ></loading>
  </div>
</template>

<script>
import { EventBus } from "./event_bus.js";
// Import component
import Loading from "vue-loading-overlay";
// Import stylesheet
import "vue-loading-overlay/dist/vue-loading.css";

export default {
  data() {
    return {
      isLoading: false,
      fullPage: true
    };
  },
  components: {
    Loading
  },
  methods: {
    onCancel() {
      console.log("User cancelled the loader.");
    }
  },
  created() {
    EventBus.$on("showLoading", data => {
      console.log(data);
      this.isLoading = true;
    });
    EventBus.$on("hideLoading", data => {
      console.log(data);
      setTimeout(() => {
        this.isLoading = false;
      }, 1000);
    });
  }
};
</script>
