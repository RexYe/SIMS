<template>
	<div class="searchOrganization">
		<v-header></v-header>
		<div class="search-container">
			<div class="search-results">
				<div id="search-results-num">检索到{{searchResultsNum}}条结果</div>
				<el-table
				v-loading="loading"
			    :data="searchData"
			    stripe
			    style="width: 100%">
			    <el-table-column
			      type="index"
			      width="100">
			    </el-table-column>
			    <el-table-column
			      prop="name"
			      label="名称"
			      width="180">
			    </el-table-column>
			    <el-table-column
			      prop="location"
			      label="地址">
			    </el-table-column>
			    <el-table-column
			      prop="website"
			      label="网址">
			    </el-table-column>
			    <el-table-column
			      fixed="right"
			      label="操作"
			      width="150">
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
import DB from '../../DB/db'

export default {
	data() {
		return {
			searchResultsNum : 0,
			searchData: [],
			loading: true
		}
	},
	components: {
		'v-header': header
	},
	methods:{
		handleClick(row) {
			if(window.localStorage){     
				localStorage.setItem("organizationName", row.name);
			}
			this.$router.push({path: '/organizationInfo'+'?'+'name='+row.name})
		}
	},
	beforeCreate: function(){
		// this.loading = true;
	},
	created: function() {
		// this.loading = true;
	},
	mounted: function() {
		const t = this
		t.searchData = [];
		t.searchResultsNum = 0;
		DB.Search.get_organization_by_name({
	        name: this.$route.query.name
	    }).then(result=>{
            let { list = [] } = result
            t.searchData = list
            t.searchResultsNum = list.length;
	    }).then(()=>{
	    	t.loading = false;
	    })
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
		margin-top: 60px;
	}
	.search-container #search-results-num{
		padding-left: 10px;
		padding-top: 15px;
		padding-bottom: 10px;
		color: #C2C1C1;
		font-size: 13px;
	}
	.search-results{
		width: 70%;
		margin: 0 auto;
	}
</style>
