<template>
  <div class="container">
    <h1 class="title">Update Client</h1>

    <form @submit.prevent="onSubmit">
      <div class="form-group">
        <label>Company Name</label>
        <input
          v-model="client.name"
          type="text"
          class="form-control"
          placeholder="Enter company name"
        />
      </div>
      <div class="form-group">
        <label>Contact Person</label>
        <input
          v-model="client.contact_person"
          type="text"
          class="form-control"
          placeholder="Enter contact person"
        />
      </div>
      <div class="form-group">
        <label>Email</label>
        <input
          v-model="client.email"
          type="email"
          class="form-control"
          placeholder="Enter email"
        />
      </div>
      <div class="form-group">
        <label>Phone</label>
        <input
          v-model="client.phone"
          type="text"
          class="form-control"
          placeholder="Enter email"
        />
      </div>
      <div class="form-group">
        <label>Website</label>
        <input
          v-model="client.website"
          type="text"
          class="form-control"
          placeholder="Enter website name"
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
  name: "EditClient",
  data() {
    return {
      client: {},
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
      let endpoint = `/api/v1/client/${this.id}/`;

      try {
        const response = await axios.put(endpoint, this.client);

        this.$router.push("/clients");
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
      const endpoint = `/api/v1/clients/${to.params.id}/`;
      try {
        const response = await axios.get(endpoint);
        return next((vm) => (vm.client = response.data));
      } catch (error) {
        console.log(error.response);
      }
    } else {
      return next();
    }
  },
  created() {},
};
</script>
