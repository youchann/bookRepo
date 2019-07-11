<template>
  <div>
      <p>2</p>
      <p>2</p>
    <input v-model="username">
    <div 
      v-if="error"
      class="error"
    >
      {{ error }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'Hello',
  data () {
    return {
      username: 'テスト用'
    }
  },

  computed: {
    error () {
      return this.username.trim().length < 7
        ? 'Please enter a longer username'
        : ''
    }
  }
}
</script>