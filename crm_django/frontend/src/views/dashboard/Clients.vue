<template>
  <div class="container">
    <h1 class="title">Clients</h1>
    <router-link :to="{ name: 'addclient' }" class="btn btn-success"
      >Add Client
    </router-link>
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
    };
  },
  methods: {
    async getClients() {
      let endpoint = "/api/v1/clients/";
      this.loadingClients = true;
      try {
        const response = await axios.get(endpoint);
        this.clients = response.data;
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
