<template>
	<div class="paper">
		<v-header></v-header>
		<div class="paper-container" v-loading="loading">
			<el-container style="height: 180px; border: 1px solid #eee; background-color: #FAFAFA">
				<el-header>
					<!-- <organization-header :name=oheader[0] :website=oheader[1] :logo=oheader[2] :english_name=oheader[3] :location=oheader[4] ></organization-header> -->
				</el-header>
			</el-container>
			<el-container style="height: 720px;  border: 1px solid #eee">
				<el-aside style="font-size: 30px; width: 180px;">
					 <organization-sidebar index="organizationPaper"></organization-sidebar>
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
						      label="题目">
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
						      :total=this.pageTotal>
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
import organizationMenu from 'components/organization/organizationMenu'
import organizationInfoHeader from 'components/organization/organizationInfoHeader'
import DB from '../../DB/db'

export default {
  data() {
  	return {
  		oheader: [],
  		paperData: [],
  		loading: true,
  		currentPage: 1,
        pagesize: 10,
  	}
  },
  components: {
    'v-header': header,
    'organization-sidebar': organizationMenu,
	'organization-header': organizationInfoHeader
  },
  beforeCreate: function(){
  	let organizationName = localStorage.getItem("organizationName")
  	this.$router.push({path: '/organizationPaper'+'?'+'name='+organizationName})
  },
  created: function() {
		const t = this
		DB.Search.get_organization_by_name({
			name: this.$route.query.name
		}).then(result=>{
		    let { list = [] } = result;
		   	t.oheader.push(list[0].name, list[0].website, list[0].logo, list[0].english_name, list[0].location)
		})
		DB.Search.get_paper_by_organization_name({
			name: this.$route.query.name
		}).then(result=>{
			t.pageTotal = result.total
		    let { list = [] } = result;
		    for(let i=0 ; i<list.length; i++){
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
