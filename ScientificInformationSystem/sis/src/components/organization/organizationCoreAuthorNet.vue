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
					<d-header index="organizationCoreAuthorNet"></d-header>
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
            echartsData: [],
            echartsLinks: [],
            echartsAuthorList :[],
            echartsAuthorListWithName: [],
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
        this.$router.push({path: '/organizationCoreAuthorNet'+'?'+'name='+organizationName})
    },
    methods: {
        drawPie (id) {
            this.chart = echarts.init(document.getElementById(id), 'roma');
            this.chart.setOption({
            backgroundColor: 'rgba(0,0,0,0)',
                title: {
                    text: "核心作者合作关系网络",
                    top: "top",
                    left: "center",
                    textStyle: {
                        fontWeight: 'normal',
                        fontSize: 16,
                        color: '#F1F1F3'
                    },
                },
                tooltip: {},
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
                    name: '核心作者',
                    type: 'graph',
                    layout: 'force',
                    force: {
                        repulsion: 300
                    },
                    data: this.echartsData,
                    links: this.echartsLinks,
                    // categories: this.echartsAuthorListWithName,
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
                            color: 'green',
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
            setTimeout(()=>{
                this.drawPie('charts');
            },2500)
            var that = this;
            var resizeTimer = null;
            window.onresize = function() {
                if (resizeTimer) clearTimeout(resizeTimer);
                resizeTimer = setTimeout(function() {
                    that.drawPie('charts');
                }, 300);
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
        DB.Search.get_organization_core_author_net_by_organization_name({
            name: this.$route.query.name
        }).then(result=>{
            // console.log(result);
            let { list = [] } = result;
            let { links = [] } = result;
            // let { echarts_author_list_with_name = [] } = result;
            t.echartsLinks = links;
            t.echartsData = list;
            // console.log(t.echartsLinks)
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
		width: 900px;
		height: 600px;
	}
</style>
