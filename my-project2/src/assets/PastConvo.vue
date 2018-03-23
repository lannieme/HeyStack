<template>
<div class="past-convo container">
    <div class="row">
        <div class="col-md-12">
            <input class="search form-control" placeholder="Search" />
            <button class="sort btn btn-primary" data-sort="date">
        Sort by Date</button>
            <button class="sort btn btn-primary" data-sort="title">
        Sort by Title</button>
        </div>
    </div> 

    <div class="row">
        <div class="col-md-12">
            <b-list-group class="list">
                <b-list-group-item class="d-flex justify-content-between align-items-center">
                    
                    <img src="../assets/convo2.png" fluid alt="Responsive image" class="pull-left photo"/>
                    <p class="title">Engagement rate</p>
                    <b-badge variant="primary" class="date" pill>March 3rd</b-badge>
                </b-list-group-item>
                <b-list-group-item class="d-flex justify-content-between align-items-center">
                    
                    <img src="../assets/convo3.png" fluid alt="Responsive image" class="pull-left photo"/>
                    <p class="title">Marketing email</p>
                    <b-badge variant="primary" class="date"  pill>March 1st</b-badge>
                </b-list-group-item>
                <b-list-group-item class="d-flex justify-content-between align-items-center">
                    
                    <img src="../assets/HSavatar60.png" fluid alt="Responsive image" class="pull-left photo"/>
                    <p class="title">Conversion rate</p>
                    <b-badge variant="primary"  class="date" pill>March 1st</b-badge>
                </b-list-group-item>
            </b-list-group>
        </div>
    </div> <!-- end of row -->
</div>

</template>

<script>
export default {
  data: () => ({
  }),
  created() {
    let listScript = document.createElement('script')
    listScript.setAttribute('src', 'https://cdnjs.cloudflare.com/ajax/libs/list.js/1.5.0/list.min.js')
    document.head.appendChild(listScript)
  },
  methods: {
  }
}

var options = {
  valueNames: [ 'title', 'date' ]
};

// var userList = new List('past-convo', options);


</script>

<style>
h1 {
  text-align:center;
}
.row {
  margin-top: 10px;
  margin-bottom: 10px;
}
.badge-primary{
    background-color: #7DC9C7;
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

</style>

