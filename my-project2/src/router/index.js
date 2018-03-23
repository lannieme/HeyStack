import Vue from 'vue'
import Router from 'vue-router'
import AppNav from '../assets/AppNav.vue'
import PastConvo from '../assets/PastConvo.vue'
import Convo from '../assets/Conversation.vue'
import FirstRoute from '../components/FirstRoute.vue'
import Home from '../components/Home.vue'
Vue.use(Router)
export default new Router({
  routes: [
  	{
      path: '/',
      name: 'default',
      component: Home
    },
    {
      path: '/home',
      name: 'home',
      component: Home
    },
    {
      path: '/convo',
      name: 'convo',
      component: Convo
    },
    {
      path: '/firstroute',
      name: 'FirstRoute',
      component: FirstRoute
    }
  ]
})
