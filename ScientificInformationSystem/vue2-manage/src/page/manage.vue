<template>
	<div class="manage_page fillcontain">
		<el-row style="height: 100%;">
	  		<el-col :span="4"  style="min-height: 100%; background-color: #324057;">
				<el-menu :default-active="defaultActive" style="min-height: 100%;" theme="dark" router>
					<el-menu-item index="manage"><i class="el-icon-menu"></i>首页</el-menu-item>
					<el-submenu index="2">
						<template slot="title"><i class="el-icon-document"></i>用户管理</template>
						<el-menu-item index="addUsers">新建用户</el-menu-item>
						<el-menu-item index="deleteUsers">删除用户</el-menu-item>
					</el-submenu>
					<el-submenu index="3">
						<template slot="title"><i class="el-icon-edit"></i>作者管理</template>
						<el-menu-item index="addAuthors">新增作者</el-menu-item>
						<el-menu-item index="deleteAuthors">删除作者</el-menu-item>
					</el-submenu>
					<el-submenu index="4">
						<template slot="title"><i class="el-icon-star-on"></i>期刊管理</template>
						<el-menu-item index="paper">新增期刊</el-menu-item>
						<el-menu-item index="project">删除期刊</el-menu-item>
					</el-submenu>
					<el-submenu index="5">
						<template slot="title"><i class="el-icon-menu"></i>机构管理</template>
						<el-menu-item index="addOrganization">新增机构</el-menu-item>
						<el-menu-item index="deleteOrganization">删除机构</el-menu-item>
					</el-submenu>
				<!-- 	<el-submenu index="6">
						<template slot="title"><i class="el-icon-more"></i>领域管理</template>
						<el-menu-item index="addDomain">新增领域</el-menu-item>
						<el-menu-item index="deleteDomain">删除领域</el-menu-item>
					</el-submenu> -->
					<el-submenu index="7">
						<template slot="title"><i class="el-icon-warning"></i>说明</template>
						<el-menu-item index="explain">说明</el-menu-item>
					</el-submenu>
				</el-menu>
			</el-col>
			<el-col :span="20" style="height: 100%;overflow: auto;">
				<keep-alive>
				    <router-view></router-view>
				</keep-alive>
			</el-col>
		</el-row>
  	</div>
</template>

<script>
    export default {
		computed: {
			defaultActive: function(){
				return this.$route.path.replace('/', '');
			}
		},
    }
</script>


<style lang="less" scoped>
	@import '../style/mixin';
	.manage_page{
		
	}
</style>
