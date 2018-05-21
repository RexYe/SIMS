<template>
    <div class="journal-Menu">
         <el-menu
              :default-active="index"
              background-color="#545c64"
              text-color="#fff"
              active-text-color="#ffd04b"
              style="height: 700px"
              router>
             <el-menu-item index="journalInfo">
                <i class="el-icon-menu"></i>
                <span slot="title">期刊简介</span>
              </el-menu-item>
              <el-menu-item index="journalPaper">
                <i class="el-icon-menu"></i>
                <span slot="title">论文情况</span>
              </el-menu-item>
              <el-menu-item index="journalPublishEveryYear">
                <i class="el-icon-document"></i>
                <span slot="title">数据可视化</span>
              </el-menu-item>
            </el-menu>
    </div>
</template>
<style>
  .person-Menu{

  }
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