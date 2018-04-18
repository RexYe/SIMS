<template>
	<div class="paper">
		<v-header></v-header>
		<div class="personalInfo-container">
			<el-container style="height: 200px; border: 1px solid #eee">
				<el-header>
					<p-header></p-header>
				</el-header>
			</el-container>
			<el-container style="height: 500px;  border: 1px solid #eee">
				<el-aside style="font-size: 30px; width: 180px;">
					 <p-menu></p-menu>
				</el-aside>
				<el-main>
					<div>main</div>
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

</style>
