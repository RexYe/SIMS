<template>
    <div class="personalInfo-header">
        <div class="personal-avatar">
            <img :src=avatar_src>
        </div>
        <div class="personal-world-info">
            <p id="name">{{name}}</p>
            <p id="organization">{{college}}</p>
            <p id="country"><i class="el-icon-location"></i>中国</p>
        </div>
    </div>
</template>
<style>
    .personalInfo-header {
        height: 180px;
        display: flex;
        flex-direction: row;
        align-items: center;
    }
    .personalInfo-header .personal-avatar{
        width: 100px;
        height: 100px;
        border-radius: 50%;
        overflow: hidden;
    }
    .personalInfo-header .personal-avatar img{
        width: 100%;
        height: 100%;
    }
    .personal-world-info{
        width: 200px;
        height: 100px;
        margin-left: 20px;
    }
    .personal-world-info #name {
        font-size: 40px;
        margin-bottom: 15px;
    }
    .personal-world-info #organization{
        margin-bottom: 8px;
    }
    .personal-world-info #country {
        font-size: 14px;
        color: #8F8B8B;
    }
</style>
<script>
export default {
  props: {
    name: String,
    college: String,
    avatar_src: String
  },
  data() {
    return {

    }
  }
}
</script>