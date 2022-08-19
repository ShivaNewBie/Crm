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
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
};
</script>
