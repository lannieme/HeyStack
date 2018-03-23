<template>
	<b-container class="conversation" >
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

	        	<div class="main-convo" ref="main-convo" v-chat-scroll>
	        		<ul v-chat-scroll>
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
				                <div class="bubble me">Hi, Alexis! How can I help you?</div>
				            </div>
				        </li>


				        <li v-if="showFirst" class="first">
				            <p class="time">
				                </br>
				            </p>
				            <div class="main self">
				                <img class="avatar" width="50" height="50" src="../assets/avatar.png" />
				                <div class="bubble you">Where is biggest audience from geographically and demographically?</div>
				            </div>
				        </li>

				        <li v-if="showSecond" >
				            <p class="time">
				                <span>10:28am</span>
				            </p>
				            <div class="main float-left">
				                <img class="avatar" width="50" height="50" src="../assets/HSavatar60.png" />
				                <div class="bubble me">In 2017, the biggest audience are from California. </br>I also generated a pie chart for you to better represent the data.</div><!-- 
				                <div class="text">Hi, Alexis! How can I help you?</div> -->
				            </div>
				        </li>

				        <li v-if="showSecond"  class="panel">
				            <p class="time">
				                </br>
				            </p>
				            <div class="main float-left panel-body">
				                <img class="avatar" width="50" height="50" src="../assets/HSavatar60.png" />
				                <div class="bubble me chart">
					                <div class="thumbnail">
					                	<img class="avatar" src="../assets/graph.png" />
					                	<div class="caption caption-left">
										<p> <strong>Based on your data, we recommend pie chart.</strong></p>
										<p>
											<v-popover offset="16">
											  <b-btn class="tooltip-target btn btn-primary" role="button">Edit</b-btn> 

											  <template slot="popover">
											    <ul>
											     <li><b-btn @click="showChart=true" variant="primary" class="popover-btn">Change chart type</b-btn>
											     </li>
											     <li><b-btn @click="showTheme=true" variant="primary" class="popover-btn">Change color theme</b-btn></li>
											    </ul>
											    <b-btn class="btn btn-primary" v-close-popover>Close</b-btn>
											  </template>
											</v-popover>
											<a href="#" class="btn btn-primary" role="button">
											Download
											</a> 
										</p>
										</div>
					                </div>
				                </div><!-- 
				                <div class="text">Hi, Alexis! How can I help you?</div> -->
				                
				            </div>
				        </li>

				        <li v-if="showNewColor"  class="panel">
				            <p class="time">
				                </br>
				            </p>
				            <div class="main float-left panel-body">
				                <img class="avatar" width="50" height="50" src="../assets/HSavatar60.png" />
				                <div class="bubble me chart">
				                	<p>Here is your new graph.</p>
					                <div class="thumbnail">
					                	<img class="avatar" src="../assets/graph_color.png" />
					                	<div class="caption caption-left">
										<p>
											<v-popover offset="16">
											  <b-btn class="tooltip-target btn btn-primary" role="button">Edit</b-btn> 

											  <template slot="popover">
											    <ul>
											     <li><b-btn @click="showChart=true" variant="primary" class="popover-btn">Change chart type</b-btn>
											     </li>
											     <li><b-btn @click="showTheme=true" variant="primary" class="popover-btn">Change color theme</b-btn></li>
											    </ul>
											    <b-btn class="btn btn-primary" v-close-popover>Close</b-btn>
											  </template>
											</v-popover>
											<a href="#" class="btn btn-primary" role="button">
											Download
											</a> 
										</p>
										</div>
					                </div>
				                </div><!-- 
				                <div class="text">Hi, Alexis! How can I help you?</div> -->
				                
				            </div>
				        </li>

				        <li>
			        	<b-modal v-model="showChart"
				             title="Change Chart Type">
					       <b-container fluid>
					       	<b-row class="mb-1 text-center">
					       		<b-col cols="12"><strong>For your data, we recommend using pie chart.</strong></b-col>
					       	</b-row>
					         <b-row class="mb-1 text-center">
					           <b-col cols="3"> <input id="radio-1" name="radio" type="radio"><label  for="radio-2" class="radio-label"> Bar Chart</label></b-col>
					           <b-col><img class="avatar" src="../assets/graph_bar.png" /></b-col>
					         </b-row>
					         <b-row class="mb-1">
					           <b-col cols="3"> <input id="radio-2" name="radio" type="radio"><label  for="radio-2" class="radio-label"> Pie Chart</label></b-col>
					           <b-col><img class="avatar" src="../assets/graph.png" /></b-col>
					         </b-row>
					       </b-container>
					       <div slot="modal-footer" class="w-100">
					         <p class="float-left"><strong>Generate New Graph</strong></p>
					         <b-btn size="sm" class="float-right" variant="primary" @click="showNewGraph=true">
					           Confirm
					         </b-btn>
					       </div>
					    </b-modal>
				        </li>

				        <li v-if="showThird" class="first lastQ">
				            
				            
				            <div class="main self">
				            		<div class="bubble you">What category of articles are the most popular in California? By total engagement (like, comments & shares) </div>
					                <img class="avatar" width="50" height="50" src="../assets/avatar.png" />
					                
				            </div>
				        </li>

				        <li>
			        	<b-modal v-model="showTheme"
				             title="Change Chart Color Theme"
				             :header-bg-variant="headerBgVariant"
				             :header-text-variant="headerTextVariant"
				             :body-bg-variant="bodyBgVariant"
				             :body-text-variant="bodyTextVariant"
				             :footer-bg-variant="footerBgVariant"
				             :footer-text-variant="footerTextVariant">
					       <b-container fluid>
					         <b-row class="mb-1 text-center">
					           <b-col cols="3"> </b-col>
					           <b-col>Background</b-col>
					           <b-col>Text</b-col>
					         </b-row>
					         <b-row class="mb-1">
					           <b-col cols="3">Title</b-col>
					           <b-col><b-form-select :options="variants" v-model="headerBgVariant" /></b-col>
					           <b-col><b-form-select :options="variants" v-model="headerTextVariant" /></b-col>
					         </b-row>
					         <b-row class="mb-1">
					           <b-col cols="3">Body</b-col>
					           <b-col><b-form-select :options="variants" v-model="bodyBgVariant" /></b-col>
					           <b-col><b-form-select :options="variants" v-model="bodyTextVariant" /></b-col>
					         </b-row>
					         <b-row>
					           <b-col cols="3">Fields</b-col>
					           <b-col><b-form-select :options="variants" v-model="footerBgVariant" /></b-col>
					           <b-col><b-form-select :options="variants" v-model="footerTextVariant" /></b-col>
					         </b-row>
					       </b-container>
					       <div slot="modal-footer" class="w-100">
					         <p class="float-left">Generate New Graph</p>
					         <b-btn size="sm" class="float-right" variant="primary" @click="showNewColor=true">
					           Confirm
					         </b-btn>
					       </div>
					    </b-modal>
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
	        	<div class="download" v-if="showSecond">
	        		<img class="avatar" width="280px" src="../assets/downloadfile.png" />
	        	</div>
	        	<div class="download" v-if="showNewColor">
	        		<img class="avatar" width="280px" src="../assets/downloadfile_2.png" />
	        	</div>
	    	</b-col>
    	</b-row>
	</b-container>
</template>

<script type="text/babel">

import VuePopper from 'vue-popper-component'
import popover from 'vue-popover'
import VTooltip from 'v-tooltip'

export default {
  name: 'conversation',
  components: {
  	popover,
  	'popper': VuePopper
  	 
  },
  data: function(){
  	return{
  		first: false,
  		second: false,
  		counter: 0,
  		editShow: false,
  		showPopper4: true,
  		showChart: false,
  		showTheme: false,
  		showNewColor: false,
  		showNewGraph: false,
  		variants: [
        'primary', 'secondary', 'success', 'warning', 'danger', 'info', 'light', 'dark'
		],
		headerBgVariant: 'dark',
		headerTextVariant: 'light',
		bodyBgVariant: 'light',
		bodyTextVariant: 'dark',
		footerBgVariant: 'warning',
		footerTextVariant: 'dark'
  	}
  },
  computed:{
  	showFirst(){
  		return this.counter > 0? true: false;
  	},
  	showSecond(){
  		return this.counter > 1? true: false;
  	},
  	showThird(){
  		return this.counter > 2? true: false;
  	},
  },
  methods:{
    // scrollToEnd: function() {    	
    //   var container = this.$refs["main-convo"];
    //   // console.log(this.$refs);
    //   container.scrollTop = container.scrollHeight;
    // },
  }
}


</script>

<style>
.lastQ{
	display: inline-block;
}
.caption-left{
	padding-top: 20px;
	opacity: 0.9;
	background-color: #D6D6D6;
	color: #38ADA9;
}

.caption-left p{
	color: black;
}

.caption-left .btn-primary{
	background-color: #079992;
  	border-color: #079992;
}

.caption-left .btn-primary:hover{
	background-color: #065652;
  	border-color: #065652;
}

.download{
	margin-top: 20px;
}

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

.time{
	margin-top: 10px;
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
    margin: 5px 45px 5px 20px;  
    text-align: left; 
}

.me::before {
    box-shadow: -2px 2px 2px 0 rgba( 178, 178, 178, .4 );
    left: -9px;           
}

.me.chart{
	text-align: center;
}

.you {
    background-color:#dbecff;   
    margin: 5px 20px 5px 45px;    
    text-align: left; 
    max-width: 50%;    
}

.you::before {
	background-color:#dbecff;
    box-shadow: 2px -2px 2px 0 rgba( 178, 178, 178, .4 );
    right: -9px;    
}

.v-popover {
	display: inline-block;
}

.popover-btn{
	padding: 0 7px;
	margin: 5px 0;
}
.popover {
	border: 0;
}
.tooltip {
  display: block !important;
  z-index: 10000;
}

.tooltip .tooltip-inner {
  background: black;
  color: white;
  border-radius: 16px;
  padding: 5px 10px 4px;
}

.tooltip .tooltip-arrow {
  width: 0;
  height: 0;
  border-style: solid;
  position: absolute;
  margin: 5px;
  border-color: black;
  z-index: 1;
}

.tooltip[x-placement^="top"] {
  margin-bottom: 5px;
}

.tooltip[x-placement^="top"] .tooltip-arrow {
  border-width: 5px 5px 0 5px;
  border-left-color: transparent !important;
  border-right-color: transparent !important;
  border-bottom-color: transparent !important;
  bottom: -5px;
  left: calc(50% - 5px);
  margin-top: 0;
  margin-bottom: 0;
}

.tooltip[x-placement^="bottom"] {
  margin-top: 5px;
}

.tooltip[x-placement^="bottom"] .tooltip-arrow {
  border-width: 0 5px 5px 5px;
  border-left-color: transparent !important;
  border-right-color: transparent !important;
  border-top-color: transparent !important;
  top: -5px;
  left: calc(50% - 5px);
  margin-top: 0;
  margin-bottom: 0;
}

.tooltip[x-placement^="right"] {
  margin-left: 5px;
}

.tooltip[x-placement^="right"] .tooltip-arrow {
  border-width: 5px 5px 5px 0;
  border-left-color: transparent !important;
  border-top-color: transparent !important;
  border-bottom-color: transparent !important;
  left: -5px;
  top: calc(50% - 5px);
  margin-left: 0;
  margin-right: 0;
}

.tooltip[x-placement^="left"] {
  margin-right: 5px;
}

.tooltip[x-placement^="left"] .tooltip-arrow {
  border-width: 5px 0 5px 5px;
  border-top-color: transparent !important;
  border-right-color: transparent !important;
  border-bottom-color: transparent !important;
  right: -5px;
  top: calc(50% - 5px);
  margin-left: 0;
  margin-right: 0;
}

.tooltip.popover .popover-inner {
  background: #EEEEEE;
  color: black;
  padding: 24px;
  border-radius: 5px;
  box-shadow: 0 5px 30px rgba(0,0,0,.1);
}

.tooltip.popover .popover-arrow {
  border-color: #EEEEEE;
}

.tooltip[aria-hidden='true'] {
  visibility: hidden;
  opacity: 0;
  transition: opacity .15s, visibility .15s;
}

.tooltip[aria-hidden='false'] {
  visibility: visible;
  opacity: 1;
  transition: opacity .15s;
}

</style>