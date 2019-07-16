<template>
  <TableSample />
</template>

<script>
import TableSample from "../components/TableSample";
import axios from 'axios'
import store from '../App'

export default {
  data: function() {
    return {
    }
  },
  created: function() {
    console.log(store.state)
  },
  methods: {
  },
}
</script>