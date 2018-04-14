<template>
    <div class="addDomain">
        <head-top></head-top>
        <header class="addDomain_title">删除作者</header>
        <div class="addDomain_content">
            <el-table
    :data="tableData"
    style="width: 100%">
    <el-table-column
      label="姓名"
      width="180">
      <template slot-scope="scope">
        <i class="el-icon-time"></i>
        <span style="margin-left: 10px">{{ scope.row.date }}</span>
      </template>
    </el-table-column>
    <el-table-column
      label="领域名称"
      width="180">
      <template slot-scope="scope">
        <el-popover trigger="hover" placement="top">
          <p>名称: {{ scope.row.name }}</p>
          <p>简介: {{ scope.row.address }}</p>
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">{{ scope.row.name }}</el-tag>
          </div>
        </el-popover>
      </template>
    </el-table-column>
    <el-table-column label="操作">
      <template slot-scope="scope">
        <el-button
          size="mini"
          @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
        </div>
    </div>
</template>
<script>
    import headTop from '../components/headTop'
    export default {
    data() {
      return {
        tableData: [{
          date: '王万良',
          name: '计算机科学与技术',
          address: '计算机科学与技术是...'
        }, {
          date: '周杰伦',
          name: '人工智能',
          address: '人工智能是...'
        }]
      }
    },
    components: {
            headTop,
        },
    methods: {
      handleEdit(index, row) {
        console.log(index, row);
      },
      handleDelete(index, row) {
        console.log(index, row);
      }
    }
  }

</script>

<style lang="less">
    @import '../style/mixin';
    .addDomain_title{
        margin-top: 20px;
        .sc(24px, #666);
        text-align: center;
    }
    .addDomain_content{
        width: 60%;
        min-height: 400px;
        margin: 20px auto 0;
        border-radius: 10px;
        ul > li{
            padding: 20px;
            span{
                color: #666;
            }
        }
    }
</style>
