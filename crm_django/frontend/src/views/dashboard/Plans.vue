<template>
  <div class="container">
    <h1 class="title">Plans</h1>
    <div class="row">
      <div class="col">
        <div class="card-body">
          <h5 class="card-title">Free</h5>
          <h6 class="card-subtitle mb-2 text-muted">0$</h6>
          <p class="card-text">Free Subscription</p>
          <p>Max 5 clients</p>
          <p>Max 5 leads</p>

          <button @click="subscribe('free')" class="btn btn-primary">
            Subscribe
          </button>
        </div>
      </div>
      <div class="col">
        <div class="card-body">
          <h5 class="card-title">Small team</h5>
          <h6 class="card-subtitle mb-2 text-muted">$10</h6>
          <p class="card-text">Start-up subscription</p>
          <p>Max 15 clients</p>
          <p>Max 15 leads</p>
          <button @click="subscribe('smallteam')" class="btn btn-primary">
            Subscribe
          </button>
        </div>
      </div>
      <div class="col">
        <div class="card-body">
          <h5 class="card-title">Big team</h5>
          <h6 class="card-subtitle mb-2 text-muted">$25</h6>
          <p class="card-text">Enterprise subscription</p>
          <p>Max 50 clients</p>
          <p>Max 50 leads</p>
          <button @click="subscribe('bigteam')" class="btn btn-primary">
            Subscribe
          </button>
        </div>
      </div>
      <hr />
      <div>
        <button @click="cancelPlan()" class="btn btn-danger">
          Cancel Plan
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Plans",
  data() {
    return {
      pub_key: "",
      stripe: null,
    };
  },
  async created() {
    await this.getPubKey();
    this.stripe = Stripe(this.pub_key);
  },
  methods: {
    async getPubKey() {
      try {
        const response = await axios.get("/api/v1/stripe/get_stripe_pub_key/");

        this.pub_key = response.data.pub_key;
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async cancelPlan() {
      let endpoint = "/api/v1/teams/cancel_plan/";

      try {
        const response = await axios.post(endpoint);

        console.log(response);
        this.$store.commit("setTeam", {
          id: response.data.id,
          name: response.data.team_name,
          plan_name: response.data.plan.plan_name,
          max_leads: response.data.plan.max_leads,
          max_clients: response.data.plan.max_clients,
        });
        this.$router.push({ name: "teams" });
      } catch (error) {
        console.log(error);
      }
    },
    async subscribe(plan_name) {
      this.loadingLeads = true;
      const data = {
        plan_name: plan_name,
      };

      try {
        const response = await axios.post(
          "/api/v1/stripe/create_checkout_session/",
          data
        );
        console.log(response);

        return this.stripe.redirectToCheckout({
          sessionId: response.data.sessionId,
        });
      } catch (error) {
        console.log(error);
      }
      //   try {
      //     const response = await axios.post(endpoint, data);
      //     this.$store.commit("setTeam", {
      //       id: response.data.id,
      //       name: response.data.team_name,
      //       plan_name: response.data.plan.plan_name,
      //       max_leads: response.data.plan.max_leads,
      //       max_clients: response.data.plan.max_clients,
      //     });
      //     this.$router.push("/teams");

      //     console.log(response);
      //     console.log("upgrade");
      //   } catch (error) {
      //     console.log(error);
      //   }
    },
  },
};
</script>
