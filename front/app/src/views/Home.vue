<template>
  <v-container>
    <v-layout align-center id="text-layout">
      <v-flex xs12>
        <v-text-field v-model="keyword" v-on:keyup=searchIfEntered required label="キーワードを入力してください (例) 感動 泣ける 青春"></v-text-field>
      </v-flex>
    </v-layout>
    <v-layout justify-end>
      <v-flex xs1>
        <v-btn v-on:click=search large color="info">次へ >></v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>

export default {
  data: () => ({
    keyword : ""
  }),
  methods: {
    search() {
      this.$router.push({ path: `search?keyword=${this.keyword}`});
    },
    // searchIfEntered(e) {
    //   if (e.keyCode === 13) this.search();
    // }
  }
};
</script>

<style>
  #text-layout {
    min-height: 250px;
  }
</style>
