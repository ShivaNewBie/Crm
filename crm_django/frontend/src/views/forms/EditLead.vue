<template>
  <div class="container">
    <h1 class="title">Update Lead</h1>

    <form @submit.prevent="onSubmit">
      <div class="form-group">
        <label>Company Name</label>
        <input
          v-model="lead.company_name"
          type="text"
          class="form-control"
          placeholder="Enter company name"
        />
      </div>
      <div class="form-group">
        <label>Contact Person</label>
        <input
          v-model="lead.contact_person"
          type="text"
          class="form-control"
          placeholder="Enter contact person"
        />
      </div>
      <div class="form-group">
        <label>Email</label>
        <input
          v-model="lead.email"
          type="email"
          class="form-control"
          placeholder="Enter email"
        />
      </div>
      <div class="form-group">
        <label>Phone</label>
        <input
          v-model="lead.phone"
          type="text"
          class="form-control"
          placeholder="Enter email"
        />
      </div>
      <div class="form-group">
        <label>Website</label>
        <input
          v-model="lead.website"
          type="text"
          class="form-control"
          placeholder="Enter website name"
        />
      </div>
      <div class="form-group">
        <label>Confidence</label>
        <input
          v-model="lead.confidence"
          type="number"
          class="form-control"
          placeholder="Enter confidence"
        />
      </div>
      <div class="form-group">
        <label>Estimated Value</label>
        <input
          v-model="lead.estimated_value"
          type="number"
          class="form-control"
          placeholder="Enter confidence"
        />
      </div>
      <div class="form-group">
        <label>Status</label>
        <select
          v-model="lead.status"
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
          v-model="lead.priority"
          class="form-select"
          aria-label="Default select example"
        >
          <option selected>Open this select menu</option>
          <option value="low">Low</option>
          <option value="medium">Medium</option>
          <option value="high">High</option>
        </select>
      </div>
      <div class="form-group">
        <label>Assign to</label>
        <select
          v-model="lead.assigned_to.id"
          class="form-select"
          aria-label="Default select example"
        >
          <option value="" selected>Select member</option>
          <option
            v-for="member in team.members"
            v-bind:id="member.id"
            v-bind:value="member.id"
          >
            {{ member.email }}
          </option>
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
  name: "EditLead",
  data() {
    return {
      team: {
        members: [],
      },
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
    async onSubmit() {
      let endpoint = `/api/v1/leads/${this.id}/`;

      try {
        const response = await axios.put(endpoint, this.lead);
        this.$router.push("/leads");
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    // async getLead() {
    //   let endpoint = `/api/v1/leads/${this.id}/`;

    //   try {
    //     const response = await axios.get(endpoint);
    //     this.lead = response.data;
    //     console.log(response);
    //   } catch (error) {
    //     console.log(error);
    //   }
    // },
    async getTeamMembers() {
      let endpoint = "/api/v1/teams/get_my_team/";

      try {
        const response = await axios.get(endpoint);
        this.team = response.data;
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
      const endpoint = `/api/v1/leads/${to.params.id}/`;

      try {
        const response = await axios.get(endpoint);
        console.log(response);
        return next((vm) => (vm.lead = response.data));
      } catch (error) {
        console.log(error.response);
      }
    } else {
      return next();
    }
  },
  created() {
    this.getTeamMembers();
  },
};
</script>
