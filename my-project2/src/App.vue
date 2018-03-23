<template>
  <div id="app">
    <AppNav></AppNav>
    <router-view></router-view>
   <!--  <AppNav></AppNav>
    <b-container>
      <b-row>
        <b-col cols="8">
        <div class="float-left"><h3>Ask HeyStack</h3></div><br>
        <div class="callout clear-fix">
          <div class="callout_avatar ">
            <img src="./assets/HSavatar-callout.png">
          </div>
          <div class="callout_form">
            <b-form @submit="onSubmit">
              <b-form-input v-model="form.question" required
                    type="text"
                    placeholder="Enter your questions here.."></b-form-input>
              <b-button type="submit" variant="primary" class="callout_form--button">Send</b-button>
          </b-form>
          </div>
        </div>
        <div class="past_Conversation">
          <div class="float-left"><h3>Past Conversations</h3></div><br>
          <PastConvo></PastConvo>
        </div>
        </b-col>
        <b-col cols="4">
          <h5>Top 20 Frequently Asked Questions</h5>
          <b-list-group>
            <b-list-group-item href="#" class="flex-column align-items-start">
              <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">Question 1</h5>
                <small>3 days ago</small>
              </div>
            </b-list-group-item>
            <b-list-group-item href="#" class="flex-column align-items-start">
              <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">Question 2</h5>
                <small class="text-muted">3 days ago</small>
              </div>
            </b-list-group-item>
            <b-list-group-item href="#" class="flex-column align-items-start">
              <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">Question 3</h5>
                <small class="text-muted">3 days ago</small>
              </div>
            </b-list-group-item>
            <b-list-group-item href="#" class="flex-column align-items-start">
              <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">Question 4</h5>
                <small class="text-muted">3 days ago</small>
              </div>
            </b-list-group-item>
            <b-list-group-item href="#" class="flex-column align-items-start">
              <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">Question 5</h5>
                <small class="text-muted">3 days ago</small>
              </div>
            </b-list-group-item>
            <b-list-group-item href="#" class="flex-column align-items-start">
              <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">Question 6</h5>
                <small class="text-muted">3 days ago</small>
              </div>
            </b-list-group-item>
            <b-list-group-item href="#" class="flex-column align-items-start">
              <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">Question 7</h5>
                <small class="text-muted">3 days ago</small>
              </div>
            </b-list-group-item>
          </b-list-group>
        </b-col>
      </b-row>
      
    </b-container> -->
  </div>
</template>

<script>
import AppNav from './assets/AppNav.vue'
import PastConvo from './assets/PastConvo.vue'

export default {
  name: 'app',
  components: {
    AppNav,
    PastConvo
  },
  data () {
    return {
      form: {
        email: '',
      },
    }
  },
  methods:{
    onSubmit(evt){
      evt.preventDefault();
       alert(JSON.stringify(this.form));
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
  color: #4A4A4A;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

.callout{
  background-color: #7DC9C7;
  border-radius: 5px;
  height: 217px;
  margin-top: 30px;
  margin-bottom: 30px;

}

.callout_avatar{
  float: left;
  position: relative;
  top: 50%;
  transform: translateY(-50%);
  margin-left: 40px;
  margin-right: 20px;
}

.callout_form{
  float: right;
  position: relative;
  top: 50%;
  transform: translateY(-50%);
  width: 500px;
}

form {
  margin-right: 40px;
}

form input {
  height: 80px;
}

.callout_form--button{
  float: right;
  margin-top: 20px;
  background-color: #079992;
  border-color: #079992;
}

.callout_form--button:hover{
  margin-top: 20px;
  background-color: #065652;
  border-color: #065652;

}



</style>
