<template>
  <v-card class="pt-3">
    <v-img
      :src="book_info.image_url"
      height="170px"
      width="120px"
      class="mx-auto"
    >
    </v-img>

    <v-card-text>
      <div class="card-text">
        <p>{{ book_info['name'] }}</p>
        <span class="grey--text discription-link">
          <a class="not-decolation" v-bind:href="'https://bookmeter.com/books/' + book_info.id" target="_blank">
            読書メーターで詳細をみる
          </a>
        </span>
      </div>
    </v-card-text>

    <v-card-actions>
      <v-btn v-on:click=nextPage(book_info) class="mx-auto" color="info">この本を選択</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import axios from 'axios'
import store from '../App'

export default {
  props: ['book_info'],
  data: function() {
    return {}
  },
  created: function() {
  },
  methods: {
    nextPage: function(book_info) {
      store.state.selectedBookInfo = book_info
      this.$router.push({ path: 'evaluation'})
    }
  },
};
</script>

<style>
.discription-link {
  display: block;
  position: absolute;
  bottom: 0;
  right: 0;
}
.card-text {
  position: relative;
  min-height: 100px;
}
.not-decolation {
  text-decoration: none;
  color: grey;
}
</style>