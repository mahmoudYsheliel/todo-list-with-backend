<script lang="ts" setup>
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const name = ref();
const pass = ref();
const confirmPass =ref()
const router = useRouter();
const showError =ref(false)

function login() {
  if (pass.value==confirmPass.value && pass.value!=''){
    axios
    .post("http://127.0.0.1:8000/login", {
      user: {
        username: name.value,
        password: pass.value,
      },
    })
    .then((res) => {
      if (res.data) {
        router.push("/signup");
      }else{
      router.push("/notfound");
      }
    });
  }else{
    showError.value=true
  }

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
        @change="showError=false"
      />
      <input
        v-model="confirmPass"
        type="text"
        name="confirm password"
        id="confirm password"
        placeholder="confirm password"
        @change="showError=false"
      />
      <button @click="login">login</button>
      <p v-if="confirmPass!=pass && showError" >password don't match</p>
      <p v-if="confirmPass==pass && pass=='' && showError">empty password not allowed</p>
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
}
</style>
