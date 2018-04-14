<template>
    <div class="addDomain">
        <head-top></head-top>
        <header class="addDomain_title">新增领域</header>
        <div class="addDomain_content">
            <el-form ref="form" :model="form" label-width="80px">
            <el-form-item label="领域名称">
                <el-input v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item label="领域大类">
                <el-select v-model="form.region" placeholder="请选择领域大类">
                    <el-option label="计算机科学" value="shanghai"></el-option>
                    <el-option label="人工智能" value="beijing"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="即时上线">
                <el-switch v-model="form.delivery"></el-switch>
            </el-form-item>
            <el-form-item label="备注">
                <el-input type="textarea" v-model="form.desc"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit">立即创建</el-button>
                <el-button>取消</el-button>
            </el-form-item>
        </el-form>
        </div>
    </div>
</template>
<script>
    import headTop from '../components/headTop'
    export default {
        data() {
            return {
                form: {
                    name: '',
                    region: '',
                    date1: '',
                    date2: '',
                    delivery: false,
                    type: [],
                    resource: '',
                    desc: ''
                }
            }
        },
        components: {
            headTop,
        },
        methods: {
            onSubmit() {
                console.log('submit!');
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
