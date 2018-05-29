<template>
    <div class="addDomain">
        <head-top></head-top>
        <header class="addDomain_title">新增机构</header>
        <div class="addDomain_content">
            <el-form ref="form" :model="form" label-width="100px" >
                <el-form-item 
                label="机构名称" prop="name" :rules="[{
                  required: true, message: '名字不能为空', trigger: 'blur'
                }]">
                    <el-input v-model="form.name"></el-input>
                </el-form-item>
                <el-form-item 
                label="机构英文名称" prop="english_name" :rules="[{
                  required: true, message: '名字不能为空', trigger: 'blur'
                }]">
                    <el-input v-model="form.english_name"></el-input>
                </el-form-item>
                <el-form-item label="logo地址">
                    <el-input v-model="form.logo"></el-input>
                </el-form-item>
                <el-form-item label="官方网站">
                    <el-input v-model="form.website"></el-input>
                </el-form-item>
                <el-form-item label="地址">
                    <el-input v-model="form.location"></el-input>
                </el-form-item>
                <el-form-item label="机构简介">
                    <el-input type="textarea" v-model="form.introduction"></el-input>
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
    import DB from '../DB/db.js'
    export default {
        data() {
            return {
                form: {
                    name: '',
                    english_name: '',
                    logo: '',
                    location: '',
                    introduction: '',
                    website: '',
                },
            }
        },
        components: {
            headTop,
        },
        methods: {
            onSubmit() {       
                const t = this
                let {name,english_name,logo,location,introduction,website} = t.form

                DB.Search.add_organization({
                     name,english_name,logo,location,introduction,website
                }).then(result=>{
                    console.log(result)
                    let { list = [] } = result
                     if (list[0].status == 1) {
                            this.$message({
                                type: 'success',
                                message: '添加成功'
                            });
                            this.$router.push('addOrganization')
                        }else{
                            this.$message({
                                type: 'error',
                                message: '添加失败'
                            });
                        }
                })
            },

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
