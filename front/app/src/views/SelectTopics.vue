<template>
  <v-container>
    <v-layout align-center id="text-layout">
      <v-flex xs12>
        <h1 class="text-xs-center" id="heading">あなたが欲しい本に近いイメージの単語群を選択してください</h1>
      </v-flex>
    </v-layout>

    <v-layout justify-end>
      <v-flex xs1>
        <v-btn v-on:click=nextPage large color="info">次へ >></v-btn>
      </v-flex>
    </v-layout>
 
    <v-layout row wrap v-for="(topic, index) in topics" :key="index">
      <v-flex xs1>
        <v-card class="topic-checkbox">
          <v-checkbox
          :label="``"
          @change="clickedBox(index)">
          </v-checkbox>
        </v-card>
      </v-flex>
      <v-flex xs11 dark color="secondary">
        <v-card class="topic-words">
          <div v-for="(word, index) in topic[1]" :key="index" class="topic-word">
            {{ word }}
          </div>
        </v-card>
      </v-flex>
    </v-layout>
    <!-- <v-layout justify-end>
      <v-flex xs1>
        <v-btn v-on:click=nextPage large color="info">次へ >></v-btn>
      </v-flex>
    </v-layout> -->
  </v-container>
</template>

<script>
import axios from 'axios'
import store from '../App'

export default {
  data: function() {
    return {
      topics: [],
      selectedIndex : []
    }
  },
  created: function() {
    this.postToAPI(true)
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
    },
    nextPage: function() {
      this.$data.selectedIndex.forEach(index => {
        console.log(this.$data.topics[index][0])
        store.state.bookIds.push(this.$data.topics[index][0])
      })
      if (this.$route.query.word_class == 'adjective') {
        this.$router.push({ path: 'select_topics?word_class=noun'});
      } else {
        this.$router.push({ path: 'select_books'})
      }
    },
    postToAPI: function(isAdjective) {
      console.log(store.state.bookIds)
      let url = (process.env.API_URL) ? process.env.API_URL : 'http://localhost:5000'
      url += (isAdjective) ? '/show_adjective_topics' : '/show_noun_topics'
      const json = (isAdjective) ? {
        noun: store.state.noun,
        adjective: store.state.adjective,
        selected_keywords: store.state.selectedSimilarWords
      } : {
        book_ids: store.state.bookIds
      }

      axios.post(url, json).then(response => {
        this.$data.topics = []
        this.$data.topics = (isAdjective) ? response.data.adjective_topics : response.data.noun_topics
        console.log(this.$data.topics)
      })

      store.state.book_ids = []
    }
  },
  beforeRouteUpdate: function(to, from, next) {
    this.postToAPI(false)
    next();
  }
};
</script>

<style>
.topic-words {
  display: flex;
  height: 80px;
  margin: 16px 0 20px 0;
}
.topic-word {
  margin: 10px;
  line-height: 60px;
  font-size: 20px;
}
.topic-checkbox {
  height: 80px;
}
.topic-checkbox .v-input {
  align-items: center;
  justify-content: center;
  padding-left: 7px;
  padding-top: 27px;
}

</style>