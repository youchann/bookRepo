<template>
  <v-container>
    <v-layout text-xs-center wrap>
      <v-flex xs12>
        <v-img :src="require('../assets/logo.svg')" class="my-3" contain height="200"></v-img>
      </v-flex>

      <v-flex mb-4>
        <h1 class="display-2 font-weight-bold mb-3">Welcome to Vuetify</h1>
        <p class="subheading font-weight-regular">
          For help and collaboration with other Vuetify developers,
          <br>please join our online
          <a
            href="https://community.vuetifyjs.com"
            target="_blank"
          >Discord Community</a>
        </p>
      </v-flex>
    </v-layout>
    <v-alert :value="true" type="success">This is a success alert.</v-alert>
    <v-alert :value="true" type="info">This is a info alert.</v-alert>
    <v-alert :value="true" type="warning">This is a warning alert.</v-alert>
    <v-alert :value="true" type="error">This is a error alert.</v-alert>
  </v-container>
</template>

<script>
export default {

};
</script>

<style>
</style>