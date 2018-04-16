<template>
	<div class="interpersonalRelationshipNetwork">
		<v-header></v-header>
		<div class="interpersonalRelationshipNetwork-container">
			<p>人际关系网络</p>
			<div id="interpersonalRelationshipNetwork"></div>
		</div>
	</div>
</template>

<script>
import header from 'components/header/header'
import echarts from 'echarts'

export default {
  data() {
  },
  components: {
    'v-header': header
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
