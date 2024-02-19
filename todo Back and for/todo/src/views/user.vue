<script setup lang="ts">
import Todo from "../components/Todo.vue";
import axios from "axios";
import { ref } from "vue";
import { useToken } from "../stateManagement/token";
import router from "../router";

interface todo {
  title: string;
  description: string;
  id: string;
}

const token = useToken();

const todos = ref<todo[]>();

let accesstoken = token.getToken;
const get_todos = async () => {
  axios
    .post(
      "http://127.0.0.1:8000/get_todos",
      {},
      {
        headers: {
          Authorization: `Bearer ${accesstoken}`,
        },
      }
    )
    .then((res) => {
      todos.value = res.data.data.todos;
    });
};

get_todos();
const title = ref();
const des = ref();
function post() {
  console.log({ title: title.value, description: des.value });
  axios
    .post(
      "http://127.0.0.1:8000/create_todo/",
      {
        new_todo: {
          title: title.value,
          description: des.value,
        },
      },
      {
        headers: {
          Authorization: `Bearer ${accesstoken}`,
        },
      }
    )
    .then((res) => {
      console.log(res);
      get_todos();
      title.value = "";
      des.value = "";
    });
}
function logout(){
  token.logout()
  router.push('/signup')
}
</script>

<template>
  <main>
    <button @click="logout" style="transform: translate(-20px,20px);">Logout</button>
    <div class="contain">
      <h2 class="title">To Do List With Backend</h2>
      <div class="container">
        <div class="add">
          <div class="wraper">
            <input type="text" placeholder="title" v-model="title" />
            <input type="text" placeholder="descroption" v-model="des" />
          </div>
          <button @click="post">ADD</button>
        </div>
        <div class="todos">
          <Todo
            v-for="todo in todos"
            :title="todo.title"
            :description="todo.description"
            :id="todo.id"
            :get_todos="get_todos"
          />
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped>
.contain{
  width: 800px;
  margin: auto;
  padding-top: 100px;
}
.wraper {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-block: 16px 8px;
}
.wraper > * {
  font-size: 16px;
}
input::placeholder {
  opacity: 0.75;
}

.todos {
  padding-top: 24px;
  display: flex;
  flex-direction: column;
}
input{
  width: 500px;
  height: 24px;
  border-radius: 8px;
  font-size: 24px;
  padding-left: 8px;
}
button{
  display: block;
  width: 100px;
  height: 32px;
  color: white;
  background-color: blueviolet;
  border-radius: 8px;
  font-size: 24px;
  text-transform: capitalize;
  cursor: pointer;
  margin-left: auto;
}
</style>
