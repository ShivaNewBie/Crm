<template>
  <Navbar />
  <router-view />
</template>

<script>
import { axios } from "@/common/api.service.js";

import Navbar from "@/components/Navbar.vue";

export default {
  name: "App",
  components: {
    Navbar,
  },
  beforeCreate() {
    this.$store.commit("initializeStore"); //will run the function in store initializesStore
    if (this.$store.state.token) {
      //if the token exists
      axios.defaults.headers.common["Authorization"] =
        "Token" + this.$store.state.token; //token will be added automatically everytime we use axios
      console.log(this.$store.state.token);
    } else {
      axios.defaults.headers.common["Authorization"] = ""; //not authenticated
      console.log("test");
    }
  },
};
</script>

<style lang="scss"></style>
