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
      } catch (error) {
        console.log(error);
      }

      this.$router.push("/login");
      axios.defaults.headers.common["Authorization"] = "";
      localStorage.removeItem("token");

      this.$store.commit("removeToken");
    },
  },
  beforeCreate() {
    this.$store.commit("initializeStore"); //will run the function in store initializesStore
    console.log(this.$store.state.user);
    if (this.$store.state.token) {
      //if the token exists
      axios.defaults.headers.common["Authorization"] =
        "Token" + this.$store.state.token; //token will be added automatically everytime we use axios
    } else {
      axios.defaults.headers.common["Authorization"] = ""; //not authenticated
    }
    if (!this.$store.state.team.id) {
      //if there is no team created. 0 will return false
      this.$router.push("/add-team/");
    }
  },
};
</script>

<style lang="scss"></style>
