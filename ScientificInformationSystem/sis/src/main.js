import Vue from 'vue'
import App from './App'
import Vuex from 'vuex'
import VueRouer from 'vue-router'
import line from 'components/line/line'
import index from 'components/index/index'
import {DatePicker, Input} from 'element-ui'


Vue.component(DatePicker.name, DatePicker)
Vue.component(Input.name, Input)

Vue.use(VueRouer)
Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    count: 0,
    color: ['#325B69', '#698570', '#AE5548', '#6D9EA8', '#9CC2B0', '#C98769']
  }
});
const router = new VueRouer({
  routes: [{
    path: '/line',
    component: line
  },
  {
    path: '/',
    component: index
  }],
  linkActiveClass: 'active'
})
new Vue({
  router,
  store,
  template: '<App>',
  components: {
    App
  },
  data: {
    eventHub: new Vue(),
    charts: []
  }
}).$mount('#app')

// router.push('line')
