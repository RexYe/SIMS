<template>
	<div class="paperDetail">
		<v-header></v-header>
		<div class="paperDetail-container">
			<el-container style="height: 180px; border: 1px solid #eee; background-color: #FAFAFA">
				<el-header>
					<!-- <p-header name='王小' college="浙江工业大学"></p-header> -->
					<p-header :name=pheader[0] :college=pheader[1] :avatar_src=pheader[2]></p-header>
				</el-header>
			</el-container>
			<el-container style="height: 720px;  border: 1px solid #eee">
				<el-aside style="font-size: 30px; width: 180px;">
					 <p-menu index="paper"></p-menu>
				</el-aside>
				<el-main>
					<div class="paper-details">
						<span class="title">{{paperDetailData.title}}</span>
						<span class="authors">{{paperDetailData.authors}}</span>
						<span class="src">{{paperDetailData.src}}</span>
						<span>摘要：</span>
						<span class="abstract">{{paperDetailData.abstract}}</span>
						<span>关键词：</span>
						<span class="keywords">{{paperDetailData.key_words}}</span>
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
			// console.log(row);
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
		    t.pheader.push(list[0].name, list[0].organization, list[0].avatar_src)    
		})
		DB.Search.get_paper_detail_by_title({
			title: localStorage.getItem("title")
		}).then(result=>{
		    let { list = [] } = result;
		    t.paperDetailData = list[0]   
		})
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
		margin-top: 60px;
	}
	.paper-details{
		display: flex;
		flex-direction: column;
	}
	.paper-details .title{
		font-size: 30px;
		margin-bottom: 20px; 
	}
	.paper-details .authors{
		font-size: 18px;
		font-family: Microsoft YaHei;
		margin-bottom: 10px;
	}
	.paper-details .src{
		font-size: 15px;
		font-family: Microsoft YaHei;
		color: grey; 
		margin-bottom: 15px;
	}
	.paper-details .abstract{
		font-size: 15px;
		font-family: Microsoft YaHei;
		width: 70%;
		margin-bottom: 15px;
		margin-top: 9px;
		line-height: 21px;
	}
	.paper-details .keywords{
		font-size: 16px;
		font-family: Microsoft YaHei;
		width: 70%;
		margin-bottom: 15px;
		margin-top: 9px;
		line-height: 21px;
	}
</style>
