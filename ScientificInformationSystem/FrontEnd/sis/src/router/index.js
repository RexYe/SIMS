import Vue from 'vue'
import Router from 'vue-router'
import Search from '@/components/Search'
import SearchResults from '@/components/SearchResults'

// const search = () => import('@/components/Search')
Vue.use(Router)

export default new Router({
	routes: [
		{
			path: '/',
			name: 'Search',
			component: Search
		},
		{
			path: '/2',
			name: 'SearchResults',
			component: SearchResults
		}
	]
})
