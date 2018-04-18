<template>
    <div class="personalInfo-header">
        <p id="name">{{name}}</p>
        <span id="organization">{{college}}</span>
    </div>
</template>
<style>
  .personalInfo-header #name {
        font-size: 40px;
        margin-bottom: 10px;
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