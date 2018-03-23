<template>
	<b-container class="conversation">
		<b-row class="text-center">
	        <b-col cols="8 LeftSideBar">
	        	<div class="leftside-header border-bottom">
	        		<div class="flex-item">
	        			<img src="../assets/backoption.png" class="backoption">
	        		</div>
	        		<div class="flex-item">Health of published articles</div>
		        	<div class="flex-item setting_bar">
		        		<img src="../assets/setting-bar.png" class="setting-bar">
		        	</div>
	        	</div>

	        	<div class="main-convo">
	        		<ul>
				        <li>
				            <p class="time">
				                <span>10:27am</span>
				            </p>
				            <div class="main self">
				                <img class="avatar" width="50" height="50" src="../assets/avatar.png" />
				                <!-- <div class="text">Hey,Stack!</div> -->
				                <div class="bubble you">Hey,Stack!</div>
				            </div>
				        </li>

				        <li>
				            <p class="time">
				                <span>10:27am</span>
				            </p>
				            <div class="main float-left">
				                <img class="avatar" width="50" height="50" src="../assets/HSavatar60.png" />
				                <div class="bubble me">Hi, Alexis! How can I help you?</div><!-- 
				                <div class="text">Hi, Alexis! How can I help you?</div> -->
				            </div>
				        </li>


				        <li v-if="showFirst" class="first">
				            <p class="time">
				                </br>
				            </p>
				            <div class="main self">
				                <img class="avatar" width="50" height="50" src="../assets/avatar.png" />
				                <!-- <div class="text">Hey,Stack!</div> -->
				                <div class="bubble you">Where is biggest audience from geographically and demographically?</div>
				            </div>
				        </li>

				        <li v-if="showSecond" >
				            <p class="time">
				                <span>10:28am</span>
				            </p>
				            <div class="main float-left">
				                <img class="avatar" width="50" height="50" src="../assets/HSavatar60.png" />
				                <div class="bubble me">In 2017, the biggest audience are from California. </div><!-- 
				                <div class="text">Hi, Alexis! How can I help you?</div> -->
				            </div>
				        </li>

				    </ul>
	        	</div> <!-- end of main-convo -->

	        	<div class="send-message">

	        		<div class="sendtext">
	        			<b-row class="text-center">
					        <b-col cols="1" class="add"><img width="25" height="25" src="../assets/add.png" /></b-col>
					        <b-col><textarea class="col-10" placeholder="Enter your question here.." ></textarea></b-col>

					       <!-- <b-col><form><input type="text" ref="my_input"></form></b-col> -->
					        <b-col cols="4" class="add"><b-button type="submit" variant="primary"  v-on:click="counter +=1" class="send-button">Send</b-button></b-col>
					    </b-row>
					    
					</div>
	        	</div>
	    	</b-col>
	        <b-col class="RightSideBar border-left">
	        	<div class="sidebar-header">
		        	<div class="flex-item files border-bottom">Files</div>
		        	<div class="flex-item">Profile</div>
	        	</div>
	        	
	    	</b-col>
    	</b-row>
	</b-container>
</template>

<script>
export default {
  name: 'conversation',
  components: {
  },
  data: function(){
  	return{
  		first: false,
  		second: false,
  		counter: 0,
  	}
  },
  computed:{
  	showFirst(){
  		return this.counter > 0? true: false;
  	},
  	showSecond(){
  		return this.counter > 1? true: false;
  	}
  },
  methods:{
    getFormValues () {
      this.output = this.$refs.my_input.value
    }
  }
}


</script>

<style>

.send-button{
  float: right;
  margin-right:20px;
  background-color: #079992;
  border-color: #079992;
}
.add{
	padding: 10px;
    margin-left: 10px;
}
.sendtext {
    height: 160px;
    border-top: solid 1px #ddd;
}

.sendtext textarea {
    padding: 10px;
    height: 100%;
    width: 100%;
    border: none;
    outline: none;
    resize: none;
}

.main-convo {
	height: 500px;
	overflow-y: scroll;

}
::-webkit-scrollbar {
    width: 0px;  /* remove scrollbar space */
    background: transparent;  /* optional: just make scrollbar invisible */
}
.main-convo li{
	display: list-item;

}

.text {
        display: inline-block;
        position: relative;
        padding: 0 10px;
        max-width: ~'calc(100% - 40px)';
        min-height: 30px;
        line-height: 2.5;
        font-size: 12px;
        text-align: left;
        word-break: break-all;
        background-color: #fafafa;
        border-radius: 4px;
}

.text:before{
	content: " ";
    position: absolute;
    top: 9px;
    right: 100%;
    border: 6px solid transparent;
    border-right-color: #fafafa;   
}

.self {
    text-align: right;
}

.self .avatar{
    float: right;
    margin: 0 0 0 10px;
}

.self .text {
    background-color: #dbecff;

 }



.self.text:before {
    right: inherit;
    left: 100%;
    border-right-color: transparent;
    border-left-color: #dbecff;
}

.conversation{
}

.border-bottom{
  border-bottom: 2px solid #E7E7E7  !important;
}

.RightSideBar{
	text-align: center;
}
.sidebar-header {
  padding: 0;
  margin: 0;
  list-style: none;
  
  display: -webkit-box;
  display: -moz-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
  
  -webkit-flex-flow: row wrap;
  justify-content: space-around;
}

.flex-item {
	font-size: 1em;
	padding: 5px;
	margin-top: 10px;
	text-align: center;
}
.files {
	width:100px;
}
.leftside-header {
  padding: 0;
  margin: 0;
  list-style: none;
  
  display: -webkit-box;
  display: -moz-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
  
  -webkit-flex-flow: row wrap;
  justify-content: space-between;
}
.setting-bar{
	height:20px;
}
.backoption{
	height: 32px;
}


.bubble{
    background-color: #F2F2F2;
    border-radius: 5px;
    box-shadow: 0 0 6px #B2B2B2;
    display: inline-block;
    padding: 10px 18px;
    position: relative;
    vertical-align: top;
}

.bubble::before {
    background-color: #F2F2F2;
    content: "\00a0";
    display: block;
    height: 16px;
    position: absolute;
    top: 11px;
    transform:             rotate( 29deg ) skew( -35deg );
        -moz-transform:    rotate( 29deg ) skew( -35deg );
        -ms-transform:     rotate( 29deg ) skew( -35deg );
        -o-transform:      rotate( 29deg ) skew( -35deg );
        -webkit-transform: rotate( 29deg ) skew( -35deg );
    width:  20px;
}

.me {
    /*float: left; */  
    margin: 5px 45px 5px 20px;         
}

.me::before {
    box-shadow: -2px 2px 2px 0 rgba( 178, 178, 178, .4 );
    left: -9px;           
}

.you {
    /*float: right; */
    background-color:#dbecff;   
    margin: 5px 20px 5px 45px;         
}

.you::before {
	background-color:#dbecff;
    box-shadow: 2px -2px 2px 0 rgba( 178, 178, 178, .4 );
    right: -9px;    
}

</style>