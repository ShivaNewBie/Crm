<template>
  <div class="container">
    <form @submit.prevent="onSubmit">
      <div class="form-group">
        <label for="exampleInputEmail1">Email address</label>
        <input
          v-model="email"
          type="email"
          class="form-control"
          id="exampleInputEmail1"
          aria-describedby="emailHelp"
          placeholder="Enter email"
        />
      </div>
      <div class="form-group">
        <label for="exampleInputPassword1">Password</label>
        <input
          v-model="password1"
          type="password"
          class="form-control"
          id="exampleInputPassword1"
          placeholder="Password"
        />
      </div>

      <button type="submit" class="btn btn-primary mt-2">Submit</button>
    </form>
  </div>
</template>

<script>
// import { axios } from "@/common/api.service.js";

import axios from "axios";
export default {
  name: "Login",
  data() {
    return {
      email: "",
      password1: "",
      errors: [],
    };
  },
  methods: {
    async onSubmit() {
      axios.defaults.headers.common["Authorization"] = "";
      // axios.defaults.xsrfCookieName = "csrftoken";
      // axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
      localStorage.removeItem("token");
      let endpoint = "/auth/token/login/";
      this.errors = [];
      if (this.email === "") {
        this.errors.push("The email is missing");
      }
      if (this.password1 === "") {
        this.errors.push("The password is missing");
      }
      try {
        const response = await axios.post(endpoint, {
          email: this.email,
          password: this.password1,
        });
        const token = response.data.auth_token;
        this.$store.commit("setToken", token);
        axios.defaults.headers.common["Authorization"] = "Token " + token;
        localStorage.setItem("token", token);
        console.log(response);
        console.log(token);
        // console.log(response.data.auth_token);
      } catch (error) {
        console.log(error);
        if (error.response) {
          for (const property in error.response.data) {
            this.errors.push(`${property}: ${error.response.data[property]}`);
          }
        } else if (error.message) {
          // this.errors.push("Something went wrong. Please try again");
          console.log(error);
        }
      }
      try {
        const response = await axios.get("auth/users/me/");

        this.$store.commit("setUser", {
          id: response.data.id,
          email: response.data.email,
        });
        localStorage.setItem("email", response.data.email);
        localStorage.setItem("id", response.data.id);

        console.log(response);
      } catch (error) {
        console.log(error);
      }

      try {
        const response = await axios.get("api/v1/teams/get_my_team/");

        this.$store.commit("setTeam", {
          id: response.data.id,
          name: response.data.team_name,
          plan_name: response.data.plan.plan_name,
          max_leads: response.data.plan.max_leads,
          max_clients: response.data.plan.max_clients,
        });

        this.$router.push("/my-account/");

        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>
