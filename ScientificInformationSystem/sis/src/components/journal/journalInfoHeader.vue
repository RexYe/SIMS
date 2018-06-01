<template>
    <div class="journalInfo-header">
        <div class="journal-logo">
            <img :src=logo>
        </div>
        <div class="personal-world-info">
            <p id="name">{{name}}</p>
            <p id="english-name">{{english_name}}</p>
            <!-- <a id="website">{{website}}</a> -->
            <p id="country"><i class="el-icon-location"></i>中国</p>
        </div>
        <div class="honor">
            <span v-for = "honor in honor" class="honor-item"><img src="../../assets/icon/jiangpai.png" height="22" width="22">{{honor}}</span>
        </div>
        <div class="influence">
            <div class="complex">
                <span class="title">（2017版）复合影响因子：</span>
                <span class="no">{{complex_influence}}</span>
            </div>           
            <div class="comprehensive">
                <span class="title">（2017版）综合影响因子：</span>
                <span class="no">{{comprehensive_influence}}</span>
            </div>           
        </div>
    </div>
</template>
<style>
    .journalInfo-header {
        padding-left: 20px;
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
        font-size: 30px;
        margin-bottom: 15px;
    }
    .personal-world-info #english-name{
        margin-bottom: 8px;
        color: #8F8B8B;
        font-size: 14px;
    }
    .personal-world-info #country {
        margin-top: 26px;
        font-size: 14px;
        color: #8F8B8B;
    }
    .honor{
        font-size: 15px;
        display: flex;
        align-items: center;
        justify-content: center;
        align-content: center;
    }
    .honor-item{
        padding: 4px;
        display: flex;
        align-items: center;
    }
    .influence{
        padding-left: 80px;
        display: flex;
        flex-flow: column;
    }
    .influence .title{
        font-size: 14px;
    }
    .influence .no{
        font-size: 14px;
        color: red;
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
    // this.honor = this.honor.split(';')
    console.log(this.honor)
  }
}
</script>