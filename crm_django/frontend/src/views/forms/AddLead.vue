<template>
  <div class="container">
    <h1 class="title">Leads</h1>

    <form @submit.prevent="onSubmit">
      <div class="form-group">
        <label>Company Name</label>
        <input
          v-model="company_name"
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
      <div class="form-group">
        <label>Confidence</label>
        <input
          v-model="confidence"
          type="number"
          class="form-control"
          placeholder="Enter confidence"
        />
      </div>
      <div class="form-group">
        <label>Estimated Value</label>
        <input
          v-model="estimated_value"
          type="number"
          class="form-control"
          placeholder="Enter confidence"
        />
      </div>
      <div class="form-group">
        <label>Status</label>
        <select
          v-model="status"
          class="form-select"
          aria-label="Default select example"
        >
          <option selected>Open this select menu</option>
          <option value="new">New</option>
          <option value="contacted">Contacted</option>
          <option value="inprogress">In progress</option>
          <option value="lost">Lost</option>
          <option value="won">Won</option>
        </select>
      </div>
      <div class="form-group">
        <label>Priority</label>
        <select
          v-model="priority"
          class="form-select"
          aria-label="Default select example"
        >
          <option selected>Open this select menu</option>
          <option value="low">Low</option>
          <option value="medium">Medium</option>
          <option value="high">High</option>
        </select>
      </div>

      <button type="submit" class="btn btn-primary mt-2">Submit</button>
    </form>
  </div>
</template>

<script>
// import { axios } from "@/common/api.service.js";
import axios from "axios";
export default {
  name: "AddLead",
  data() {
    return {
      company_name: "",
      contact_person: "",
      email: "",
      phone: "",
      website: "",
      confidence: 0,
      estimated_value: 0,
      status: "new",
      priority: "medium",
    };
  },
  methods: {
    async onSubmit() {
      let endpoint = "/api/v1/leads/";
      const data = {
        company_name: this.company_name,
        contact_person: this.contact_person,
        email: this.email,
        phone: this.phone,
        website: this.website,
        confidence: this.confidence,
        estimated_value: this.estimated_value,
        status: this.status,
        priority: this.priority,
      };

      try {
        const response = await axios.post(endpoint, data);

        this.$router.push("/leads");
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>
