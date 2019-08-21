<template>
  <div id="app">
    <img src="./assets/logo.png">
    <router-link to="/demos/test">test</router-link>
    {{message}}{{message2}}
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      message: 'this is eric message\r\n',
      message2:  'this is NOT eric message'
    }
  }
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
