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
        <label>Contact Person</label>
        <input
          v-model="contact_person"
          type="text"
          class="form-control"
          placeholder="Enter contact person"
        />
      </div>
      <div class="form-group">
        <label>Email</label>
        <input
          v-model="email"
          type="email"
          class="form-control"
          placeholder="Enter email"
        />
      </div>
      <div class="form-group">
        <label>Phone</label>
        <input
          v-model="phone"
          type="text"
          class="form-control"
          placeholder="Enter email"
        />
      </div>
      <div class="form-group">
        <label>Website</label>
        <input
          v-model="website"
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
  name: "AddClient",
  data() {
    return {
      name: "",
      contact_person: "",
      email: "",
      phone: "",
      website: "",
    };
  },
  methods: {
    async onSubmit() {
      let endpoint = "/api/v1/clients/";
      const data = {
        name: this.name,
        contact_person: this.contact_person,
        email: this.email,
        phone: this.phone,
        website: this.website,
      };

      try {
        const response = await axios.post(endpoint, data);

        this.$router.push("/clients");
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>
