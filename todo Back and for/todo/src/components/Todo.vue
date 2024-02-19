<script setup lang="ts">
import { defineProps, ref } from "vue";
import { useToken } from "../stateManagement/token";
import axios from "axios";

const prop = defineProps(["id", "title", "description",'get_todos']);
const token = useToken();

let accesstoken = token.getToken;

const titileEdit = ref(prop.title);
const descriptionEdit = ref(prop.description);

function rem(id: string) {
  axios
    .post(
      "http://127.0.0.1:8000/delete_todo/",
      { id: id },
      {
        headers: {
          Authorization: `Bearer ${accesstoken}`,
        },
      }
    )
    .then((res) => {
      console.log(res);
      prop.get_todos()
    });
}

async function ed(id: string) {
  axios
    .post("http://127.0.0.1:8000/update_todo/" , {
      id:id,
      new_todo:{title: titileEdit.value,
      description: descriptionEdit.value,}
      
    }, {
        headers: {
          Authorization: `Bearer ${accesstoken}`,
        },
      })
    .then((res) => {
      console.log(res);
      prop.get_todos()
    });
}
</script>

<template>
  <main>
    <input type="text" v-model="titileEdit" />

    <input type="text" v-model="descriptionEdit" />
    <div class="container">
      <button
        @click="
          () => {
            rem(id);
          }
        "
      >
        Remove
      </button>
      <button
        @click="
          () => {
            ed(id);
          }
        "
      >
        Edit
      </button>
    </div>
  </main>
</template>

<style scoped>

.container {
  display: flex;
  justify-content: end;
}
button {
  width: 100px;
  height: 32px;
  color: white;
  background-color: blueviolet;
  border-radius: 8px;
  font-size: 16px;
  text-transform: capitalize;
  cursor: pointer;
  margin-left: 8px;
  font-weight: 500;
  
}
input{
  height: 24px;
  border-radius: 4px;
  width: 200px;
  padding-left: 8px;
  font-size: larger;
  margin-left: 8px;
}
</style>
