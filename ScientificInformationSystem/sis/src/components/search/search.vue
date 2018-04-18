<template>
	<div class="search">
		<v-header></v-header>
		<div class="search-container">
			<span>搜索结果:</span>
			<div class="search-results">
				<el-table
			    :data="searchData"
			    stripe
			    style="width: 100%">
			    <el-table-column
			      prop="name"
			      label="姓名"
			      width="180">
			    </el-table-column>
			    <el-table-column
			      prop="organization"
			      label="机构">
			    </el-table-column>
			    <el-table-column
			      fixed="right"
			      label="操作"
			      width="100">
			      <template slot-scope="scope">
			        <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>
			      </template>
			    </el-table-column>
			  </el-table>
			</div>
		</div>
	</div>
</template>

<script>
import header from 'components/header/header'


export default {
data() {
	return {
		searchData: [{
			name: '王小',
			organization: '浙江工业大学'
		}, {
			name: '王小',
			organization: '东南大学'
		}]
	}
},
  components: {
    'v-header': header
  },
  methods:{
	handleClick(row) {
		console.log(row);
		this.$router.push({path: '/personalInfo'})
	}
  }
}
</script>
<style scoped>
	.search{
		width: 100%;
		height: 100%;
	}
	.search-container{
		height: 900px;
		margin-top: 70px;
	}
	.search-results{
		width: 70%;
		margin: 0 auto;
	}
</style>
