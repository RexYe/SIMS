<template>
	<div class="project">
		<v-header></v-header>
		<div class="project-container">
			<el-container style="height: 180px; border: 1px solid #eee; background-color: #ffd04b">
				<el-header>
					<p-header name='王小' college="浙江工业大学"></p-header>
				</el-header>
			</el-container>
			<el-container style="height: 720px;  border: 1px solid #eee">
				<el-aside style="font-size: 30px; width: 180px;">
					 <p-menu index="project"></p-menu>
				</el-aside>
				<el-main>
					<div>project</div>
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
	.project{
		width: 100%;
		height: 100%;
	}
	.project-container{
		height: 900px;
		margin-top: 70px;
	}
</style>
