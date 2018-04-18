<template>
	<div class="paperDetail">
		<v-header></v-header>
		<div class="paperDetail-container">
			<el-container style="height: 180px; border: 1px solid #eee; background-color: #ffd04b">
				<el-header>
					<p-header name='王小' college="浙江工业大学"></p-header>
				</el-header>
			</el-container>
			<el-container style="height: 500px;  border: 1px solid #eee">
				<el-aside style="font-size: 30px; width: 180px;">
					 <p-menu index="paper"></p-menu>
				</el-aside>
				<el-main>
					<div class="paper-details">
						<p>{{paperName}}</p>
						<p>作者：</p>
						<p>单位：</p>
						<p>关键词：</p>
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

export default {
  data() {
  	return {
  		searchData: [{
          name: '王小',
          paperInfo: '徐新黎 吕琪 王万良 皇甫晓洁 . 一种带有能量自补给节点的异构传感器网络分簇路由算法. 计算机科学, 2017,     (01): 134-140'
        }, {
          name: '王小',
          paperInfo: '徐新黎 吕琪 王万良 皇甫晓洁 . 一种带有能量自补给节点的异构传感器网络分簇路由算法. 计算机科学, 2017,     (01): 134-140'
        }],
        paperName: '基于网格排序的多目标粒子群优化算法'
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
  }
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
