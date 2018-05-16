<template>
	<div class="interpersonalRelationshipNetwork">
		<v-header></v-header>
		<div class="interpersonalRelationshipNetwork-container">
			<el-container style="height: 180px; border: 1px solid #eee; background-color: #FAFAFA">
				<el-header>
					
				</el-header>
			</el-container>
			<el-container style="height: 100%;  border: 1px solid #eee">
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
    		pheader: [],
            echartsData: [],
    	}
    },
    components: {
        'v-header': header,
        'journal-sidebar': journalMenu,
        'journalinfo-header': journalInfoHeader,
        'd-header': journalDataVisualizationHeader
    },
    beforeCreate: function(){
        let paperName = localStorage.getItem("paperName")
        this.$router.push({path: '/journalPublishEveryYear'+'?'+'name='+paperName})
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
                data: ['增速']
            },
            xAxis: [{
                type: 'category',
                axisTick: {
                    alignWithLabel: true
                },
                data: ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016']
            }],
            yAxis: [{
                type: 'value',
                name: '增速',
                min: 0,
                max: 50,
                position: 'right',
                axisLabel: {
                    formatter: '{value} %'
                }
            }],
            series: [{
                name: '增速',
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
                data: [1,13,37,35,15,13,25,21,6,45,32,2,4,13,6,4,11]
            }]
            });
        }
    },
    mounted() {
        console.log('mounted')
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
        console.log('cteated')
        const t = this
        // DB.Search.get_personalinfo_by_uniid({
        //     uniid: this.$route.query.uniid
        // }).then(result=>{
        //     let { list = [] } = result;
        //     t.pheader.push(list[0].name, list[0].organization, list[0].avatar_src)    
        // });
        // DB.Search.get_interpersonal_relationship_network_by_uniid({
        //     uniid: this.$route.query.uniid
        // }).then(result=>{
        //     let { list = [] } = result;
        //     let { links = [] } = result;
        //     let { author_list = [] } = result;
        //     let { author_list_with_name = [] } = result;
           
        //     t.echartsData = list;
        //     t.echartsLinks = links;
        //     t.echartsAuthorList = author_list;
        //     t.echartsAuthorListWithName = author_list_with_name;
        //     t.mainAuthor = result.mainAuthor;
        // })
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
		margin-top: 60px;
	}
	#charts{
		margin-top: 30px;
		width: 1000px;
		height: 750px;
	}
</style>
