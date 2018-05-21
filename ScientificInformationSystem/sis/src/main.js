import Vue from 'vue'
import App from './App'
import Vuex from 'vuex'
import VueRouer from 'vue-router'
import index from 'components/index/index'
import personalInfo from 'components/personalInfo/personalInfo'
import search from 'components/search/search'
import searchJournal from 'components/search/searchJournal.vue'
import journalInfo from 'components/journal/index.vue'
import journalPaper from 'components/journal/journalpaper.vue'
import journalPublishEveryYear from 'components/journal/journalPublishEveryYear.vue'
import journalKeyWord from 'components/journal/journalKeyWord.vue'
import journalAuthorRank from 'components/journal/journalAuthorRank.vue'
import organizationInfo from 'components/organization/index.vue'
import organizationPaper from 'components/organization/organizationPaper.vue'
import organizationPublishEveryYear from 'components/organization/organizationPublishEveryYear.vue'
import organizationKeyWord from 'components/organization/organizationKeyWord.vue'
import organizationAuthorRank from 'components/organization/organizationAuthorRank.vue'
import searchOrganization from 'components/search/searchOrganization.vue'
import interpersonalRelationshipNetwork from 'components/dataVisualization/interpersonalRelationshipNetwork'
import domainDistribution from 'components/dataVisualization/domainDistribution'
import paper from 'components/paper/paper'
import paperDetail from 'components/paper/paperDetail'



import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
// import 'assets/lib/jquery.particleground.js'

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
    path: '/search',
    component: search
  },{
    path: '/searchJournal',
    component: searchJournal
  },{
    path: '/searchOrganization',
    component: searchOrganization
  },{
    path: '/journalInfo',
    component: journalInfo
  },{
    path: '/journalPaper',
    component: journalPaper
  },{
    path: '/journalPublishEveryYear',
    component: journalPublishEveryYear
  },{
    path: '/journalKeyWord',
    component: journalKeyWord
  },{
    path: '/journalAuthorRank',
    component: journalAuthorRank
  },{
    path: '/organizationInfo',
    component: organizationInfo
  },{
    path: '/organizationPaper',
    component: organizationPaper
  },{
    path: '/organizationPublishEveryYear',
    component: organizationPublishEveryYear
  },{
    path: '/organizationKeyWord',
    component: organizationKeyWord
  },{
    path: '/organizationAuthorRank',
    component: organizationAuthorRank
  },{
    path: '/interpersonalRelationshipNetwork',
    component: interpersonalRelationshipNetwork
  },{
    path: '/domainDistribution',
    component: domainDistribution
  },{
    path: '/personalInfo',
    component: personalInfo
  },{
    path: '/paper',
    component: paper
  },{
    path: '/paperDetail',
    component: paperDetail
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

