<template>
  <v-container>
    <v-layout wrap>
      <v-flex xs2 v-for="n in 20">
        <v-card width="160px" class="cards">
          <div class="checkboxes">
            <v-checkbox
            :label="'hogehoge'">
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
      adjectiveTopics : "",
      keyword : this.$route.query.keyword
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
      console.log(response.data)
    })
  },
};
</script>

<style>
.checkboxes {
  display: inline-block;
}
.cards {
  margin: 10px auto;
  text-align: center;
}
</style>
