<template lang="pug">
ciu-navbar
  template(v-slot:brand)
    h1 Ciu Kune
  router-link(to="/") Home
  router-link(to="/test") Test
  template(v-slot:end)
    ciu-dropdown
      template(#header)
        ciu-icon(icon="user-circle")
      router-link(to="logout")
        div(class="ciu-flex-row")
          ciu-icon(icon="sign-out-alt")
          div Logout
</template>
