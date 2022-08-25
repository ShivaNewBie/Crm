<template>
  <Navbar @logout="logoutAcc" />
  <router-view />
</template>

<script>
// import { axios } from "@/common/api.service.js";
import axios from "axios";
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
    if (this.$store.state.token) {
      console.log(this.$store.state.team.id);
      //if the token exists
      console.log("initialize token");

      axios.defaults.headers.common["Authorization"] =
        "Token " + this.$store.state.token; //token will be added automatically everytime we use axios WARNING!!! DO NOT FORGET TO USE SPACE IN AFTER TOKEN
    } else {
      console.log("no token");
      axios.defaults.headers.common["Authorization"] = ""; //not authenticated
    }
    // if (!this.$store.state.team.id) {
    //   console.log("test");
    //   //if there is no team created. 0 will return false
    //   this.$router.push("/add-team/");
    // }
  },
};
</script>

<style lang="scss"></style>
