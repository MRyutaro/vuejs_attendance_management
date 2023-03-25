import Vue from 'vue';
import Router from 'vue-router';
import Login from '../pages/Login.vue';
import Frontend from '../pages/loginok.vue';
import Store from '@/store/index.js';

Vue.use(Router);

const routes = [
  {
    name: 'Login',
    path: '/login',
    component: Login,
  },
  {
    name: 'loginok',
    path: '/',
    component: Frontend,
    meta: { requiresAuth: true },
  },
];

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, next) => {
  if (
    to.matched.some((record) => record.meta.requiresAuth) &&
    !Store.state.userToken
  ) {
    next({ path: '/loginok', query: { redirect: to.fullPath } });
  } else {
    next();
  }
});

export default router;
