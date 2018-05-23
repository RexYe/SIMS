<template>
	<div class="interpersonalRelationshipNetwork">
		<v-header></v-header>
		<div class="interpersonalRelationshipNetwork-container">
			<el-container style="height: 180px; background-color: rgba(0,0,0,0)">
				<el-header>
					<organization-header :name=oheader[0] :website=oheader[1] :logo=oheader[2] :english_name=oheader[3] :location=oheader[4] ></organization-header>
				</el-header>
			</el-container>
			<el-container style="height: 100%;">
				<el-aside style="font-size: 30px; width: 180px;">
                    <organization-sidebar index="organizationPublishEveryYear"></organization-sidebar>
				</el-aside>
				<el-main>
					<d-header index="organizationPublishEveryYear"></d-header>
					<div id="charts"></div>
				</el-main>
			</el-container>
		</div>
	</div>
</template>

<script>
import header from 'components/header/header'
import echarts from 'echarts'
import organizationMenu from 'components/organization/organizationMenu'
import organizationInfoHeader from 'components/organization/organizationInfoHeader'
import organizationDataVisualizationHeader from 'components/organization/organizationDataVisualizationHeader'
import DB from '../../DB/db'

export default {
    data() {
    	return {
    		oheader: [],
            echartsYear: [],
            echartsSum: []
    	}
    },
    components: {
        'v-header': header,
        'organization-sidebar': organizationMenu,
        'organization-header': organizationInfoHeader,
        'd-header': organizationDataVisualizationHeader
    },
    beforeCreate: function(){
        let organizationName = localStorage.getItem("organizationName")
        this.$router.push({path: '/organizationPublishEveryYear'+'?'+'name='+organizationName})
    },
    methods: {
        drawPie (id) {
            this.chart = echarts.init(document.getElementById(id), 'roma');
            this.chart.setOption({
            backgroundColor: 'rgba(0,0,0,0)',
            title: {
                text: '年度总文献量',        
                textStyle: {
                    fontWeight: 'normal',
                    fontSize: 16,
                    color: '#F1F1F3'
                },
                left: '6%'
            },
            tooltip: {
                trigger: 'axis'
            },
            toolbox: {
                feature: {
                    dataView: {
                        show: true,
                        readOnly: false
                    },
                    restore: {
                        show: true
                    },
                    saveAsImage: {
                        show: true
                    }
                }
            },
            grid: {
                containLabel: true
            },
            legend: {
                data: ['数量'],
                textStyle: {
                    fontWeight: 'normal',
                    fontSize: 16,
                    color: '#F1F1F3'
                },
            },
            xAxis: [{
                type: 'category',
                axisTick: {
                    alignWithLabel: true
                },
                axisLabel: {
                    textStyle: {
                        color: '#F1F1F3'
                    }
                },
                axisLine:{
                    lineStyle:{
                        color:'#fff'
                    }
                },
                data: this.echartsYear
            }],
            yAxis: [{
                type: 'value',
                name: '数量',
                min: 0,
                max: this.yAxisMax,
                position: 'left',
                axisLabel: {
                    formatter: '{value}',
                    textStyle: {
                        color: '#F1F1F3'
                    }
                },
                axisLine:{
                    lineStyle:{
                        color:'#fff'
                    }
                },
            }],
            series: [{
                name: '数量',
                type: 'line',
                stack: '总量',
                    label: {
                        normal: {
                            show: true,
                            position: 'top',
                        }
                    },
                lineStyle: {
                        normal: {
                            width: 3,
                            shadowColor: 'rgba(0,0,0,0.4)',
                            shadowBlur: 10,
                            shadowOffsetY: 10
                        }
                    },
                data: this.echartsSum
            }]
            });
        }
    },
    mounted() {
        this.$nextTick(function() {
            setTimeout(()=>{
                this.drawPie('charts');
            },500)
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
        const t = this;
        DB.Search.get_organization_by_name({
            name: this.$route.query.name
        }).then(result=>{
            let { list = [] } = result;
            t.oheader.push(list[0].name, list[0].website, list[0].logo, list[0].english_name, list[0].location)
        });
        DB.Search.get_organization_publish_every_year_by_organization_name({
            name: this.$route.query.name
        }).then(result=>{
            //总坐标最大值为最大发表量适当加10
            t.yAxisMax = result.max + 10
            let { list = [] } = result;
            list.map(function(index, elem) {
                t.echartsYear.push(index.year)
                t.echartsSum.push(index.sum)
            }) 
        });
    },
}

</script>
<style scoped>
	.interpersonalRelationshipNetwork{
		width: 100%;
		height: 100%;
	}
	.interpersonalRelationshipNetwork-container{
		height: 100%;
		margin-top: 60px;
	}
	#charts{
		margin-top: 30px;
		width: 900px;
		height: 600px;
	}
</style>
