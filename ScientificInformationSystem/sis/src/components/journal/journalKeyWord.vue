<template>
	<div class="interpersonalRelationshipNetwork">
		<v-header></v-header>
		<div class="interpersonalRelationshipNetwork-container">
			<el-container style="height: 180px; background-color: rgba(0,0,0,0)">
				<el-header>
					<journalinfo-header :name=jheader[0] :website=jheader[1] :logo=jheader[2] :english_name=jheader[3] :honor=jheader[4] :complex_influence=jheader[5] :comprehensive_influence=jheader[6]></journalinfo-header>
				</el-header>
			</el-container>
			<el-container style="height: 100%;">
				<el-aside style="font-size: 30px; width: 180px;">
					 <journal-sidebar index="journalPublishEveryYear"></journal-sidebar>
				</el-aside>
				<el-main>
					<d-header index="journalKeyWord"></d-header>
					<div id="charts"></div>
				</el-main>
			</el-container>
		</div>
	</div>
</template>

<script>
import header from 'components/header/header'
import echarts from 'echarts'
import journalMenu from 'components/journal/journalMenu'
import journalInfoHeader from 'components/journal/journalInfoHeader'
import journalDataVisualizationHeader from 'components/journal/journalDataVisualizationHeader'
import DB from '../../DB/db'

export default {
    data() {
    	return {
    		jheader: [],
            echartsKeyword: [],
            echartsSum: []
    	}
    },
    components: {
        'v-header': header,
        'journal-sidebar': journalMenu,
        'journalinfo-header': journalInfoHeader,
        'd-header': journalDataVisualizationHeader
    },
    beforeCreate: function(){
        let journalName = localStorage.getItem("journalName")
        this.$router.push({path: '/journalKeyWord'+'?'+'name='+journalName})
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
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: '#00fcae'
                            }, {
                                offset: 1,
                                color: '#006388'
                            }]),
                            opacity: 1,
                        }
                    }
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
        const t = this
        DB.Search.get_journal_by_name({
            name: this.$route.query.name
        }).then(result=>{
            let { list = [] } = result;
            let honor_arr = list[0].honor.split(';')
            t.jheader.push(list[0].name, list[0].website, list[0].logo, list[0].english_name, honor_arr, list[0].complex_influence, list[0].comprehensive_influence)
            t.intro.push(list[0].introduction)     
            t.host_unit.push(list[0].host_unit) 
        }).then(()=>{
            t.loading = false;
        })
        DB.Search.get_journal_keyword_by_journal_name({
            name: this.$route.query.name
        }).then(result=>{
            let { list = [] } = result;
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
