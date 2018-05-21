<template>
    <div class="journalDataVisualization-header">
        <el-menu :default-active="index" class="el-menu-demo" mode="horizontal" background-color="rgba(0,0,0,0)"
              text-color="#fff"
              active-text-color="#ffd04b" router>
            <el-menu-item index="journalPublishEveryYear">年度出版概况</el-menu-item>
            <el-menu-item index="journalKeyWord">关键词分布</el-menu-item>
            <el-menu-item index="journalAuthorRank">作者贡献情况</el-menu-item>
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