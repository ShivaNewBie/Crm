<template>
  <div class="container">
    <h1 class="title">Add Team</h1>
    <form @submit.prevent="onSubmit">
      <div class="form-group">
        <label>Team Name</label>
        <input
          v-model="team_name"
          type="text"
          class="form-control"
          placeholder="Enter Team Name"
        />
      </div>

      <button type="submit" class="btn btn-primary mt-2">Submit</button>
    </form>
  </div>
</template>

<script>
import { axios } from "@/common/api.service.js";

export default {
  name: "AddTeam",
  data() {
    return {
      team_name: "",
    };
  },
  methods: {
    async onSubmit() {
      let endpoint = "/api/v1/teams/";

      try {
        const response = await axios.post(endpoint, {
          team_name: this.team_name,
        });
        this.$store.commit("setTeam", {
          id: response.data.id,
          name: response.data.team_name,
        });
        console.log(response);
        this.$router.push("/");
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>
