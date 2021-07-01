<template lang="pug">
div(class="ciu-dropdown")
  header
    a(href="#" @click="toggle()")
      slot(name="header")
        ciu-icon(icon="chevron-down")
    div(v-if="isOpen" @click="isOpen = false")
      slot
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { ref } from 'vue'

export default defineComponent({
  setup() {
    let isOpen = ref(false);
    let toggle = () => {
      isOpen.value = !isOpen.value;
    }
    return {
      isOpen,
      toggle
    }
  },
})
</script>

<style>
.ciu-dropdown > header {
  position: relative;
  vertical-align: middle;
}

.ciu-dropdown > * > a {
  align-content: center;
  display: flex;
}

.ciu-dropdown > * > a > * {
  margin-left: var(--ciu-spacing);
  margin-right: var(--ciu-spacing);
}

.ciu-dropdown > div {
  background: var(--ciu-primary);
  border-bottom-left-radius: var(--ciu-on-primary);
  border-bottom-right-radius: var(--ciu-on-primary);
  border-top: 1px solid var(--ciu-color);
  display:block;
  padding: var(--ciu-spacing);
  position: absolute;
}
</style>
