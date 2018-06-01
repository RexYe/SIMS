<template>
	<div class="personalInfo">
		<v-header></v-header>
		<div class="personalInfo-container" v-loading="loading">
			<el-container style="width:100%; height: 180px; background: rgba(0,0,0,0)">
				<el-header>
					<organization-header :name=oheader[0] :website=oheader[1] :logo=oheader[2] :english_name=oheader[3] :location=oheader[4] ></organization-header>
				</el-header>
			</el-container>
			<el-container style="height: 100%;" >
				<el-aside style="font-size: 30px; width: 160px;">
					 <organization-sidebar index="organizationInfo"></organization-sidebar>
				</el-aside>
				<el-main>
					<div class="resume">
						<div class="info">
							<span>机构简介</span>
							<div class="line"></div>
							<div id="info-list">{{intro[0]}}</div>
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
			intro: [],
			loading: false
		}
	},
	components: {
		'v-header': header,
		'organization-sidebar': organizationMenu,
		'organization-header': organizationInfoHeader
	},
	methods: {
		
	},
	beforeCreate: function() {
		let organizationName = localStorage.getItem("organizationName")
  		this.$router.push({path: '/organizationInfo'+'?'+'name='+organizationName})
	},
	created: function() {
		const t = this
		DB.Search.get_organization_by_name({
			name: this.$route.query.name
		}).then(result=>{
		    let { list = [] } = result;
		   	t.oheader.push(list[0].name, list[0].website, list[0].logo, list[0].english_name, list[0].location)
		   	t.intro.push(list[0].introduction)
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
		color: #fff;
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
