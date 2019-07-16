<template>
  <TableSample />
</template>

<script>
import axios from 'axios'
import store from '../App'

export default {
  data: function() {
    return {
    }
  },
  created: function() {
    console.log(store.state)
    // let url = (process.env.API_URL) ? process.env.API_URL : 'http://localhost:5000'
    // url += '/search'

    // axios.get(url, {
    //   params: {
    //     keyword: this.$route.query.keyword
    //   }
    // }).then(response => {
    //   this.$data.similarWords = response.data.similar_words
    //   store.state.noun = response.data.analyzed_keywords.noun
    //   store.state.adjective = response.data.analyzed_keywords.adjective
    // })
  },
  methods: {
    
  },
};
</script>