<template>
	<div class="personalInfo">
		<v-header></v-header>
		<div class="personalInfo-container">
			<el-container style="width:100%; height: 180px; border: 1px solid #eee; background-color: #ffd04b">
				<el-header>
					<p-header name='王小' college="浙江工业大学"></p-header>
				</el-header>
			</el-container>
			<el-container style="height: 100%;  border: 1px solid #eee">
				<el-aside style="font-size: 30px; width: 180px;">
					 <p-menu index="personalInfo"></p-menu>
				</el-aside>
				<el-main>
					<div class="resume">
						<div class="info">
							<span>个人简介</span>
							<div class="line"></div>
							<div id="info-list">王小，男，1962年8月生，山西山阴安荣村人，全国政协委员。任北京大学环境工程研究所所长，兼任《应用基础与工程科学学报》编委会主任、《科学通报》特邀编辑、国际水沙科学协会（IASWS）常务理事等职。
1982年毕业于武汉大学水利学院治河专业，1985年和1989年在清华大学水利工程系水力学及河流海岸动力学专业分别获硕士和博士学位，1989至1991年在北京大学做博士后研究工作。曾在日本北海道大学土木工程系、牛津大学工程力学系作为访问学者进行学术交流和合作研究。1992年起在北京大学任教授。1996年获国家杰出青年基金资助。</div>
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

export default {
	data() {
		return {
			domains: [
				{name: '信息科学'},
				{name: '图形学'}
			],
			keywords: [
				{name: '信息科学'},
				{name: '图形学'}
			],
			workExperienceData:[
				{logo:'https://www.scholarmate.com/insLogo/450.jpg' , name:'浙江大学'},
				{logo:'https://www.scholarmate.com/insLogo/450.jpg' , name:'清华大学'}
			],
			eduExperienceData:[
				{logo:'https://www.scholarmate.com/insLogo/450.jpg' , name:'浙江大学'},
				{logo:'https://www.scholarmate.com/insLogo/450.jpg' , name:'清华大学'}
			]
		}
	},
	components: {
		'v-header': header,
		'p-header': personalInfoHeader,
		'p-menu': personMenu
	},
	methods: {
		
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
