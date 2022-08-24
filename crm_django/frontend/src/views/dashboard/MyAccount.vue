<template>
  <div class="container">
    <h1 class="title">My account</h1>
    <router-link
      :to="{ name: 'editaccount', params: { id: this.$store.state.user.id } }"
      class="btn btn-success"
      >Edit Account
    </router-link>
  </div>
</template>

<script>
export default {
  name: "MyAccount",
  props: {
    id: {
      type: String,
    },
  },
};
</script>
