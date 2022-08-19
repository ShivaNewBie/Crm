import { createStore } from "vuex";

export default createStore({
  state: {
    isAuthenticated: false,
    token: "",
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("token")) {
        //once we register we used localstorage get item thus running this conditional
        state.token = localStorage.getItem("token");
        state.isAuthenticated = true;
      }
    },
    setToken(state, token) {
      state.token = token;
      isAuthenticated = true;
    },
    removeToken(state) {
      state.token = "";
      isAuthenticated = false;
    },
  },
  actions: {},
  modules: {},
});
