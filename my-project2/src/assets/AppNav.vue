<template>
<!-- Fixed navbar -->
<b-navbar toggleable="md" class="border-bottom">

  <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

  <b-navbar-brand href="#"><img src="../assets/menu-logo.png" class="appnav__logo"></b-navbar-brand>

  <b-collapse is-nav id="nav_collapse">

    <b-navbar-nav>
      <b-nav-item ><router-link to="/home">Home</router-link></b-nav-item>
      <b-nav-item href="#"><router-link to="/convo">Conversations</router-link></b-nav-item>
      <b-nav-item href="#"><router-link to="/convo">Help</router-link></b-nav-item>
    </b-navbar-nav>

    <!-- Right aligned nav items -->
    <b-navbar-nav class="ml-auto">
      <b-nav-item-dropdown right>
        <!-- Using button-content slot -->
        <template slot="button-content">
          <em>Alexis S.</em>
          <img src="../assets/user-avatar.png" class="appnav__logo">
        </template>
        <b-dropdown-item href="#">Profile</b-dropdown-item>
        <b-dropdown-item href="#">Log out</b-dropdown-item>
      </b-nav-item-dropdown>
    </b-navbar-nav>

  </b-collapse>
</b-navbar>

</template>

<script>

</script>

<style>
.nav-link:hover, .nav-link:active{
  color: #38ADA9!;
}

.navbar {
  margin-bottom: 20px;
}
.border-bottom{
  border-bottom: 2px solid #E7E7E7  !important;
}

a:hover{
   text-decoration: none;
   color: #F9B550;
}
</style>

