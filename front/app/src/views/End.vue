<template>
  <div>End</div>
</template>

<script>
import store from '../App'
import axios from 'axios'

export default {
  data() {
    return {
      
    }
  },
  created() {
    let url = (process.env.API_URL) ? process.env.API_URL : 'http://localhost:5000'
    url += '/save_evaluation_data'

    const json = {
      evaluation_data: store.state.evaluationData
    }
    axios.post(url, json).then(response => {
      console.log(response)
    })
  },
  methods: {
  }
};
</script>