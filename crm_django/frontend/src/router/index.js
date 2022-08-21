import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import EditLead from "../views/forms/EditLead.vue";

import store from "../store";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
    meta: {
      requireLogin: true,
    },
  },
  {
    path: "/register",
    name: "register",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/auth/Register.vue"),
  },
  {
    path: "/login",
    name: "login",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/auth/Login.vue"),
  },
  {
    path: "/my-account",
    name: "my-account",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(
        /* webpackChunkName: "about" */ "../views/dashboard/MyAccount.vue"
      ),
    meta: {
      requireLogin: true,
    },
  },
  {
    path: "/leads",
    name: "leads",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/dashboard/Leads.vue"),
    meta: {
      requireLogin: true,
    },
  },
  {
    path: "/lead/:id",
    name: "lead",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/dashboard/Lead.vue"),
    meta: {
      requireLogin: true,
    },
    props: true,
  },
  {
    path: "/add-lead",
    name: "addlead",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/forms/AddLead.vue"),
    meta: {
      requireLogin: true,
    },
  },
  {
    path: "/edit-lead/:id",
    name: "editlead",
    component: EditLead,
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    meta: {
      requireLogin: true,
    },
    props: true,
  },
  {
    path: "/add-team",
    name: "addteam",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/forms/AddTeam.vue"),
    meta: {
      requireLogin: true,
    },
  },
];

const router = createRouter({
  history: createWebHistory("/"),
  routes,
});

router.beforeEach((to, from, next) => {
  if (
    to.matched.some((record) => record.meta.requireLogin) &&
    !store.state.isAuthenticated
  ) {
    next("/login");
  } else {
    next();
  }
});

export default router;
