
<template>
<div id="app">
  <router-view class="router-view"></router-view>
  <a class="toback" href="http://localhost:8002" target="_Blank">管理登录</a>
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
    /*background: linear-gradient(#272C3A,#F4F2F2);*/
		background-image: url('assets/img/index_bg.png');
    background-repeat: no-repeat;
    background-size: cover;
		color: #fff;
	}
  .toback{
    display: flex;
    align-items: center;
    justify-content: center;
    align-content: center;
    background: rgba(0,0,0,0);
  }
</style>