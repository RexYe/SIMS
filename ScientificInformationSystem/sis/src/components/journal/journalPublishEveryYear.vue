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
					<d-header index="journalPublishEveryYear"></d-header>
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
            echartsYear: [],
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
        this.$router.push({path: '/journalPublishEveryYear'+'?'+'name='+journalName})
    },
    methods: {
        drawPie (id) {
            this.chart = echarts.init(document.getElementById(id), 'roma');
            this.chart.setOption({
             title: {
                text: '年度总文献量'
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
                data: ['数量']
            },
            xAxis: [{
                type: 'category',
                axisTick: {
                    alignWithLabel: true
                },
                data: this.echartsYear
            }],
            yAxis: [{
                type: 'value',
                name: '数量',
                min: 0,
                max: 50,
                position: 'left',
                axisLabel: {
                    formatter: '{value}'
                }
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
            console.log('nexttick')
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
        DB.Search.get_journal_publish_every_year_by_journal_name({
            name: this.$route.query.name
        }).then(result=>{
            let { list = [] } = result;
            list.map(function(index, elem) {
                t.echartsYear.push(index.publish_time)
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
