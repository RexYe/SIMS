<style lang="stylus" rel="stylesheet/stylus">

</style>

<template>
<div id="app">
  <router-view class="router-view"></router-view>
</div>

</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      seller: {}
    }
  },
  created() {}
}
</script>