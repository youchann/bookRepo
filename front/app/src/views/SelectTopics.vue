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
 
    <v-layout row wrap v-for="(topic, index) in adjectiveTopics" :key="index">
      <v-flex xs1>
        <v-card class="topic-checkbox">
          <v-checkbox
          :label="``">
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
      adjectiveTopics: []
    }
  },
  created: function() {
    let url = (process.env.API_URL) ? process.env.API_URL : 'http://localhost:5000'
    url += '/show_adjective_topics'

    axios.post(url, {
      noun: store.state.noun,
      adjective: store.state.adjective,
      selected_keywords: store.state.selectedSimilarWords
    }).then(response => {
      this.$data.adjectiveTopics = response.data.adjective_topics
    })
  },
  methods: {
    
  },
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
.v-input {
  align-items: center;
  justify-content: center;
  padding-left: 7px;
  padding-top: 27px;
}

</style>