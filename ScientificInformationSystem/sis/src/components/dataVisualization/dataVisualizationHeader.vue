<template>
    <div class="dataVisualization-header">
        <el-menu :default-active="index" class="el-menu-demo" mode="horizontal" router>
                <el-menu-item index="interpersonalRelationshipNetwork">人际关系网络</el-menu-item>
                <el-menu-item index="focus">领域分布</el-menu-item>
                <el-menu-item index="3">影响情况</el-menu-item>
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