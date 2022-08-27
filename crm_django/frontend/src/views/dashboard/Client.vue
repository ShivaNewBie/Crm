<template>
  <div class="container">
    <h1 class="title">{{ client.name }}</h1>
    <router-link :to="{ name: 'editclient' }" class="btn btn-success"
      >Edit Client
    </router-link>
    <button @click="deleteClient" class="btn btn-danger">Delete Client</button>

    <div class="row gx-5">
      <div class="col">
        <div class="shadow p-3 mb-5 bg-body rounded">
          <h2><strong>Contact Information:</strong></h2>
          <h4><strong>Contact person: </strong> {{ client.contact_person }}</h4>
          <h4><strong>Email: </strong> {{ client.email }}</h4>
          <h4><strong>Phone: </strong> {{ client.phone }}</h4>
          <h4><strong>Website: </strong> {{ client.website }}</h4>
        </div>
      </div>
      <div class="col">
        <div class="shadow p-3 mb-5 bg-body rounded">
          <h2><strong>Details:</strong></h2>

          <h4><strong>Created at: </strong> {{ client.created_at }}</h4>
          <h4><strong>Updated at: </strong> {{ client.updated_at }}</h4>
        </div>
      </div>
    </div>
    <hr />
  </div>

  <div class="container">
    <h2>Notes</h2>
    <router-link :to="{ name: 'addnote' }" class="btn btn-success"
      >Add note
    </router-link>

    <div class="" v-for="note in notes" v-bind:key="note.id">
      <h3>{{ note.name }}</h3>
      <p>{{ note.body }}</p>
      <router-link
        :to="{ name: 'editnote', params: { id: client.id, note_id: note.id } }"
        class="btn btn-success"
        >Edit note
      </router-link>
    </div>
  </div>
</template>

<script>
// import { axios } from "@/common/api.service.js";
import axios from "axios";
export default {
  name: "Client",
  data() {
    return {
      client: {},
      notes: [],
    };
  },
  props: {
    id: {
      type: String,
      required: true,
    },
  },
  methods: {
    async deleteClient() {
      let endpoint = `/api/v1/clients/delete_client/${this.id}/`;

      try {
        const response = await axios.post(endpoint);
        this.$router.push("/clients");

        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async getClient() {
      let endpoint = `/api/v1/clients/${this.id}/`;

      try {
        const response = await axios.get(endpoint);
        this.client = response.data;
        console.log(response);
      } catch (error) {
        console.log(error);
      }
      try {
        const response = await axios.get(`/api/v1/notes/?client_id=${this.id}`);

        this.notes = response.data;
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
  },
  created() {
    this.getClient();
  },
};
</script>
