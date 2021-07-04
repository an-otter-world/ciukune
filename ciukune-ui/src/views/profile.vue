<template lang="pug">
ciu-component
  header
    h1 Profile
  ciu-api-form(:resource="me")
    ciu-api-errors
    ciu-api-input(field="email")
      ciu-text-field(:placeholder="$t('profile.email')" v-model="me.state.email")
    ciu-api-input(field="username" patch)
      ciu-text-field(:placeholder="$t('profile.username')" v-model="me.state.username")
ciu-component
  header
    h1 Change Password
  ciu-api-form(:resource="me")
    ciu-api-errors
    ciu-api-input(field="email")
      ciu-text-field(:placeholder="$t('profile.email')" password v-model="email")
    ciu-api-input(field="username")
      ciu-text-field(:placeholder="$t('profile.username')" v-model="username")
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { getMeResource } from '../api/resources/user/me'

export default defineComponent({
    setup() {
      const me = getMeResource()

      return {
	      me,
        email: me.state.email,
	      username: me.state.username,
      }
    },
})
</script>
