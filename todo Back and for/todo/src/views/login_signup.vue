<script lang="ts" setup>
import { useRouter } from "vue-router";

const router = useRouter();

function login() {
  router.push("/login");
}

function signup() {
  router.push("/signup");
}
</script>

<template>
  <main>
    <div class="container">
      <button @click="login">login</button>
      <button @click="signup">signup</button>
    </div>
  </main>
</template>

<style scoped>
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
  flex-direction: row;
  margin: auto;
  width: fit-content;
  padding-top: 100px;
  gap: 24px;
}
</style>
