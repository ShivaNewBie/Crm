<template>
  <div class="container">
    <h1 class="title">Leads</h1>
    <router-link :to="{ name: 'addlead' }" class="btn btn-success"
      >Add Lead
    </router-link>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th s cope="col">Company</th>
          <th scope="col">Contact person</th>
          <th scope="col">Assigned to</th>

          <th scope="col">Status</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="lead in leads" :key="lead.id">
          <th scope="row">1</th>
          <td>{{ lead.company_name }}</td>

          <td>{{ lead.contact_person }}</td>
          <td>{{ lead.assigned_to.email }}</td>

          <td>{{ lead.status }}</td>
          <td>
            <router-link :to="{ name: 'lead', params: { id: lead.id } }"
              >View</router-link
            >
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
// import { axios } from "@/common/api.service.js";
import axios from "axios";
export default {
  name: "Leads",
  data() {
    return {
      leads: [],
      loadingLeads: false,
    };
  },
  methods: {
    async getLeads() {
      let endpoint = "/api/v1/leads/";
      this.loadingLeads = true;
      try {
        const response = await axios.get(endpoint);
        this.leads = response.data;
        console.log(response);

        this.loadingLeads = false;
      } catch (error) {
        console.log(error);
      }
    },
  },
  created() {
    this.getLeads();
  },
};
</script>
