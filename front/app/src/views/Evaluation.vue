<template>
  <v-container>
    <v-layout column align-center justify-center id="text-layout">
      <v-flex xs3>
        <v-card class="pt-3">
          <v-img
            :src="selectedBookInfo.image_url"
            height="170px"
            width="120px"
            class="mx-auto"
          >
          </v-img>
          <v-card-text>
            {{ selectedBookInfo.name }}
          </v-card-text>
        </v-card>
      </v-flex>
      <v-spacer></v-spacer>
      <v-flex xs12>
        <h1 class="text-xs-center my-5">アンケートにお答えください↓</h1>
      </v-flex>
    </v-layout>
    <v-layout row wrap v-for="(evaluation, index) in evaluationList" :key="index">
      <v-flex xs12 dark color="secondary">
        <v-card class="topic-words">
          <v-card-title class="evaluation-description">{{ evaluation.description }}</v-card-title>
          <v-spacer></v-spacer>
          <v-card-actions>
            <span style="margin-right: 23px;">はい</span>
            <v-radio-group :row=true v-model="evaluation.evaluation">
              <v-radio
                v-for="n in 4"
                :key="n"
                :value="n"
              ></v-radio>
            </v-radio-group>
            <span>いいえ</span>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout justify-end>
      <v-flex xs1>
        <v-btn v-on:click=nextPage large color="info">次へ >></v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import store from '../App'
import axios from 'axios'

export default {
  data() {
    return {
      evaluationList: [],
      selectedBookInfo: []
    }
  },
  created() {
    let url = (process.env.API_URL) ? process.env.API_URL : 'http://localhost:5000'
    url += '/get_evaluation_data'

    axios.get(url).then(response => {
      this.$data.evaluationList = response.data.evaluation_list
    }).then(() => {
      for(let i = 0; i < this.$data.evaluationList.length; i += 1) {
        this.$data.evaluationList[i].evaluation = 1
      }
      console.log(this.$data.evaluationList)
    })

    this.$data.selectedBookInfo = store.state.selectedBookInfo
  },
  methods: {
    nextPage() {
      for(let i = 0; i < this.$data.evaluationList.length; i += 1) {
        store.state.evaluationData.push({
          "evaluation_id": this.$data.evaluationList[i].id,
          "evaluation" : this.$data.evaluationList[i].evaluation
        })
      }
      this.$router.push({ path: 'end'})
    }
  }
};
</script>

<style>
.evaluation-description{
  font-size: 17px;
}

</style>