import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import FirstRoute from '@/components/FirstRoute'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/helloworld',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/firstroute',
      name: 'FirstRoute',
      component: FirstRoute
    }
  ]
})
