<template>
  <div :style="style">{{ name }}</div>
</template>
<style>
</style>
<script>
import { Mixin } from "./mixin";
export default {
  mixins: [Mixin]
};
</script>