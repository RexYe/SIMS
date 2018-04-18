import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const paper = r => require.ensure([], () => r(require('@/components/paper')), 'paper');

const routes = [
	{
		path: '/',
		component: login
	},
	{
		path: '/manage',
		component: manage,
		name: '',
		children: [{
			path: '',
			component: home,
			meta: [],
		},{
			path: '/paper',
			component: paper,
			meta: ['内容管理', '论文管理'],
		}]
	}
]

export default new Router({
	routes,
	strict: process.env.NODE_ENV !== 'production',
})
