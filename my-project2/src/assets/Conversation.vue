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
</script>

<style>
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


</style>