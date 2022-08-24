<template>
  <div class="container">
    <h1 class="title">{{ lead.company_name }}</h1>
    <router-link :to="{ name: 'editlead' }" class="btn btn-success"
      >Edit lead
    </router-link>
    <button @click="convertToClient" class="btn btn-success">
      Convert to client
    </button>
    <div class="row gx-5">
      <div class="col">
        <div class="shadow p-3 mb-5 bg-body rounded">
          <h2><strong>Contact Information:</strong></h2>
          <h4><strong>Contact person: </strong> {{ lead.contact_person }}</h4>
          <h4><strong>Email: </strong> {{ lead.email }}</h4>
          <h4><strong>Phone: </strong> {{ lead.phone }}</h4>
          <h4><strong>Website: </strong> {{ lead.website }}</h4>
        </div>
      </div>
      <div class="col">
        <div class="shadow p-3 mb-5 bg-body rounded">
          <h2><strong>Details:</strong></h2>

          <h4><strong>Confidence: </strong> {{ lead.confidence }}</h4>
          <h4><strong>Estimated_value: </strong> {{ lead.estimated_value }}</h4>
          <h4><strong>Status: </strong> {{ lead.status }}</h4>
          <h4><strong>Priority: </strong> {{ lead.priority }}</h4>
          <h4>
            <strong>Assigned to: </strong>
            <template v-if="lead.assigned_to">{{
              lead.assigned_to.email
            }}</template>
          </h4>

          <h4><strong>Created_by: </strong> {{ lead.created_by }}</h4>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import { axios } from "@/common/api.service.js";
import axios from "axios";
export default {
  name: "Lead",
  data() {
    return {
      lead: {
        assigned_to: {},
      },
    };
  },
  props: {
    id: {
      type: String,
      required: true,
    },
  },
  methods: {
    async getLead() {
      let endpoint = `/api/v1/leads/${this.id}/`;

      try {
        const response = await axios.get(endpoint);
        this.lead = response.data;
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async convertToClient() {
      let endpoint = `/api/v1/convert_lead_to_client/`;
      const data = {
        lead_id: this.id,
      };
      try {
        const response = await axios.post(endpoint, data);
        console.log(response);

        this.$router.push("/clients");
      } catch (error) {
        console.log(error);
      }
    },
  },
  created() {
    this.getLead();
  },
};
</script>
