<template>
  <div class="container">
    <h1 class="title">Team</h1>

    <template v-if="team.created_by.id === parseInt($store.state.user.id)">
      <router-link :to="{ name: 'addmember' }" class="btn btn-success"
        >Add Member
      </router-link>
    </template>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Email</th>
          <th scope="col">Full name</th>

          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="member in team.members" :key="team.id">
          <th scope="row">1</th>
          <td>{{ member.email }}</td>
          <td>{{ member.first_name }} {{ member.last_name }}</td>
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
        created_by: {},
      },
    };
  },
  methods: {
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
  created() {
    this.getTeamMembers();
  },
};
</script>
