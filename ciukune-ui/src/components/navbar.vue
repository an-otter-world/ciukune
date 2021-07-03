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
      ciu-router-link(to="/profile" icon="user-circle") {{ $t('navbar.profile') }}
      ciu-router-link(to="logout" icon="sign-out-alt") {{ $t('navbar.logout') }}
</template>
