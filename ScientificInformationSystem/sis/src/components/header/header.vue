<template>
    <div class="Header">
        <div class="Header-container" style="margin-top: 15px;">
            <el-input placeholder="请输入内容" v-model="searchKey" class="input-with-select">
                <el-select v-model="select" slot="prepend" placeholder="请选择">
                    <el-option label="作者名" value="1"></el-option>
                    <el-option label="论文名" value="2"></el-option>
                    <el-option label="机构" value="3"></el-option>
                </el-select>
                <el-button slot="append" icon="el-icon-search" @click="search"></el-button>
            </el-input>
        </div>
    </div>
</template>
<style>
    .Header{
        width: 100%;
        height: 70px;
        position: fixed;
        top: 0;
        background: white;
        box-shadow: 1px 1px 5px black;
        z-index: 1000;
        opacity: 0.99;
    }
    .Header-container{
        margin: 0 auto;
        width: 40%;
    }
    .el-select .el-input {
        width: 90px;
    }
    .input-with-select .el-input-group__prepend {
        background-color: #fff;
    }
</style>
<script>
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
            console.log(this.select, this.searchKey);
            this.$router.push({path: '/search'})
        }
    }
}
</script>