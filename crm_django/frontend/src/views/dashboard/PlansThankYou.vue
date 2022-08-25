<template>
  <div class="container">
    <h1 class="title">Thank you for subscribing</h1>

    <div v-if="changePlan"><h1>Plan changed</h1></div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "PlansThankYou",
  data() {
    return {
      changePlan: false,
    };
  },
  async created() {
    try {
      const response = await axios.post("/api/v1/stripe/check_session/", {
        session_id: this.$route.query.session_id,
      });
      this.changePlan = true;
      console.log(response);

      this.$store.commit("setTeam", {
        id: response.data.id,
        name: response.data.team_name,
        plan_name: response.data.plan.plan_name,
        max_leads: response.data.plan.max_leads,
        max_clients: response.data.plan.max_clients,
      });
    } catch (error) {
      console.log(error);
    }
  },
};
</script>
