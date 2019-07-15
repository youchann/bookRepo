<template>
  <v-container>
    <v-layout>
      <v-flex xs12>
        <h3 class="text-xs-center">検索ワード: {{ keyword }}</h3>
      </v-flex>
    </v-layout>
    <v-layout align-center id="text-layout">
      <v-flex xs12>
        <h1 class="text-xs-center" id="heading">あなたが欲しい本と近い関連のある単語を選択してください↓</h1>
      </v-flex>
    </v-layout>
 
    <v-layout wrap>
     <v-flex xs2 v-for="(word, index) in similarWords" :key="index">
        <v-card width="180px" class="cards">
          <div class="checkboxes">
            <v-checkbox
            :label="word"
            @change="clickedBox(index)">
            </v-checkbox>
          </div>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  data: function() {
    return {
      similarWords : [],
      keyword : this.$route.query.keyword,
      selectedIndex : []
    }
  },
  created: function() {
    let url = (process.env.API_URL) ? process.env.API_URL : 'http://localhost:5000'
    url += '/search'

    axios.get(url, {
      params: {
        keyword: this.$route.query.keyword
      }
    }).then(response => {
      this.$data.similarWords = response.data.similar_words
    })
  },
  methods: {
    clickedBox: function(index) {
      let selectedIndex = this.$data.selectedIndex
      if (selectedIndex.includes(index)) {
        selectedIndex = selectedIndex.filter( value => value != index )
      } else {
        selectedIndex.push(index)
      }
      this.$data.selectedIndex = selectedIndex
      console.log(this.$data.selectedIndex)
    }
  },
};
</script>

<style>
.checkboxes {
  display: inline-block;
}
.cards {
  margin: 5px auto;
  text-align: center;
}
#text-layout {
  min-height: 250px;
}
</style>
