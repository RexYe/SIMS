<template>
    <div class="journalInfo-header">
        <div class="journal-logo">
            <img :src=logo>
        </div>
        <div class="personal-world-info">
            <p id="name">{{name}}</p>
            <p id="english-name">{{english_name}}</p>
            <a id="website">{{website}}</a>

            <p id="location">
                <i class="el-icon-location"></i>
                <p id="location">{{location}},中国</p>
            </p>
        </div>
        <div></div>
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
        height: 120px;
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
    .personal-world-info #location {
        margin-top: 1px;
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
    location: String
  },
  data() {
    return {

    }
  },
  created: function () {
    // this.honor = this.honor.split(';')
    // console.log(this.honor)
  }
}
</script>