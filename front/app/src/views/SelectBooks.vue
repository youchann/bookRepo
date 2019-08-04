<template>
  <v-container
    grid-list-md
  >
    <v-layout align-center id="text-layout">
      <v-flex xs12>
        <h1 class="text-xs-center" id="heading">あなたが欲しいと思った本を選択してください</h1>
      </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex
        xs3
        v-for="(book_info, index) in bookInfoList"
        :key="index"
      >
        <BookCard :book_info="book_info"/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import BookCard from '../components/BookCard'
import axios from 'axios'
import store from '../App'

export default {
  components: {
    BookCard
  },
  data: function() {
    return {
      bookInfoList: []
    }
  },
  created: function() {
    console.log(store.state.bookIds)
    let url = (process.env.API_URL) ? process.env.API_URL : 'http://localhost:5000'
    url += '/get_info_from_book_ids'
    const json = {
      book_ids: store.state.bookIds
    }
    axios.post(url, json).then(response => {
      this.$data.bookInfoList = response.data.info_list
      console.log(this.$data.bookInfoList)
    })
  },
  methods: {
    nextPage: function() {
    },
  },
};
</script>

<style>
</style>