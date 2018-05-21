<template>
	<div class="personalInfo">
		<v-header></v-header>
		<div class="personalInfo-container" v-loading="loading">
			<el-container style="width:100%; height: 180px; background: rgba(0,0,0,0)">
				<el-header>
					<journalinfo-header :name=jheader[0] :website=jheader[1] :logo=jheader[2] :english_name=jheader[3] :honor=jheader[4] :complex_influence=jheader[5] :comprehensive_influence=jheader[6]></journalinfo-header>
				</el-header>
			</el-container>
			<el-container style="height: 100%;" >
				<el-aside style="font-size: 30px; width: 160px;">
					 <journal-sidebar index="journalInfo"></journal-sidebar>
				</el-aside>
				<el-main>
					<div class="resume">
						<div class="info">
							<span>期刊简介</span>
							<div class="line"></div>
							<div id="info-list">{{intro[0]}}</div>
						</div>
						<div class="host_unit">
							<span>主办单位</span>
							<div class="line"></div>
							<div id="info-list">{{host_unit[0]}}</div>
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
			intro: [],
			host_unit: [],
			loading: false
		}
	},
	components: {
		'v-header': header,
		'journal-sidebar': journalMenu,
		'journalinfo-header': journalInfoHeader
	},
	methods: {
		
	},
	beforeCreate: function() {
		let journalName = localStorage.getItem("journalName")
  		this.$router.push({path: '/journalInfo'+'?'+'name='+journalName})
	},
	created: function() {
		const t = this
		DB.Search.get_journal_by_name({
			name: this.$route.query.name
		}).then(result=>{
		    let { list = [] } = result;
		    // console.log('list',list)
		    let honor_arr = list[0].honor.split(';')
		    t.jheader.push(list[0].name, list[0].website, list[0].logo, list[0].english_name, honor_arr, list[0].complex_influence, list[0].comprehensive_influence)
	 		t.intro.push(list[0].introduction)	   
	 		t.host_unit.push(list[0].host_unit) 
		}).then(()=>{
			t.loading = false;
		})
	}
}

</script>
<style scoped>
	.personalInfo{
		width: 100%;
		height: 100%;
	}
	.personalInfo-container{
		height: 100%;
		margin-top: 60px;
	}
	.personalInfo-container .resume{
		display: flex;
		flex-direction: column;
	}
	.resume span{
		font-size: 20px;
	}
	.resume .line{
		width: 100%;
		border-bottom: 1px solid #dddddd;
		margin-top: 10px;
		margin-bottom: 10px;
	}
	.resume .info{
		margin-bottom: 20px;
	}
	.resume #info-list{
		font-size: 16px;
		color: #6C6A6A;
		padding: 10px;
	}
	.resume .domain{
		margin-bottom: 20px;
	}
	.resume .domain #domain-list{
		margin-top: 10px;
	}
	.resume .domain #domain-list #tag{
		font-size: 15px;
	}
	.resume .keywords{
		margin-bottom: 20px;
	}
	.resume .keywords #keywords-list{
		margin-top: 10px;
		width: 100%;
	}
	.resume .keywords #keywords-list #tag{
		font-size: 15px;
	}
</style>
