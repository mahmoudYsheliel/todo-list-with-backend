import { defineStore } from "pinia";

export const useToken = defineStore("token", {
  state: () => ({
    token: null as string | null,
    isAuthorized:false
  }),
  actions: {
    addToken(token: string) {
      this.token = token;
      this.isAuthorized=true
      this.saveToLocalStorage();
    },
    saveToLocalStorage() {
      localStorage.setItem("token", JSON.stringify(this.token));
      localStorage.setItem("isAuthorized", JSON.stringify(this.isAuthorized));
    },
    logout(){
      this.token=null
      this.isAuthorized=false
      localStorage.clear()
    }
  },
  getters: {
    getToken(state) {
      const data = localStorage.getItem("token");

      if (data) {
        this.token = JSON.parse(data);
      }
      return state.token;
    },
    getIsAuthorized(state){
      const data =localStorage.getItem('isAuthorized')
      if (data!=null){
        this.isAuthorized=JSON.parse(data)
      }
      return state.isAuthorized
    }
  },

});
