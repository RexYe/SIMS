import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const login = r => require.ensure([], () => r(require('@/page/login')), 'login');
const manage = r => require.ensure([], () => r(require('@/page/manage')), 'manage');
const home = r => require.ensure([], () => r(require('@/page/home')), 'home');
// const addShop = r => require.ensure([], () => r(require('@/page/addShop')), 'addShop');
// const addGoods = r => require.ensure([], () => r(require('@/page/addGoods')), 'addGoods');
const userList = r => require.ensure([], () => r(require('@/page/userList')), 'userList');
// const shopList = r => require.ensure([], () => r(require('@/page/shopList')), 'shopList');
// const foodList = r => require.ensure([], () => r(require('@/page/foodList')), 'foodList');
// const orderList = r => require.ensure([], () => r(require('@/page/orderList')), 'orderList');
const adminList = r => require.ensure([], () => r(require('@/page/adminList')), 'adminList');
const visitor = r => require.ensure([], () => r(require('@/page/visitor')), 'visitor');
const newMember = r => require.ensure([], () => r(require('@/page/newMember')), 'newMember');
const uploadImg = r => require.ensure([], () => r(require('@/page/uploadImg')), 'uploadImg');
const vueEdit = r => require.ensure([], () => r(require('@/page/vueEdit')), 'vueEdit');
const adminSet = r => require.ensure([], () => r(require('@/page/adminSet')), 'adminSet');
const sendMessage = r => require.ensure([], () => r(require('@/page/sendMessage')), 'sendMessage');
const explain = r => require.ensure([], () => r(require('@/page/explain')), 'explain');
const addDomain = r => require.ensure([], () => r(require('@/page/addDomain')), 'addDomain');
const deleteDomain = r => require.ensure([], () => r(require('@/page/deleteDomain')), 'deleteDomain');
const addAuthors = r => require.ensure([], () => r(require('@/page/addAuthors')), 'addAuthors');
const deleteAuthors = r => require.ensure([], () => r(require('@/page/deleteAuthors')), 'deleteAuthors');
const addUsers = r => require.ensure([], () => r(require('@/page/addUsers')), 'addUsers');
const deleteUsers = r => require.ensure([], () => r(require('@/page/deleteUsers')), 'deleteUsers');
const addOrganization = r => require.ensure([], () => r(require('@/page/addOrganization')), 'addOrganization');
const deleteOrganization = r => require.ensure([], () => r(require('@/page/deleteOrganization')), 'deleteOrganization');
const paper = r => require.ensure([], () => r(require('@/page/paper')), 'paper');
const project = r => require.ensure([], () => r(require('@/page/project')), 'project');

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
			path: '/userList',
			component: userList,
			meta: ['数据管理', '用户列表'],
		},{
			path: '/adminList',
			component: adminList,
			meta: ['数据管理', '管理员列表'],
		},{
			path: '/visitor',
			component: visitor,
			meta: ['图表', '用户分布'],
		},{
			path: '/newMember',
			component: newMember,
			meta: ['图表', '用户数据'],
		},{
			path: '/uploadImg',
			component: uploadImg,
			meta: ['文本编辑', 'MarkDown'],
		},{
			path: '/vueEdit',
			component: vueEdit,
			meta: ['编辑', '文本编辑'],
		},{
			path: '/adminSet',
			component: adminSet,
			meta: ['设置', '管理员设置'],
		},{
			path: '/addUsers',
			component: addUsers,
			meta: ['用户管理', '新增用户'],
		},{
			path: '/deleteUsers',
			component: deleteUsers,
			meta: ['用户管理', '删除用户'],
		},{
			path: '/addAuthors',
			component: addAuthors,
			meta: ['作者管理', '新增作者'],
		},{
			path: '/deleteAuthors',
			component: deleteAuthors,
			meta: ['作者管理', '删除作者'],
		},{
			path: '/paper',
			component: paper,
			meta: ['内容管理', '论文管理'],
		},{
			path: '/project',
			component: project,
			meta: ['内容管理', '项目管理'],
		},{
			path: '/addOrganization',
			component: addOrganization,
			meta: ['机构管理', '新增机构'],
		},{
			path: '/deleteOrganization',
			component: deleteOrganization,
			meta: ['机构管理', '删除机构'],
		},{
			path: '/addDomain',
			component: addDomain,
			meta: ['领域管理', '新增领域'],
		},{
			path: '/deleteDomain',
			component: deleteDomain,
			meta: ['领域管理', '删除领域'],
		},{
			path: '/sendMessage',
			component: sendMessage,
			meta: ['设置', '发送通知'],
		},{
			path: '/explain',
			component: explain,
			meta: ['说明', '说明'],
		}]
	}
]

export default new Router({
	routes,
	strict: process.env.NODE_ENV !== 'production',
})
