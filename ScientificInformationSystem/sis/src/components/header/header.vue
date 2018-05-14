<template>
    <div class="Header">
        <img src="../../assets/img/logo.png" height="70" width="70">
        <div class="Header-container" >
            <el-input placeholder="请输入内容" v-model="searchKey" class="input-with-select">
                <el-select v-model="select" slot="prepend" placeholder="请选择">
                    <el-option label="作者名" value="1"></el-option>
                    <el-option label="论文名" value="2"></el-option>
                    <el-option label="机构" value="3"></el-option>
                </el-select>
                <el-button slot="append" icon="el-icon-search" @click="search"></el-button>
            </el-input>
        </div>
        <a href="https://github.com/RexYe/SIMS">
            <i class="el-icon-menu"></i>
        </a>
    </div>
</template>
<style>
    .Header{
        width: 100%;
        height: 60px;
        position: fixed;
        top: 0;
        background: white;
        box-shadow: 0 2px 4px -1px rgba(0, 0, 0, 0.2), 0 4px 5px 0 rgba(0, 0, 0, 0.14), 0 1px 10px 0 rgba(0, 0, 0, 0.12);
        z-index: 1000;
        opacity: 0.99;
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        align-items: center;
    }
    img{
        
    }
    .Header-container{
        /*margin: 0 auto;*/
        width: 35%;

    }
    .el-select .el-input {
        width: 90px;
    }
    .input-with-select .el-input-group__prepend {
        background-color: #fff;
    }
</style>
<script>
import DB from '../../DB/db'
export default {
    data() {
        return {
            searchKey: '',
            select: ''
        }
    },
    created() {},
    methods: {
        search: function() {
            // console.log('select:',this.select, 'searchKey:',this.searchKey);
            const t = this;
            t.query_obj = this.searchKey
            this.$router.push({path: '/search'+'?'+'name='+t.query_obj})
            location.reload();
        }
    }
}
</script>