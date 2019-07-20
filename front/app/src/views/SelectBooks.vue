<template>
  <v-container
    grid-list-md
  >
    <v-layout row wrap>
      <v-flex
        xs3
        v-for="(book_isbn, index) in booksISBN"
        :key="index"
      >
        <BookCard :book_isbn="book_isbn"/>
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
      booksISBN: []
    }
  },
  created: function() {
    console.log(store.state.bookIds)
    let url = (process.env.API_URL) ? process.env.API_URL : 'http://localhost:5000'
    url += '/get_isbn_from_book_ids'
    const json = {
      book_ids: store.state.bookIds
    }
    axios.post(url, json).then(response => {
      this.$data.booksISBN = response.data.isbn_list
      console.log(this.$data.booksISBN)
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