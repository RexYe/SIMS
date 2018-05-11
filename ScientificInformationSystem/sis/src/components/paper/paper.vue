<template>
	<div class="paper">
		<router-link :to="/paper2/" ></router-link>
		<v-header></v-header>
		<div class="paper-container">
			<el-container style="height: 180px; border: 1px solid #eee; background-color: #ffd04b">
				<el-header>
					<p-header :name=pheader[0] :college=pheader[1] :avatar_src=pheader[2]></p-header>
				</el-header>
			</el-container>
			<el-container style="height: 500px;  border: 1px solid #eee">
				<el-aside style="font-size: 30px; width: 180px;">
					 <p-menu index="paper"></p-menu>
				</el-aside>
				<el-main>
					<div class="paper-results">
						<el-table
			    :data="paperData"
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
  		paperData: []
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
		})
  },
  methods: {
  		handleClick(row) {
			console.log('row',row);
			if(window.localStorage){     
  				localStorage.setItem("title", row.title); 
  			}
			this.$router.push({path: '/paperDetail'})
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
		margin-top: 70px;
	}
</style>
