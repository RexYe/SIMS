<template>
	<div class="personalInfo">
		<v-header></v-header>
		<div class="personalInfo-container" v-loading="loading">
			<el-container style="width:100%; height: 180px; border: 1px solid #eee; background: #FAFAFA">
				<el-header>
					<p-header :name=pheader[0] :college=pheader[1] :avatar_src=pheader[2]></p-header>
				</el-header>
			</el-container>
			<el-container style="height: 100%;  border: 1px solid #eee" >
				<el-aside style="font-size: 30px; width: 180px;">
					 <p-menu index="personalInfo"></p-menu>
				</el-aside>
				<el-main>
					<div class="resume">
						<div class="info">
							<span>个人简介</span>
							<div class="line"></div>
							<div id="info-list">{{intro[0]}}</div>
						</div>
						<div class="domain">
							<span>科技领域</span>
							<div class="line"></div>
							<div id="domain-list" v-for="domain in domains"><el-tag id="tag" size="small" type="info" >{{domain.name}}</el-tag></div>
						</div>
						<div class="keywords">
							<span>关键词</span>
							<div class="line"></div>
							<div id="keywords-list" v-for="keyword in keywords"><el-tag id="tag" size="small" type="info" >{{keyword.name}}</el-tag></div>
						</div>
						<div class="work-experience">
							<span>工作经历</span>
							<div class="line"></div>
							<div id="work-experience-list">
								 <el-table
								:data="workExperienceData"
								stripe
								v-bind:show-header="false"
								style="width: 100%">
								<el-table-column
								  label="logo"
								  width="180">
									<template slot-scope="scope">
										<img :src="scope.row.logo" style="width: 60px; height:60px">
									</template>
								</el-table-column>
								<el-table-column
								  prop="name"
								  label="姓名">
								</el-table-column>
								</el-table>
							</div>
						</div>
						<div class="edu-experience">
							<span>教育经历</span>
							<div class="line"></div>
							<div id="edu-experience-list">
								 <el-table
								:data="eduExperienceData"
								stripe
								v-bind:show-header="false"
								style="width: 100%">
								<el-table-column
								  label="logo"
								  width="180">
									<template slot-scope="scope">
										<img :src="scope.row.logo" style="width: 60px; height:60px">
									</template>
								</el-table-column>
								<el-table-column
								  prop="name"
								  label="姓名">
								</el-table-column>
								</el-table>
							</div>
						</div>
					</div>
				</el-main>
			</el-container>
		</div>
	</div>
</template>

<script>
import header from 'components/header/header'
import personalInfoHeader from 'components/personalInfoHeader/personalInfoHeader'
import personMenu from 'components/personMenu/personMenu'
import DB from '../../DB/db'

export default {
	data() {
		return {
			pheader: [],
			domains: [],
			keywords: [],
			workExperienceData:[],
			eduExperienceData:[],
			intro: [],
			loading: true
		}
	},
	components: {
		'v-header': header,
		'p-header': personalInfoHeader,
		'p-menu': personMenu
	},
	methods: {
		
	},
	beforeCreate: function() {
		let uniid = localStorage.getItem("uniid")
  		this.$router.push({path: '/personalInfo'+'?'+'uniid='+uniid})
	},
	created: function() {
		const t = this
		console.log('uniid',this.$route)
		DB.Search.get_personalinfo_by_uniid({
			uniid: this.$route.query.uniid
		}).then(result=>{
		    let { list = [] } = result;
		    console.log('list',list)
		    t.pheader.push(list[0].name, list[0].organization, list[0].avatar_src)
		    t.intro.push(list[0].intro)
		    let work_experience_arr = list[0].work_experience.split(',')
		    t.workExperienceData.push({logo:work_experience_arr[1], name:work_experience_arr[0]})
		    let edu_experience = list[0].edu_experience.split(',');
		    t.eduExperienceData.push({logo:edu_experience[1], name:edu_experience[0]});
		    let domains_arr = list[0].domain.split(',');
		    for (let i=0; i<domains_arr.length ; i++) {
				t.domains.push({name: domains_arr[i]})
			}	
			let keywords_arr = list[0].domain.split(',');
		    for (let i=0; i<domains_arr.length ; i++) {
				t.keywords.push({name: domains_arr[i]})
			}	    
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
		margin-top: 70px;
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
	.resume .info #list{
		font-size: 15px;
		color: #6C6A6A;
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
