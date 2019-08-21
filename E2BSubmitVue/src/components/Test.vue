<template>
  <div id="test">
    <h2>{{message}}</h2>
    <button @click="sayOut">按钮</button>
    <button @click="parseXML">解析</button>
    <table>
      <thead>
      <tr>
        <th>姓名</th>
        <th>邮件</th>
        <th>密码</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="user in users">
        <td v-text="user.username"></td>
        <td v-text="user.email"></td>
        <td v-text="user.password"></td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  export default {
    name: 'Test',
    data () {
      return {
        users: [],
        message: 'this is a message'
      }
    },
    methods: {
        sayOut:function(){
        this.message = 'this is NOT a message';
        this.axios.get('/demos/getdata').then((response) => {
          //console.log(response.data)
          this.users = response.data;
          //return response.data;

        }).catch((response) => {
          console.log(response)
        })
      },
      parseXML:function(){
        this.axios.get('/demos/processICSR').then((response) => {
          console.log(response.data)
        }).catch((response) => {
          console.log(response)
        })
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
