<template>
  <v-card class="pt-3">
    <v-img
      src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
      height="150px"
      width="120px"
      class="mx-auto"
    >
    </v-img>

    <v-card-text>
      <div class="card-text">
        <p>新しい朝が来た、希望の朝だ。。</p>
        <span class="grey--text discription-link">Wikipediaで詳細を見る</span>
      </div>
    </v-card-text>

    <v-card-actions>
      <v-btn class="mx-auto" color="info">Info</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import axios from 'axios'
import store from '../App'

export default {
  props: ['book_isbn'],
  data: function() {
    return {
    }
  },
  created: function() {
//     console.log(store.state.bookIds)
//     let url = (process.env.API_URL) ? process.env.API_URL : 'http://localhost:5000'
//     url += '/get_isbn_from_book_ids'
//     const json = {
//       book_ids: store.state.bookIds
//     }
//     axios.post(url, json).then(response => {
//       this.$data.booksISBN = response.data.isbn_list
//       console.log(this.$data.booksISBN)
//     })
  },
  methods: {
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
</style>