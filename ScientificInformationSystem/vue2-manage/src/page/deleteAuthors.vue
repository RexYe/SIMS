<template>
    <div class="addDomain">
        <head-top></head-top>
        <header class="addDomain_title">删除作者</header>
        <div class="addDomain_content">
            <el-table
    :data="authorsData"
    style="width: 100%">
    <el-table-column
      label="姓名"
      width="130">
      <template slot-scope="scope">
        <img class="avatar" :src=scope.row.avatar_src>
        <span>{{ scope.row.name }}</span>
      </template>
    </el-table-column>
      <el-table-column
      label="机构"
      width="160">
      <template slot-scope="scope">
        <span style="margin-left: 10px">{{ scope.row.organization }}</span>
      </template>
    </el-table-column>
    <el-table-column
      label="性别"
      width="70">
      <template slot-scope="scope">
          <div slot="reference" class="name-wrapper">
            <el-tag size="medium">{{ scope.row.sex }}</el-tag>
          </div>
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
    import DB from '../DB/db.js'
    export default {
    data() {
      return {
        authorsData: [],
      }
    },
    components: {
            headTop,
        },
    created: function() {
      const t = this
      DB.Search.get_authors_list({
      }).then(result=>{
          let { list = [] } = result;
          for(let i=0 ; i<list.length; i++){
            t.authorsData.push(list[i])
          }    
      }).then(()=>{
        t.loading = false;
      })
  },
    methods: {
      handleEdit(index, row) {
        console.log(index, row);
      },
      handleDelete(index, row) {
        console.log(index, row);
       DB.Search.delete_author_by_uniid({
        uniid: row.uniid
      }).then(result=>{
             console.log(result)
                    let { list = [] } = result
                    if (list[0].status == 1) {
                            this.$message({
                                type: 'success',
                                message: '删除成功'
                            });
                            this.$router.push('deleteAuthors')
                            location.reload();
                        }else{
                            this.$message({
                                type: 'error',
                                message: '删除失败'
                            });
                        }  
      })
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
    .avatar{
      width: 30px;
      height: 30px;
      border-radius: 50%;
    }
</style>
