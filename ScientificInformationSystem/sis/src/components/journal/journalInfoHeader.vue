<template>
    <div class="journalInfo-header">
        <div class="journal-logo">
            <img :src=logo>
        </div>
        <div class="personal-world-info">
            <p id="name">{{name}}</p>
            <p id="english-name">{{english_name}}</p>
            <a id="website">{{website}}</a>

            <p id="country"><i class="el-icon-location"></i>中国</p>
        </div>
        <div v-for = "honor in honor"><img src="../../assets/icon/jiangpai.png" height="22" width="22">{{honor}}</div>
        <div>
            复合影响因子：<span>{{complex_influence}}</span>
            综合影响因子：<span>{{comprehensive_influence}}</span>
        </div>
    </div>
</template>
<style>
    .journalInfo-header {
        height: 180px;
        display: flex;
        flex-direction: row;
        align-items: center;     
    }
    .journalInfo-header .journal-logo{
        width: 120px;
        height: 166px;
        overflow: hidden;
    }
    .journalInfo-header .journal-logo img{
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
    english_name: String,
    website: String,
    logo: String,
    honor: Array,
    complex_influence: String,
    comprehensive_influence: String
  },
  data() {
    return {

    }
  },
  created: function () {
    this.honor = this.honor.split(';')
    console.log(this.honor)

  }
}
</script>