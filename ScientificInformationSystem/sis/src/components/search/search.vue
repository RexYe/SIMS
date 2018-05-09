<template>
	<div class="search">
		<v-header></v-header>
		<div class="search-container">
			<div id="search-results-num">检索到{{searchResultsNum}}条结果</div>
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
import DB from '../../DB/db'

export default {
data() {
	return {
		searchResultsNum : 0,
		searchData: []
	}
},
  components: {
    'v-header': header
  },
  methods:{
	handleClick(row) {
		// console.log('row:',row);
	if(window.localStorage){     
  		localStorage.setItem("uniid", row.uniid);
  	}
		this.$router.push({path: '/personalInfo'+'?'+'uniid='+row.uniid})
	}
  },
  created: function() {

  },
  mounted: function() {
  	const t = this
  	t.searchData = [];
  	t.searchResultsNum = 0;
	DB.Search.get_authors_by_name({
	        name: this.$route.query.name
	    }).then(result=>{
	            console.log(result)
                let { list = [] } = result
                console.log(list)
                t.searchData = list
                t.searchResultsNum = list.length;
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
		margin-top: 70px;
	}
	.search-container #search-results-num{
		padding-left: 10px;
		padding-top: 10px;
		color: #C2C1C1;
	}
	.search-results{
		width: 70%;
		margin: 0 auto;
	}
</style>
