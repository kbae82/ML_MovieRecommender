import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";
import { ButtonPlugin } from "bootstrap-vue";
import Autocomplete from "@trevoreyre/autocomplete-vue";
import "@trevoreyre/autocomplete-vue/dist/style.css";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.config.productionTip = false;

// Install BootstrapVue
Vue.use(BootstrapVue);
// Optionally install the BootstrapVue components plugin
Vue.use(IconsPlugin);
Vue.use(ButtonPlugin);

//Install Autocomplete
Vue.use(Autocomplete);

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
