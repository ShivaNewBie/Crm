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
import { axios } from "@/common/api.service.js";
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
        this.$router.push("/");
        console.log(response);
        console.log(token);
        // console.log(response.data.auth_token);
      } catch (error) {
        if (error.response) {
          for (const property in error.response.data) {
            this.errors.push(`${property}: ${error.response.data[property]}`);
          }
        } else if (error.message) {
          // this.errors.push("Something went wrong. Please try again");
          console.log(error);
        }
      }
    },
  },
};
</script>
