import Vue from 'vue'
import App from './App'
import Vuex from 'vuex'
import VueRouer from 'vue-router'
import line from 'components/line/line'
import index from 'components/index/index'
import personalInfo from 'components/personalInfo/personalInfo'
import search from 'components/search/search'
import interpersonalRelationshipNetwork from 'components/dataVisualization/interpersonalRelationshipNetwork'
import paper from 'components/paper/paper'


import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(VueRouer)
Vue.use(Vuex)
Vue.use(ElementUI);

const store = new Vuex.Store({
  state: {  
    count: 0,
    color: ['#325B69', '#698570', '#AE5548', '#6D9EA8', '#9CC2B0', '#C98769']
  }
});
const router = new VueRouer({
  mode: 'history',
  routes: [{
    path: '/line',
    component: line
  },{
    path: '/search',
    component: search
  },{
    path: '/interpersonalRelationshipNetwork',
    component: interpersonalRelationshipNetwork
  },{
    path: '/personalInfo',
    component: personalInfo
  },{
    path: '/paper',
    component: paper
  },{
    path: '/',
    component: index
  }],
  linkActiveClass: 'active'
})
new Vue({
  router,
  store,
  template: '<App/>',
  components: {
    App
  },
  data: {
    eventHub: new Vue(),
    charts: []
  }
}).$mount('#app')

// router.push('line')
