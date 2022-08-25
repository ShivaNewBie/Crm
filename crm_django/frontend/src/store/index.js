import { createStore } from "vuex";

export default createStore({
  state: {
    isAuthenticated: false,
    token: "",
    user: {
      id: 0,
      email: "",
    },
    team: {
      id: 0,
      name: "",
      plan_name: "",
      max_leads: 0,
      max_clients: 0,
    },
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("token")) {
        //once we login we used localstorage get item thus running this conditional
        state.token = localStorage.getItem("token");
        state.isAuthenticated = true;
        state.user.email = localStorage.getItem("email");
        state.user.id = localStorage.getItem("id");
        state.team.id = localStorage.getItem("team_id");
        state.team.name = localStorage.getItem("team_name");
        state.team.plan_name = localStorage.getItem("team_plan_name");
        state.team.max_clients = localStorage.getItem("team_max_clients");
        state.team.max_leads = localStorage.getItem("team_max_leads");
      } else {
        state.token = "";
        state.isAuthenticated = false;
        state.user.id = 0;
        state.user.username = "";
        state.team.id = 0;
        state.team.name = "";
        state.team.plan_name = "";
        state.team.max_leads = 0;
        state.team.max_clients = 0;
      }
    },
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = "";
      state.isAuthenticated = false;
    },
    setUser(state, user) {
      state.user = user;
    },
    setTeam(state, team) {
      state.team = team;

      localStorage.setItem("team_id", team.id);
      localStorage.setItem("team_name", team.name);
      localStorage.setItem("team_plan_name", team.plan_name);
      localStorage.setItem("team_max_clients", team.max_clients);
      localStorage.setItem("team_max_leads", team.max_leads);
    },
  },
  actions: {},
  modules: {},
});
