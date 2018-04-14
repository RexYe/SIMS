<template>
    <div class="addDomain">
        <head-top></head-top>
        <header class="addDomain_title">项目管理</header>
        <div class="addDomain_content">
            <el-form ref="form" :model="form" label-width="80px">
            <el-form-item label="作者名字">
                <el-input v-model="form.name"></el-input>
            </el-form-item>
            <el-form-item label="性别">
                <el-select v-model="form.region" placeholder="请选择性别">
                    <el-option label="男" value="man"></el-option>
                    <el-option label="女" value="women"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="所属领域">
                <el-checkbox-group v-model="form.type">
                <el-checkbox label="计算机科学与技术" name="type"></el-checkbox>
                <el-checkbox label="人工智能" name="type"></el-checkbox>
                <el-checkbox label="机器学习" name="type"></el-checkbox>
                <el-checkbox label="物联网" name="type"></el-checkbox>
                </el-checkbox-group>
            </el-form-item>
            <el-form-item label="个人简介">
                <el-input type="textarea" v-model="form.desc"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="onSubmit">立即新增</el-button>
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
