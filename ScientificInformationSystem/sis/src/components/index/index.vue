<template>
	<div class="index">
		<v-header></v-header>
		<div class="index-container">科研信息管理系统</div>
	</div>
</template>

<script>
import header from 'components/header/header'


export default {
  data() {
  	return {

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
	}
	.index-container{
		height: 900px;
		margin-top: 70px;
	}
</style>
