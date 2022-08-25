<template>
  <div class="container">
    <h1 class="title">Leads</h1>
    <router-link
      v-if="$store.state.team.max_leads > num_leads"
      :to="{ name: 'addlead' }"
      class="btn btn-success"
      >Add Lead
    </router-link>
    <div v-else>You have reached your plan limitations!</div>
    <hr />
    <form @submit.prevent="onSubmit">
      <div class="input-group mb-3">
        <input
          v-model="query"
          type="text"
          class="form-control"
          placeholder="Search"
          aria-label="Search"
          aria-describedby="basic-addon2"
        />
        <div class="input-group-append">
          <button class="btn btn-outline-secondary">Submit</button>
        </div>
      </div>
    </form>
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
          <td>
            <template v-if="lead.assigned_to">
              {{ lead.assigned_to.first_name }} {{ lead.assigned_to.last_name }}
            </template>
          </td>

          <td>{{ lead.status }}</td>
          <td>
            <router-link :to="{ name: 'lead', params: { id: lead.id } }"
              >View</router-link
            >
          </td>
        </tr>
      </tbody>
    </table>
    <div class="buttons">
      <button
        @click="prevPage()"
        v-if="previousButton"
        type="button"
        class="btn btn-light"
      >
        Previous
      </button>
      <button
        v-if="nextButton"
        @click="nextPage()"
        type="button"
        class="btn btn-light"
      >
        Next
      </button>
    </div>
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
      nextButton: false,
      previousButton: false,
      currentPage: 1,
      query: "",
      num_leads: 0,
    };
  },
  methods: {
    onSubmit() {
      this.getLeads();
    },
    nextPage() {
      this.currentPage += 1;
      this.getLeads();
    },
    prevPage() {
      this.currentPage -= 1;
      this.getLeads();
    },
    async getLeads() {
      this.nextButton = false;
      this.previousButton = false;
      let endpoint = `/api/v1/leads/?page=${this.currentPage}&search=${this.query}`; //search passed param
      this.loadingLeads = true;

      try {
        const response = await axios.get("api/v1/leads/");
        this.num_leads = response.data.count;

        console.log(response);
      } catch (error) {
        console.log(error);
      }

      try {
        const response = await axios.get(endpoint);
        this.leads = response.data.results;

        if (response.data.next) {
          this.nextButton = true;
        }
        if (response.data.previous) {
          this.previousButton = true;
        }
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
