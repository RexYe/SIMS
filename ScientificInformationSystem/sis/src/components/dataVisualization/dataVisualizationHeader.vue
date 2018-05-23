<template>
    <div class="dataVisualization-header">
        <el-menu :default-active="index" class="el-menu-demo" mode="horizontal" 
               background-color="rgba(0,0,0,0)"
              text-color="#fff"
              active-text-color="#ffd04b" router>
            <el-menu-item index="interpersonalRelationshipNetwork">人际关系网络</el-menu-item>
            <!-- <el-menu-item index="domainDistribution">领域分布</el-menu-item> -->
        </el-menu>
    </div>
</template>
<style>

</style>
<script>
export default {
  props: {
    index: String
  },
  data() {
    return {

    }
  }
}
</script>