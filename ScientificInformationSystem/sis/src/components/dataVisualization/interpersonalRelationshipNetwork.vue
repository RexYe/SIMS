<template>
	<div class="interpersonalRelationshipNetwork">
		<v-header></v-header>
		<div class="interpersonalRelationshipNetwork-container">
			<el-container style="height: 180px; border: 1px solid #eee; background-color: #ffd04b">
				<el-header>
					<p-header name='王小' college="浙江工业大学"></p-header>
				</el-header>
			</el-container>
			<el-container style="height: 100%;  border: 1px solid #eee">
				<el-aside style="font-size: 30px; width: 180px;">
					 <p-menu index="interpersonalRelationshipNetwork"></p-menu>
				</el-aside>
				<el-main>
					<d-header index="interpersonalRelationshipNetwork"></d-header>
					<div id="charts"></div>
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
import dataVisualizationHeader from 'components/dataVisualization/dataVisualizationHeader'
export default {
  data() {
  	return {
  		
  	}
  },
  components: {
    'v-header': header,
    'p-header': personalInfoHeader,
    'p-menu': personMenu,
    'd-header': dataVisualizationHeader
  },
  methods: {
  	  drawPie (id) {
        this.chart = echarts.init(document.getElementById(id), 'roma');
        this.chart.setOption({
    //        backgroundColor: new echarts.graphic.RadialGradient(0.3, 0.3, 0.8, [{
    //     offset: 0,
    //     color: '#f7f8fa'
    // }, {
    //     offset: 1,
    //     color: '#cdd0d5'
    // }]),
    title: {
        text: "人际关系网络",
        subtext: "YQL",
        top: "top",
        left: "center"
    },
    tooltip: {},
    legend: [{
        formatter: function(name) {
            return echarts.format.truncateText(name, 40, '14px Microsoft Yahei', '…');
        },
        tooltip: {
            show: true
        },
        selectedMode: 'false',
        bottom: 20,
        data: ['王小', '张三', '李四']
    }],
    toolbox: {
        show: true,
        feature: {
            dataView: {
                show: true,
                readOnly: true
            },
            restore: {
                show: true
            },
            saveAsImage: {
                show: true
            }
        }
    },
    animationDuration: 3000,
    animationEasingUpdate: 'quinticInOut',
    series: [{
        name: '王小',
        type: 'graph',
        layout: 'force',

        force: {
            repulsion: 300
        },
        data: [{
            "name": "王小",
            "symbolSize": 30,
            "draggable": "true",
            "value": 27

        }, {
            "name": "张三",
            "value": 15,
            "symbolSize": 10,
            "category": "张三",
            "draggable": "true"
        }, {
            "name": "李四",
            "value": 60,
            "symbolSize": 10,
            "category": "李四",
            "draggable": "true"
        }, {
            "name": "林五",
            "symbolSize": 3,
            "category": "李四",
            "draggable": "true",
            "value": 1
        }],
        links: [{
            "source": "王小",
            "target": "张三"
        }, {
            "source": "王小",
            "target": "李四"
        }, {
            "source": "王小",
            "target": "林五"
        }],
        categories: [{
            'name': '王小'
        }, {
            'name': '张三'
        }, {
            'name': '李四'
        },{

        }],
        focusNodeAdjacency: true,
        roam: true,
        label: {
            normal: {
                show: true,
                position: 'top',

            }
        },
        lineStyle: {
            normal: {
                color: 'source',
                curveness: 0,
                type: "solid"
            }
        }
    }]
        });
      }
  },
	mounted() {
	  this.$nextTick(function() {
	    this.drawPie('charts');
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
		height: 900px;
		margin-top: 70px;
	}
	#charts{
		margin-top: 30px;
		width: 800px;
		height: 700px;
	}
</style>
