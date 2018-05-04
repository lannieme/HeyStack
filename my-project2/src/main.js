import Vue from 'vue'
import BootstrapVue from "bootstrap-vue"
import App from './App.vue'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-vue/dist/bootstrap-vue.css"
import router from './router'
import VueChatScroll from 'vue-chat-scroll'
import VTooltip from 'v-tooltip'
import Vuetify from 'vuetify'
import Delay from 'vue-delay'

Vue.use(Vuetify)
Vue.use(Delay)

Vue.use(VTooltip)
Vue.use(VueChatScroll)
Vue.use(BootstrapVue)

// new Vue({
//   el: '#app',
//   render: h => h(App)
// })
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
