
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
  created() {
  }
}
</script>
<style>
	#app{
    background: linear-gradient(#272C3A,#BFE4A2);
		/*background-image: url('assets/img/index_bg.png');*/
		color: #fff;
	}
</style>