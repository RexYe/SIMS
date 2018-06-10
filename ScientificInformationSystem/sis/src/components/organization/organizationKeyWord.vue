<template>
	<div class="interpersonalRelationshipNetwork">
		<v-header></v-header>
		<div class="interpersonalRelationshipNetwork-container">
			<el-container style="height: 180px;background-color: rgba(0,0,0,0)">
				<el-header>
					<organization-header :name=oheader[0] :website=oheader[1] :logo=oheader[2] :english_name=oheader[3] :location=oheader[4] ></organization-header>
				</el-header>
			</el-container>
			<el-container style="height: 100%;">
				<el-aside style="font-size: 30px; width: 180px;">
					  <organization-sidebar index="organizationPublishEveryYear"></organization-sidebar>
				</el-aside>
				<el-main>
					<d-header index="organizationKeyWord"></d-header>
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
            echartsKeyword: [],
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
        this.$router.push({path: '/organizationKeyWord'+'?'+'name='+organizationName})
    },
    methods: {
        drawPie (id) {
            this.chart = echarts.init(document.getElementById(id), 'roma');
            this.chart.setOption({
               backgroundColor: 'rgba(0,0,0,0)',
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                title: {
                    text: '关键词分布',        
                    textStyle: {
                        fontWeight: 'normal',
                        fontSize: 16,
                        color: '#F1F1F3'
                    },
                    left: '6%'
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
                    type: 'value',
                    axisLabel: {
                        formatter: '{value}'
                    },
                    axisLine: {
                        show: false,
                        lineStyle: {
                            color: "#00c7ff",
                            width: 1,
                            type: "solid"
                        },
                    },
                    axisTick: {
                        show: false
                    },
                    splitLine: {
                        lineStyle: {
                            color: "#063374",
                        }
                    }
                }],
                yAxis: [{
                    type: 'category',
                    data: this.echartsKeyword,
                    axisLine: {
                        show: true,
                        lineStyle: {
                            color: "#063374",
                            width: 1,
                            type: "solid"
                        }
                    },
                    axisTick: {
                        show: false
                    },
                    axisLabel: {
                        show: true,
                        textStyle: {
                            color: "#00c7ff",
                        }
                    },
                }],
                series: [{
                    type: 'bar',
                    data: this.echartsSum,
                    barWidth: 20, //柱子宽度
                    barGap: 20, //柱子之间间距
                   
                    itemStyle: {
                        normal: {
                            color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [{
                                offset: 0,
                                color: '#00fcae'
                            }, {
                                offset: 1,
                                color: '#006388'
                            }]),
                            opacity: 1,
                            barBorderRadius: 7
                        },
                        emphasis: {
                            barBorderRadius: 7
                        },
                    }
                }]
            });
        }
    },
    mounted() {
        this.$nextTick(function() {
            setTimeout(()=>{
                this.drawPie('charts');
            },1500)
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
        DB.Search.get_organization_keyword_by_organization_name({
            name: this.$route.query.name
        }).then(result=>{
            let { list = [] } = result;
            console.log(list);
            list.map(function(index, elem) {
                t.echartsKeyword.push(index.keyword)
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
