<template>
  <nav class="navbar navbar-expand-lg bg-light">
    <div class="container">
      <a class="navbar-brand" href="#">Crm</a>
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link
              to="/"
              class="nav-link active"
              aria-current="page"
              href="#"
              >Home</router-link
            >
          </li>
        </ul>
      </div>
      <template v-if="!$store.state.isAuthenticated">
        <div class="navbar-end">
          <router-link to="/login" class="btn btn-secondary me-2"
            >Log in</router-link
          >
        </div>
        <div class="navbar-end">
          <router-link to="/register" class="btn btn-success"
            >Sign up</router-link
          >
        </div>
      </template>
      <template v-else>
        <div class="navbar-end">
          <router-link :to="{ name: 'clients' }" class="btn btn-secondary me-2">
            Client
          </router-link>
        </div>
        <div class="navbar-end">
          <router-link :to="{ name: 'teams' }" class="btn btn-secondary me-2">
            Team
          </router-link>
        </div>
        <div class="navbar-end">
          <router-link :to="{ name: 'leads' }" class="btn btn-secondary me-2">
            Lead
          </router-link>
        </div>
        <div class="navbar-end">
          <router-link
            :to="{ name: 'myaccount' }"
            class="btn btn-secondary me-2"
          >
            My account
          </router-link>
        </div>
        <div class="navbar-end">
          <button
            @click="emitLogout"
            to="/logout"
            class="btn btn-secondary me-2"
          >
            Log out
          </button>
        </div>
      </template>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
  methods: {
    emitLogout() {
      this.$emit("logout");
    },
  },
};
</script>
