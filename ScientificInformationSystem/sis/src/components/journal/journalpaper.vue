<template>
	<div class="paper">
		<v-header></v-header>
		<div class="paper-container" v-loading="loading">
			<el-container style="height: 180px; background-color: rgba(0,0,0,0)">
				<el-header>
					<journalinfo-header :name=jheader[0] :website=jheader[1] :logo=jheader[2] :english_name=jheader[3] :honor=jheader[4] :complex_influence=jheader[5] :comprehensive_influence=jheader[6]></journalinfo-header>
				</el-header>
			</el-container>
			<el-container style="height: 720px;">
				<el-aside style="font-size: 30px; width: 180px;">
					 <journal-sidebar index="journalPaper"></journal-sidebar>
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
import journalMenu from 'components/journal/journalMenu'
import journalInfoHeader from 'components/journal/journalInfoHeader'
import DB from '../../DB/db'

export default {
  data() {
  	return {
  		jheader: [],
  		paperData: [],
  		loading: true,
  		currentPage: 1,
        pagesize: 10
  	}
  },
  components: {
    'v-header': header,
    'journal-sidebar': journalMenu,
	'journalinfo-header': journalInfoHeader
  },
  beforeCreate: function(){
  	let journalName = localStorage.getItem("journalName")
  	this.$router.push({path: '/journalPaper'+'?'+'name='+journalName})
  },
  created: function() {
		const t = this
		DB.Search.get_journal_by_name({
            name: this.$route.query.name
        }).then(result=>{
            let { list = [] } = result;
            let honor_arr = list[0].honor.split(';')
            t.jheader.push(list[0].name, list[0].website, list[0].logo, list[0].english_name, honor_arr, list[0].complex_influence, list[0].comprehensive_influence)
            t.intro.push(list[0].introduction)     
            t.host_unit.push(list[0].host_unit) 
        }).then(()=>{
            t.loading = false;
        })
		DB.Search.get_paper_by_journal_name({
			name: this.$route.query.name
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
