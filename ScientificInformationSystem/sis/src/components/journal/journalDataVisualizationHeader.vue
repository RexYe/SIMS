<template>
    <div class="journalDataVisualization-header">
        <el-menu :default-active="index" class="el-menu-demo" mode="horizontal" router>
            <el-menu-item index="journalPublishEveryYear">年度出版概况</el-menu-item>
            <el-menu-item index="domainDistribution">领域分布</el-menu-item>
            <el-menu-item index="focus">影响情况</el-menu-item>
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