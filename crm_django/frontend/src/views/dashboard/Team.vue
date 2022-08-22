<template>
  <div class="container">
    <h1 class="title">Team</h1>

    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Name</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="member in team.members" :key="team.id">
          <th scope="row">1</th>
          <td>{{ member.email }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Team",
  data() {
    return {
      team: {
        members: [],
      },
    };
  },
  methods: {
    async getTeamMembers() {
      let endpoint = "/api/v1/teams/get_my_team/";

      try {
        const response = await axios.get(endpoint);
        this.team.members = response.data.members;
      } catch (error) {
        console.log(error);
      }
    },
  },
  created() {
    this.getTeamMembers();
  },
};
</script>
