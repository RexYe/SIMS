<template>
    <div class="personalInfo-header">
        <p id="name">{{name}}</p>
        <p id="organization">{{college}}</p>
        <p><i class="el-icon-menu"></i>中国</p>
    </div>
</template>
<style>
    .personalInfo-header {
        height: 180px;
        padding: 20px;
    }
  .personalInfo-header #name {
        font-size: 40px;
        margin-bottom: 15px;
    }
    .personalInfo-header #organization{
        margin-bottom: 5px;
    }
</style>
<script>
export default {
  props: {
    name: String,
    college: String
  },
  data() {
    return {

    }
  }
}
</script>