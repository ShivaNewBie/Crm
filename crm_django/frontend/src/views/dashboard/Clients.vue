<template>
  <div class="container">
    <h1 class="title">Clients</h1>
    <router-link
      v-if="$store.state.team.max_clients > num_clients"
      :to="{ name: 'addclient' }"
      class="btn btn-success"
      >Add Client
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
    <template v-if="clients.length">
      <table class="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th s cope="col">Name</th>
            <th scope="col">Contact person</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="client in clients" :key="client.id">
            <th scope="row">1</th>
            <td>{{ client.name }}</td>

            <td>{{ client.contact_person }}</td>
            <td>
              <router-link :to="{ name: 'client', params: { id: client.id } }"
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
    </template>
    <template v-else>
      <p>No clients yet</p>
    </template>
  </div>
</template>

<script>
// import { axios } from "@/common/api.service.js";
import axios from "axios";
export default {
  name: "Clients",
  data() {
    return {
      clients: [],
      loadingClients: false,
      nextButton: false,
      previousButton: false,
      currentPage: 1,
      query: "",
      num_clients: 0,
    };
  },
  methods: {
    onSubmit() {
      this.getClients();
    },
    nextPage() {
      this.currentPage += 1;
      this.getClients();
    },
    prevPage() {
      this.currentPage -= 1;
      this.getClients();
    },
    async getClients() {
      this.nextButton = false;
      this.previousButton = false;
      let endpoint = `/api/v1/clients/?page=${this.currentPage}&search=${this.query}`;
      this.loadingClients = true;
      try {
        const response = await axios.get("/api/v1/clients/");
        this.num_clients = response.data.count;
        console.log(response);
      } catch (error) {
        console.log(error);
      }
      try {
        const response = await axios.get(endpoint);
        this.clients = response.data.results;
        console.log(response);

        this.loadingClients = false;
      } catch (error) {
        console.log(error);
      }
    },
  },
  created() {
    this.getClients();
  },
};
</script>
