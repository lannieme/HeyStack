<template>
    <b-container>
      <b-row>
        <b-col cols="8">
        <!-- <div class="float-left"><h4>Ask HeyStack</h4></div><br> -->
        <div class="callout clear-fix">
          <div class="callout_avatar ">
            <img src="../assets/HSavatar-callout.png">
          </div>
          <div class="callout_form">
            <b-form @submit="onSubmit">
              <!-- <b-form-input v-model="form.question" required
                    type="text"
                    placeholder="Enter your questions here.."></b-form-input> -->
              <b-button type="submit" variant="primary" class="callout_form--button">Chat with HeyStack</b-button>
          </b-form>
          </div>
        </div>
        <div class="past_Conversation">
          <div class="float-left"><h4>Past Conversations</h4></div><br>
          <PastConvo></PastConvo>
        </div>
        </b-col>
        <b-col cols="4" class="rightSide">
          <h5 class="topQ_header">Top 10 Frequently Asked Questions</h5>
          <b-list-group>
            <b-list-group-item href="#" class="flex-column align-items-start">
              <div class="d-flex w-100 justify-content-between">
                <p class="mb-1 topQ">1. How many subscribers do we have this month?</p>
                <small>1 month ago</small>
              </div>
            </b-list-group-item>
            <b-list-group-item href="#" class="flex-column align-items-start">
              <div class="d-flex w-100 justify-content-between">
                <p class="mb-1 topQ">2. What is the most popular story of last year?</p>
                <small class="text-muted">23 days ago</small>
              </div>
            </b-list-group-item>
            <b-list-group-item href="#" class="flex-column align-items-start">
              <div class="d-flex w-100 justify-content-between">
                <p class="mb-1 topQ">3. What is the CAGR of our projected revenue in 5 years?</p>
                <small class="text-muted">17 days ago</small>
              </div>
            </b-list-group-item>
            <b-list-group-item href="#" class="flex-column align-items-start">
              <div class="d-flex w-100 justify-content-between">
                <p class="mb-1 topQ">4. What is the engagement rate for the last quarter?</p>
                <small class="text-muted">24 days ago</small>
              </div>
            </b-list-group-item>
            <b-list-group-item href="#" class="flex-column align-items-start">
              <div class="d-flex w-100 justify-content-between">
                <p class="mb-1 topQ">5. Who are the top subscriber?</p>
                <small class="text-muted">3 days ago</small>
              </div>
            </b-list-group-item>
            <b-list-group-item href="#" class="flex-column align-items-start">
              <div class="d-flex w-100 justify-content-between">
                <p class="mb-1 topQ">6. Distribution channel analysis</p>
                <small class="text-muted">12 days ago</small>
              </div>
            </b-list-group-item>
            <b-list-group-item href="#" class="flex-column align-items-start">
              <div class="d-flex w-100 justify-content-between">
                <p class="mb-1 topQ">7. Trending author</p>
                <small class="text-muted">3 days ago</small>
              </div>
            </b-list-group-item>
          </b-list-group>
          <b-list-group-item href="#" class="flex-column align-items-start">
              <div class="d-flex w-100 justify-content-between">
                <p class="mb-1 topQ">8. Advertisement</p>
                <small class="text-muted">1 days ago</small>
              </div>
            </b-list-group-item>
          </b-list-group>
        </b-col>
      </b-row>
      
    </b-container>
</template>

<script>
import PastConvo from '../assets/PastConvo.vue'

export default {
  name: 'home',
  components: {
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
      this.$router.push({ name: 'convo'})
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
  /*width: 500px;*/
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
  width: 500px;
  height: 50px;
}


.callout_form--button:hover{
  margin-top: 20px;
  background-color: #065652;
  border-color: #065652;

}

.row {
  margin-top: 10px;
  margin-bottom: 10px;
}

.past-convo .form-control { 
  width:30%;
  display: inline-block;
  margin-right:10px;
}
.name {
  font-weight: 700;
}

.btn-more {
  margin-top:10px;
  width: 100%
}
.label {
  font-weight: normal;
}

.btn-primary {
    background-color: #079992;
    border-color: #079992;
}

.topQ{
  text-align: left;
}

.rightSide .list-group-item {
  margin-bottom: 5px;
}
.topQ_header{
  margin-bottom: 30px;
}
</style>
