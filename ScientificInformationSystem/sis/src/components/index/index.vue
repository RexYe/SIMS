<template>
	<div class="index">
		<v-header></v-header>
		<div class="index-container">
				<div id="particles">
				  <div class="intro">
				    <h1>科研信息管理系统</h1>
				    <p>A jQuery plugin for snazzy background particle systems</p>
				  </div>
				</div>
		</div>
	</div>
</template>

<script>
import header from 'components/header/header'
import $ from 'jquery'

export default {
  data() {
  	return {

  	}
  },
  mounted: function () {
		this.particles()
  },
  methods: {
  	particles: function () {
		this.$nextTick(function(){
			console.log(222)
		})	
	}
  },
  components: {
    'v-header': header
  }
}

</script>
<style scoped>
	.index{
		width: 100%;
		height: 100%;
		background: #16a085;
		font-family: 'Montserrat', sans-serif;
		color: #fff;
		line-height: 1.3;
		-webkit-font-smoothing: antialiased;
	}
	h1 {
		text-transform: uppercase;
		font-size: 85px;
		font-weight: 700;
		letter-spacing: 0.015em;
	}
	h1::after {
		content: '';
		width: 80px;
		display: block;
		background: #fff;
		height: 10px;
		margin: 30px auto;
		line-height: 1.1;
	}
	p {
		margin: 0 0 30px 0;
		font-size: 24px;
	}
	.intro {
  position: absolute;
  left: 0;
  top: 50%;
  padding: 0 20px;
  width: 100%;
  text-align: center;
}
	.index-container{
		height: 900px;
		margin-top: 70px;
	}
	.daytime{
		width: 100%;
		height: 650px;
		background-image: url(http://cdn.www.chelaile.net.cn/web/images/asset/daytime_bg.36774c23.png);
		background-repeat: repeat;
	}
	.cloud1{
		background-image: url(http://cdn.www.chelaile.net.cn/web/images/icons-sfbb092376f.ee0f8bec.png);
		background-position: 0 -644px;
		height: 52px;
		width: 892px;
		display: inline-block;
		overflow: hidden;

		    bottom: 145px;
    margin-left: -500px;
    -webkit-transition: All .4s ease-in-out;
    transition: All .4s ease-in-out;
    -webkit-animation-name: cloud2;
    animation-name: cloud2;
    -webkit-animation-duration: 3s;
    animation-duration: 3s;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
    animation-direction: alternate;
    animation-play-state: running;
	}
</style>
