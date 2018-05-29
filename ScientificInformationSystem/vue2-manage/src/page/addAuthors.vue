<template>
    <div class="addDomain">
        <head-top></head-top>
        <header class="addDomain_title">新增作者</header>
        <div class="addDomain_content">
            <el-form ref="form" :model="form" label-width="100px" >
                <el-form-item 
                label="作者名字" prop="name" :rules="[{
                  required: true, message: '名字不能为空', trigger: 'blur'
                }]">
                    <el-input v-model="form.name"></el-input>
                </el-form-item>
                <el-form-item label="作者id" prop="uniid" :rules="[{
                  required: true, message: 'id不能为空', trigger: 'blur'
                }]">
                    <el-input v-model="form.uniid"></el-input>
                </el-form-item>
                <el-form-item label="机构" prop="organization" :rules="[{
                  required: true, message: '机构不能为空', trigger: 'blur'
                }]">
                    <el-input v-model="form.organization"></el-input>
                </el-form-item>
                <el-form-item label="头像地址">
                    <el-input v-model="form.avatar_src"></el-input>
                </el-form-item>
                <el-form-item
                    v-for="(edu_experience, index) in form.edu_experience"
                    :label="'教育经历' + index"
                    :key="edu_experience.key"
                    :prop="'edu_experience.' + index + '.value'"
                  >
                    <el-input v-model="edu_experience.value"></el-input><el-button @click.prevent="removeEdu_experience(edu_experience)">删除</el-button>
                    <el-button @click.prevent="addEdu_experience(edu_experience)">新增</el-button>
                </el-form-item>
                <el-form-item
                    v-for="(work_experience, index) in form.work_experience"
                    :label="'工作经历' + index"
                    :key="work_experience.key"
                    :prop="'work_experience.' + index + '.value'"
                  >
                    <el-input v-model="work_experience.value"></el-input><el-button @click.prevent="removeWork_experience(work_experience)">删除</el-button>
                    <el-button @click.prevent="addWork_experience(work_experience)">新增</el-button>
                </el-form-item>
                <el-form-item label="性别">
                    <el-select v-model="form.sex" placeholder="请选择性别">
                        <el-option label="男" value="男"></el-option>
                        <el-option label="女" value="女"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="所属领域">
                    <el-input v-model="form.domain"></el-input>
                </el-form-item>
                <el-form-item label="个人简介">
                    <el-input type="textarea" v-model="form.intro"></el-input>
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
                    uniid: '',
                    organization: '',
                    avatar_src: '',
                    sex: '',
                    intro: '',
                    domain: '',
                    edu_experience: [{
                        value: ''
                    }],
                    work_experience: [{
                        value: ''
                    }]
                },
            }
        },
        components: {
            headTop,
        },
        methods: {
            onSubmit() {       
                const t = this
                let {uniid, name, sex, organization, avatar_src, domain, intro} = t.form

                DB.Search.add_authors({
                     uniid, name, sex, organization, avatar_src, domain, intro,
                     work_experience: t.form.work_experience[0].value, 
                     edu_experience: t.form.edu_experience[0].value
                }).then(result=>{
                    console.log(result)
                    let { list = [] } = result
                    if (list[0].status == 1) {
                            this.$message({
                                type: 'success',
                                message: '添加成功'
                            });
                            this.$router.push('addAuthors')
                        }else{
                            this.$message({
                                type: 'error',
                                message: '添加失败'
                            });
                        }
                })
            },
            removeEdu_experience(item) {
                var index = this.form.edu_experience.indexOf(item)
                if (index !== -1) {
                  this.form.edu_experience.splice(index, 1)
                }
            },
            addEdu_experience() {
                this.form.edu_experience.push({
                  value: '',
                  key: Date.now()
                });
            },
            removeWork_experience(item) {
                var index = this.form.work_experience.indexOf(item)
                if (index !== -1) {
                  this.form.work_experience.splice(index, 1)
                }
            },
            addWork_experience() {
                this.form.work_experience.push({
                  value: '',
                  key: Date.now()
                });
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
