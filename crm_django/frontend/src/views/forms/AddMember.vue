<template>
  <div class="container">
    <form @submit.prevent="submitForm">
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
      <div class="form-group">
        <label for="exampleInputPassword2">Password</label>
        <input
          v-model="password2"
          type="password"
          class="form-control"
          id="exampleInputPassword2"
          placeholder="Re-enter password"
        />
      </div>
      <button type="submit" class="btn btn-primary mt-2">Submit</button>
    </form>
    <div class="notification is-danger" v-if="errors.length">
      <!--Check if there are errors -->
      <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
    </div>
  </div>
</template>

<script>
// import { axios } from "@/common/api.service.js";
import axios from "axios";

export default {
  name: "AddMember",
  data() {
    return {
      email: "",
      password1: "",
      password2: "",
      errors: [],
    };
  },
  methods: {
    async submitForm() {
      this.errors = [];
      if (this.email === "") {
        this.errors.push("The email is missing");
      }
      if (this.password1 === "") {
        this.errors.push("The password is missing");
      }
      if (this.password2 === "") {
        this.errors.push("The password is missing");
      }
      let endpoint = "/api/v1/teams/add_member/";
      try {
        const response = await axios.post(endpoint, {
          email: this.email,
          password: this.password1,
        });
        this.$router.push("/teams");
        console.log(response);
      } catch (error) {
        console.log(error);
        if (error.response) {
          for (const property in error.response.data) {
            this.errors.push(`${property}: ${error.response.data[property]}`);
          }
        } else if (error.message) {
          this.errors.push("Something went wrong. Please try again");
        }
      }
    },
  },
};
</script>
