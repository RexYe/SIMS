<template>
	<div class="paper">
		<router-link :to="/paper2/" ></router-link>
		<v-header></v-header>
		<div class="paper-container" v-loading="loading">
			<el-container style="height: 180px; background-color: rgba(0,0,0,0)">
				<el-header>
					<!-- <p-header name='王小' college="浙江工业大学"></p-header> -->
					<p-header :name=pheader[0] :college=pheader[1] :avatar_src=pheader[2]></p-header>
				</el-header>
			</el-container>
			<el-container style="height: 720px;">
				<el-aside style="font-size: 30px; width: 180px;">
					 <p-menu index="paper"></p-menu>
				</el-aside>
				<el-main>
					<div class="paper-results">
						<el-table
						    :data="paperData.slice((currentPage-1)*pagesize,currentPage*pagesize)"
						    height="610"
						    stripe
						    style="width: 100%">
						    <el-table-column
						      prop="authors"
						      label="作者"
						      width="300">
						    </el-table-column>
						    <el-table-column
						      prop="title"
						      label="题目"
						      width="400">
						    </el-table-column>
						    <el-table-column
						      prop="journal"
						      label="期刊">
						    </el-table-column>
						    <el-table-column
						      prop="publish_time"
						      label="时间"
						      width="150">
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
			  			<div class="pagination">
							<el-pagination
							  background
						      @size-change="handleSizeChange"
						      @current-change="handleCurrentChange"
						      
						      :page-sizes="[5, 10, 20, 30]"
						      :page-size="10"
						      layout="total, sizes, prev, pager, next, jumper"
						      :total="paperData.length">
						    </el-pagination>
			  			</div>
					</div>
				</el-main>
			</el-container>
		</div>
	</div>
</template>

<script>
import header from 'components/header/header'
import echarts from 'echarts'
import personalInfoHeader from 'components/personalInfoHeader/personalInfoHeader'
import personMenu from 'components/personMenu/personMenu'
import DB from '../../DB/db'

export default {
  data() {
  	return {
  		pheader: [],
  		paperData: [],
  		loading: true,
  		currentPage: 1,
        pagesize: 10
  	}
  },
  components: {
    'v-header': header,
    'p-header': personalInfoHeader,
    'p-menu': personMenu
  },
  beforeCreate: function(){
  	let uniid = localStorage.getItem("uniid")
  	this.$router.push({path: '/paper'+'?'+'uniid='+uniid})
  },
  created: function() {
		const t = this
		DB.Search.get_personalinfo_by_uniid({
			uniid: this.$route.query.uniid
		}).then(result=>{
		    let { list = [] } = result;
		    console.log('list',list)
		    t.pheader.push(list[0].name, list[0].organization, list[0].avatar_src)    
		})
		DB.Search.get_paper_title_by_uniid({
			uniid: this.$route.query.uniid
		}).then(result=>{
		    let { list = [] } = result;
		    for(let i=0 ; i<list.length; i++){
		    	console.log(list[i])
		    	t.paperData.push(list[i])
		    }    
		}).then(()=>{
			t.loading = false;
		})
  },
  methods: {
  		handleClick(row) {
			console.log('row',row);
			if(window.localStorage){     
  				localStorage.setItem("title", row.title); 
  			}
			this.$router.push({path: '/paperDetail'})
		},
		handleSizeChange: function (size) {
        	this.pagesize = size;
   		 },
   		handleCurrentChange: function(currentPage){
        	this.currentPage = currentPage;
    	}
  }
}

</script>
<style scoped>
	.paper{
		width: 100%;
		height: 100%;
	}
	.paper-container{
		height: 900px;
		margin-top: 60px;
	}
	.pagination{
		display: flex;
		flex-direction: column;
		padding-top: 20px;
		align-items: center;
	}
</style>
