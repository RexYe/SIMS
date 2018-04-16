<template>
	<div class="personalInfo">
		<v-header></v-header>
		<div class="personalInfo-container">个人信息</div>
	</div>
</template>

<script>
import header from 'components/header/header'


export default {
  data() {
  },
  components: {
    'v-header': header
  }
}

</script>
<style scoped>
	.personalInfo{
		width: 100%;
		height: 100%;
	}
	.personalInfo-container{
		height: 900px;
		margin-top: 90px;
	}
</style>
