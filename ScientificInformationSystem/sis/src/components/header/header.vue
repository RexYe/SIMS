<template lang="html">
    <div class="nav">
        <div class="nav-container">
              <el-input placeholder="请输入内容" v-model="input5" class="input-with-select">
                  <el-select v-model="select" slot="prepend" placeholder="请选择">
                      <el-option label="餐厅名" value="1"></el-option>
                      <el-option label="订单号" value="2"></el-option>
                      <el-option label="用户电话" value="3"></el-option>
                  </el-select>
                <el-button slot="append" icon="el-icon-search"></el-button>
              </el-input>
        </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      input5: '',
      select: ''
    }
  }
}

</script>

<style scoped>
  .nav{
    position: fixed;
    background-color: orange;
    width: 100%;
    height: 110px;
  }
  .el-select .el-input {
    width: 130px;
  }
</style>
