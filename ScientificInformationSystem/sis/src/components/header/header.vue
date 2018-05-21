<template>
    <div class="Header">
        <img src="../../assets/img/logo.png" height="70" width="70">
        <div class="Header-container" >
            <el-input placeholder="请输入内容" v-model="searchKey" class="input-with-select">
                <el-select v-model="select" slot="prepend" placeholder="请选择">
                    <el-option label="作者" value="1"></el-option>
                    <el-option label="期刊" value="2"></el-option>
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
        background: #101010;
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
    .Header .el-input-group__prepend{
        background-color: #101010;
    }
    .Header-container{
        /*margin: 0 auto;*/
        width: 35%;

    }
    .el-select .el-input {
        width: 90px;
        color: white;
    }
    .input-with-select .el-input-group__prepend {
        background: rgba(255,255,255,0.175);
        border: 1px solid rgba(255,255,255,0.175);
    }
    .input-with-select .el-input__inner{
        background: rgba(255,255,255,0.175);
        border: 1px solid rgba(255,255,255,0.175);
        color: white;

    }
    .input-with-select .el-input-group__append {
        background: rgba(255,255,255,0.175);
        border: 1px solid rgba(255,255,255,0.175);
    }
    .input-with-select .el-scrollbar{
        background: rgba(255,255,255,0.175);
        border: 1px solid rgba(255,255,255,0.175);
    }
    .Header .el-select-dropdown  {
        background: rgba(255,255,255,0.175);
        border: 1px solid rgba(255,255,255,0.175);

    }
    .Header .el-popper{
        background: rgba(255,255,255,0.175);
        border: 1px solid rgba(255,255,255,0.175);

    }
</style>
<script>
import DB from '../../DB/db'
export default {
    data() {
        return {
            searchKey: '',
            select: '1'
        }
    },
    created() {},
    methods: {
        search: function() {
            const t = this;
            console.log('select:',t.select, 'searchKey:',t.searchKey);
            t.query_obj = this.searchKey
            if (t.select == 1) {
                this.$router.push({path: '/search'+'?'+'name='+t.query_obj});
            }
            else if (t.select == 2) {
                this.$router.push({path: '/searchJournal'+'?'+'name='+t.query_obj});
            }
            else if (t.select == 3) {
                this.$router.push({path: '/searchOrganization'+'?'+'name='+t.query_obj});
            }
            location.reload();
        }
    }
}
</script>