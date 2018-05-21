<template>
    <div class="journal-Menu">
         <el-menu
              :default-active="index"
              background-color="#545c64"
              text-color="#fff"
              active-text-color="#ffd04b"
              style="height: 700px"
              router>
             <el-menu-item index="organizationInfo">
                <i class="el-icon-menu"></i>
                <span slot="title">机构简介</span>
              </el-menu-item>
              <el-menu-item index="organizationPaper">
                <i class="el-icon-menu"></i>
                <span slot="title">论文情况</span>
              </el-menu-item>
              <el-menu-item index="organizationPublishEveryYear">
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