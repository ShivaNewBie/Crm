<template>
  <div class="container">
    <h1 class="title">Edit Member</h1>

    <form @submit.prevent="onSubmit">
      <div class="form-group">
        <label>First Name</label>
        <input
          v-model="user.first_name"
          type="text"
          class="form-control"
          placeholder="Enter first name"
        />
      </div>
      <div class="form-group">
        <label>Last Name</label>
        <input
          v-model="user.last_name"
          type="text"
          class="form-control"
          placeholder="Enter last name"
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
  name: "AddNote",
  data() {
    return {
      user: {},
    };
  },
  props: {
    id: {
      type: String,
      required: true,
    },
  },
  methods: {
    async onSubmit() {
      let endpoint = `/api/v1/teams/member/${this.id}/`;

      try {
        const response = await axios.put(endpoint, this.user);

        this.$router.push({
          name: "myaccount",
        });
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
  },
  async beforeRouteEnter(to, from, next) {
    // if the component is used to update a question
    // get the lead's data from the REST API
    if (to.params.id !== undefined && to.params.id !== "") {
      const endpoint = `/api/v1/teams/member/${to.params.id}/`;
      try {
        const response = await axios.get(endpoint);
        console.log(response);
        return next((vm) => (vm.user = response.data));
      } catch (error) {
        console.log(error.response);
      }
    } else {
      return next();
    }
  },
};
</script>
