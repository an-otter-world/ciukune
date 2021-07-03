<template lang="pug">
ciu-screen-center(v-if="!me.state")
  ciu-loading-overlay(:loading="me.loading")
    login-view
div(v-else)
  navbar
  router-view
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { ref } from 'vue'
import { onMounted } from 'vue'
import LoginView from './views/login.vue'
import Navbar from './components/navbar.vue'
import { getMeResource } from './api/resources/auth/me'


export default defineComponent({
  name: 'App',
  components: {
    LoginView,
    Navbar
  },
  setup() {
    const loading = ref(false)
    const me = getMeResource()

    onMounted(async () => {
      await me.refresh()
    })

    return {
      loading: loading,
      me: me,
    }
  },
})
</script>

<style>

#app {
  height: 100vh;
}
</style>