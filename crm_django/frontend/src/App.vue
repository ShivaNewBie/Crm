<template>
  <Navbar @logout="logoutAcc" />
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
  methods: {
    async logoutAcc() {
      let endpoint = "/auth/token/logout/";

      try {
        const response = await axios.post(endpoint);
        console.log(response);
        axios.defaults.headers.common["Authorization"] = "";
        localStorage.removeItem("token");

        this.$store.commit("removeToken");
      } catch (error) {
        console.log(error);
      }
    },
  },
  beforeCreate() {
    this.$store.commit("initializeStore"); //will run the function in store initializesStore
    if (this.$store.state.token) {
      //if the token exists
      axios.defaults.headers.common["Authorization"] =
        "Token" + this.$store.state.token; //token will be added automatically everytime we use axios
    } else {
      axios.defaults.headers.common["Authorization"] = ""; //not authenticated
    }
  },
};
</script>

<style lang="scss"></style>
