<script lang="ts" setup>
import {useToken} from '../stateManagement/token'
import { ref } from "vue";
import axios from "axios";
import {useRouter} from 'vue-router'

const name = ref();
const pass = ref();
const router =useRouter()

const token =useToken()
function login() {
  axios
    .post("http://127.0.0.1:8000/token", `grant_type=&username=${name.value}&password=${pass.value}&scope=&client_id=&client_secret=`)
    .then((res) => {
        console.log(res)
     if (res.data['access_token']){
        token.addToken(res.data['access_token'])
        router.push('user')
     }
     else{
        router.push('notfound')
     }
    });
}
</script>

<template>
 <main>
    <div class="container">
      <input
        v-model="name"
        type="text"
        name="username"
        id="username"
        placeholder="username"
      />
      <input
        v-model="pass"
        type="text"
        name="password"
        id="password"
        placeholder="password"
      />

      <button @click="login">signup</button>
    </div>
  </main>
</template>

<style scoped>
input{
  width: 300px;
  height: 50px;
  border-radius: 8px;
  font-size: 24px;
}
button {
  width: 200px;
  height: 50px;
  color: white;
  background-color: blueviolet;
  border-radius: 8px;
  font-size: 24px;
  text-transform: capitalize;
  cursor: pointer;
}
.container {
  display: flex;
  flex-direction: column;
  margin: auto;
  width: fit-content;
  padding-top: 100px;
  gap: 24px;
  align-items: center;
}</style>
