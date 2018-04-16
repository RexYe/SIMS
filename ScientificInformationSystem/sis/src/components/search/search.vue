<template>
	<div class="search">
		<v-header></v-header>
		<div class="search-container">搜索结果:</div>
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
	.search{
		width: 100%;
		height: 100%;
	}
	.search-container{
		height: 900px;
		margin-top: 90px;
	}
</style>
