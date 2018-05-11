<template>
	<div class="paperDetail">
		<v-header></v-header>
		<div class="paperDetail-container">
			<el-container style="height: 180px; border: 1px solid #eee; background-color: #ffd04b">
				<el-header>
					<p-header name='王小' college="浙江工业大学"></p-header>
					<!-- <p-header :name=pheader[0] :college=pheader[1] :avatar_src=pheader[2]></p-header> -->
				</el-header>
			</el-container>
			<el-container style="height: 500px;  border: 1px solid #eee">
				<el-aside style="font-size: 30px; width: 180px;">
					 <p-menu index="paper"></p-menu>
				</el-aside>
				<el-main>
					<div class="paper-details">
						<h1>{{paperDetailData.title}}</h1>
						<p>{{paperDetailData.src}}</p>
						<p>{{paperDetailData.authors}}</p>
						摘要：<p>{{paperDetailData.abstract}}</p>
						关键词：<p>{{paperDetailData.key_words}}</p>
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
        paperDetailData:[]
  	}
  },
  components: {
    'v-header': header,
    'p-header': personalInfoHeader,
    'p-menu': personMenu
  },
  methods: {
  		handleClick(row) {
		console.log(row);
		this.$router.push({path: '/personalInfo'})
	}
  },
   beforeCreate: function(){
  	let uniid = localStorage.getItem("uniid")
  	this.$router.push({path: '/paperDetail'+'?'+'uniid='+uniid})
  },
  created: function() {
		const t = this
		DB.Search.get_personalinfo_by_uniid({
			uniid: this.$route.query.uniid
		}).then(result=>{
		    let { list = [] } = result;
		    // console.log('list',list)
		    t.pheader.push(list[0].name, list[0].organization, list[0].avatar_src)    
		})
		DB.Search.get_paper_detail_by_title({
			title: localStorage.getItem("title")
		}).then(result=>{
		    let { list = [] } = result;
		    // console.log(list)
		    t.paperDetailData = list[0]   
		})
		// console.log(t.paperDetailData)
  },
}

</script>
<style scoped>
	.paperDetail{
		width: 100%;
		height: 100%;
	}
	.paperDetail-container{
		height: 900px;
		margin-top: 70px;
	}
</style>
