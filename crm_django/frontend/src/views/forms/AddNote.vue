<template>
  <div class="container">
    <h1 class="title">Add Client</h1>

    <form @submit.prevent="onSubmit">
      <div class="form-group">
        <label>Name</label>
        <input
          v-model="name"
          type="text"
          class="form-control"
          placeholder="Enter company name"
        />
      </div>
      <div class="form-group">
        <label>Body</label>
        <textarea
          v-model="body"
          type="text"
          class="form-control"
          placeholder="Enter body"
          rows="5"
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
      name: "",
      body: "",
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
      let endpoint = "/api/v1/notes/";
      const data = {
        name: this.name,
        body: this.body,
        client_id: this.id,
      };

      try {
        const response = await axios.post(endpoint, data);

        this.$router.push({
          name: "client",
          params: { id: this.id },
        });
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>
