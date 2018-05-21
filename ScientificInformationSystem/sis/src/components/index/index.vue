<template>
	<div class="index">
		<v-header></v-header>
		<div class="index-container">
				<div id="particles">
				  <div class="intro">
				    <h1>科研信息管理系统</h1>
				    <p>A Scientific Information systems</p>
				    <img src="../../assets/img/index_bg_gif.gif" height="151" width="172">
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
		/*background: #16a085;*/
		background: #434343;
		background-image: url('../../assets/img/index_bg2.png');
		background-repeat: repeat;
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
		margin-top: 60px;
	}
/*	.daytime{
		width: 100%;
		height: 650px;
		
	}*/

</style>
