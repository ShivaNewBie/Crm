<template>
  <div class="container">
    <h1 class="title">Update Note</h1>

    <form @submit.prevent="onSubmit">
      <div class="form-group">
        <label>Name</label>
        <input
          v-model="note.name"
          type="text"
          class="form-control"
          placeholder="Enter company name"
        />
      </div>
      <div class="form-group">
        <label>Body</label>
        <textarea
          v-model="note.body"
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
  name: "EditNote",
  data() {
    return {
      note: {},
    };
  },
  props: {
    id: {
      type: String,
      required: true,
    },
    note_id: {
      type: String,
      required: true,
    },
  },
  methods: {
    async onSubmit() {
      let endpoint = `/api/v1/notes/${this.note_id}/?client_id=${this.id}`;

      try {
        const response = await axios.put(endpoint, this.note);

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
  async beforeRouteEnter(to, from, next) {
    // if the component is used to update a question
    // get the lead's data from the REST API
    if (to.params.id !== undefined && to.params.id !== "") {
      const endpoint = `/api/v1/notes/${to.params.note_id}/?client_id=${to.params.id}`;
      try {
        const response = await axios.get(endpoint);
        console.log(response);
        return next((vm) => (vm.note = response.data));
      } catch (error) {
        console.log(error.response);
      }
    } else {
      return next();
    }
  },
};
</script>
