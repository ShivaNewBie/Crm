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
    },
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("token")) {
        //once we register we used localstorage get item thus running this conditional
        state.token = localStorage.getItem("token");
        state.isAuthenticated = true;
        state.user.email = localStorage.getItem("email");
        state.user.id = localStorage.getItem("id");
        state.team.name = localStorage.getItem("team_name");
        state.team.id = localStorage.getItem("team_id");
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
    },
  },
  actions: {},
  modules: {},
});
