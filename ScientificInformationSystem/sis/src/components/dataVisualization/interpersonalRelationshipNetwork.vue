<template>
	<div class="interpersonalRelationshipNetwork">
		<v-header></v-header>
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
					<div>人际关系网络
					<div class="interpersonalRelationshipNetwork-container">
			<div id="interpersonalRelationshipNetwork"></div>
		</div></div>
				</el-main>
			</el-container>
		
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
  	  drawPie (id) {
        this.chart = echarts.init(document.getElementById(id), 'roma');
        this.chart.setOption({
           title: {
                text: 'ECharts 入门示例'
            },
            tooltip: {},
            legend: {
                data:['销量']
            },
            xAxis: {
                data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
            },
            yAxis: {},
            series: [{
                name: '销量',
                type: 'bar',
                data: [5, 20, 36, 10, 10, 20]
            }]
        });
      }
  },
	mounted() {
	  this.$nextTick(function() {
	    this.drawPie('interpersonalRelationshipNetwork');
	    var that = this;
	    var resizeTimer = null;
	    window.onresize = function() {
	      if (resizeTimer) clearTimeout(resizeTimer);
	      resizeTimer = setTimeout(function() {
	        that.drawPie('interpersonalRelationshipNetwork');
	      }, 100);
	    }
	  });
	}
}

</script>
<style scoped>
	.interpersonalRelationshipNetwork{
		width: 100%;
		height: 100%;
	}
	.interpersonalRelationshipNetwork-container{
		width: 500px;
		height: 900px;
		margin-top: 90px;
	}
</style>
