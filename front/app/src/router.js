import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Search from "./views/Search.vue";
import Mixins from "./views/Mixins.vue";
import Tables from "./views/Tables.vue";
import UserHello from "./views/UserHello.vue";
import SelectTopics from "./views/SelectTopics.vue";
import SelectBooks from "./views/SelectBooks.vue";
import Evaluation from "./views/Evaluation.vue";
import End from "./views/End.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/search",
      name: "search",
      component: Search
    },
    {
      path: "/select_topics",
      name: "selectTopics",
      component: SelectTopics,
    },
    {
      path: "/select_books",
      name: "selectBooks",
      component: SelectBooks,
    },
    {
      path: "/evaluation",
      name: "evaluation",
      component: Evaluation,
    },
    {
      path: "/end",
      name: "end",
      component: End,
    },
    {
      path: "/hello",
      name: "userhello",
      component: UserHello
    },
    {
      path: "/mixtest",
      name: "mixtest",
      component: Mixins
    },
    {
      path: "/tables",
      name: "tables",
      component: Tables
    }
  ]
});
