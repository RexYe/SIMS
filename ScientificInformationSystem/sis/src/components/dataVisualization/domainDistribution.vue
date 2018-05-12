<template>
	<div class="interpersonalRelationshipNetwork">
		<v-header></v-header>
		<div class="interpersonalRelationshipNetwork-container">
			<el-container style="height: 180px; border: 1px solid #eee; background-color: #ffd04b">
				<el-header>
					<!-- <p-header name='王小' college="浙江工业大学"></p-header> -->
          <p-header :name=pheader[0] :college=pheader[1] :avatar_src=pheader[2]></p-header>
				</el-header>
			</el-container>
			<el-container style="height: 100%;  border: 1px solid #eee">
				<el-aside style="font-size: 30px; width: 180px;">
					 <p-menu index="interpersonalRelationshipNetwork"></p-menu>
				</el-aside>
				<el-main>
					<d-header index="domainDistribution"></d-header>
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
import DB from '../../DB/db'

export default {
  data() {
  	return {
  		pheader: []
  	}
  },
  components: {
    'v-header': header,
    'p-header': personalInfoHeader,
    'p-menu': personMenu,
    'd-header': dataVisualizationHeader
  },
    beforeCreate: function(){
    let uniid = localStorage.getItem("uniid")
    this.$router.push({path: '/domainDistribution'+'?'+'uniid='+uniid})
  },
  methods: {
  	  drawPie (id) {
        this.chart = echarts.init(document.getElementById(id), 'roma');
        this.chart.setOption({
            title : {
        text: '领域分布图',
        subtext: 'YQL',
        x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
        x : 'center',
        y : 'bottom',
        data:['人工智能','深度学习','大数据']
    },
    toolbox: {
        show : true,
        feature : {
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            magicType : {
                show: true,
                type: ['pie', 'funnel']
            },
            restore : {show: true},
            saveAsImage : {show: true}
        }
    },
    calculable : true,
    series : [
        {
            name:'面积模式',
            type:'pie',
            radius : [30, 110],
            center : ['50%', '50%'],
            roseType : 'area',
            data:[
               {value:10, name:'人工智能'},
                {value:5, name:'深度学习'},
                {value:15, name:'大数据'}
            ]
        }
    ]
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
	},
    created: function() {
    const t = this
    DB.Search.get_personalinfo_by_uniid({
      uniid: this.$route.query.uniid
    }).then(result=>{
        let { list = [] } = result;
        t.pheader.push(list[0].name, list[0].organization, list[0].avatar_src)    
    })
  },

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
