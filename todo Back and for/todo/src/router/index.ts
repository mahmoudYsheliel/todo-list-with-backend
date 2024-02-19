import { createRouter, createWebHashHistory } from "vue-router";
import login from "../views/login.vue";
import notfound from "../views/notfound.vue";
import signup from "../views/signup.vue";
import user from "../views/user.vue";
import lofin_signup from "../views/login_signup.vue";
import { useToken } from "../stateManagement/token";

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "lofin_signup",
      component: lofin_signup,
      meta: { requredAuth: false },
    },
    {
      path: "/login",
      name: "login",
      component: login,
      meta: { requredAuth: false },
    },
    {
      path: "/signup",
      name: "signup",
      component: signup,
      meta: { requredAuth: false },
    },
    {
      path: "/user",
      name: "user",
      component: user,
      meta: { requredAuth: true },
    },
    { path: "/:pathMatch(.*)", name:'notFound',component: notfound },
  ],
});

router.beforeResolve((to, from, next) => {
  if(to.name=='notFound'){
    next()
  }

  const token = useToken();
  let authorized = token.getIsAuthorized;
  console.log(authorized)
  if (to.meta.requredAuth && !authorized) {
    next({ name: "lofin_signup" });
  } else if (!to.meta.requredAuth && authorized) {
    next({ name: "user" });
  } else {
    next();
  }
});

export default router;
