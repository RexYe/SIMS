<template>
	<div class="interpersonalRelationshipNetwork">
		<v-header></v-header>
		<div class="interpersonalRelationshipNetwork-container">
			<el-container style="height: 180px; background: rgba(0,0,0,0)">
				<el-header>
					<!-- <p-header name='王小' college="浙江工业大学"></p-header> -->
                    <p-header :name=pheader[0] :college=pheader[1] :avatar_src=pheader[2]></p-header>
				</el-header>
			</el-container>
			<el-container style="height: 100%;">
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
import DB from '../../DB/db'

export default {
    data() {
    	return {
    		pheader: [],
            echartsData: [],
            echartsLinks: [],
            echartsAuthorList :[],
            echartsAuthorListWithName: [],
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
        this.$router.push({path: '/interpersonalRelationshipNetwork'+'?'+'uniid='+uniid})
    },
    methods: {
        drawPie (id) {
            this.chart = echarts.init(document.getElementById(id), 'roma');
            this.chart.setOption({
                backgroundColor: 'rgba(0,0,0,0)',
                title: {
                    text: "人际关系网络",
                    subtext: "YQL",
                    top: "top",
                    left: "center"
                },
                tooltip: {},
                // legend: [{
                //     formatter: function(name) {
                //         return echarts.format.truncateText(name, 40, '14px Microsoft Yahei', '…');
                //     },
                //     tooltip: {
                //         show: true
                //     },
                //     selectedMode: 'false',
                //     bottom: 20,
                //     data: this.echartsAuthorList
                // }],
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
                    name: this.mainAuthor,
                    type: 'graph',
                    layout: 'force',
                    force: {
                        repulsion: 300
                    },
                    data: this.echartsData,
                    links: this.echartsLinks,
                    categories: this.echartsAuthorListWithName,
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
        DB.Search.get_personalinfo_by_uniid({
            uniid: this.$route.query.uniid
        }).then(result=>{
            let { list = [] } = result;
            t.pheader.push(list[0].name, list[0].organization, list[0].avatar_src)    
        });
        DB.Search.get_interpersonal_relationship_network_by_uniid({
            uniid: this.$route.query.uniid
        }).then(result=>{
            let { list = [] } = result;
            let { links = [] } = result;
            let { author_list = [] } = result;
            let { author_list_with_name = [] } = result;
           
            t.echartsData = list;
            t.echartsLinks = links;
            t.echartsAuthorList = author_list;
            t.echartsAuthorListWithName = author_list_with_name;
            t.mainAuthor = result.mainAuthor;
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
		height: 100%;
		margin-top: 60px;
	}
	#charts{
		margin-top: 30px;
		width: 1000px;
		height: 750px;
	}
</style>
