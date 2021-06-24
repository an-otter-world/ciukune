<template lang="pug">
div(class="ciu-primary ciu-navbar")
  div(class="ciu-brand")
    slot(name="brand")
  div(class="ciu-menu" v-on:focusout="isOpened = false")
    a(href="#" v-on:click="isOpened = !isOpened")
      ciu-icon(icon="bars")
    div(class="ciu-links" v-bind:class="{ 'ciu-opened': isOpened }")
      slot
  div(class="ciu-end")
    slot(name="end")
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { ref } from 'vue'

export default defineComponent({
  setup() {
    const isOpened = ref(false);

    return {
      isOpened,
    }
  },
})
</script>

<style>
.ciu-navbar {
  display: flex;
  align-items: stretch;
}

.ciu-navbar > div {
  align-items: center;
  display: flex;
}

.ciu-navbar > .ciu-brand {
  flex-grow: 0;
  margin-left: var(--ciu-spacing);
  margin-right: var(--ciu-spacing);
}

.ciu-navbar.ciu-responsive > .ciu-brand {
  flex-grow: 1;
  order: 1;
}

.ciu-navbar > .ciu-menu {
  display: flex;
  flex-grow: 1;
}

.ciu-navbar.ciu-responsive > .ciu-menu {
  flex-direction: column;
  flex-grow: 0;
}

.ciu-navbar > .ciu-menu > a {
  display: none;
}

.ciu-navbar.ciu-responsive > .ciu-menu > a {
  display: inline;
}

.ciu-navbar > .ciu-menu > .ciu-links {
  display: flex;
}

.ciu-navbar.ciu-responsive > .ciu-menu > .ciu-links {
  background: var(--ciu-primary);
  flex-direction: column;
  left: 0;
  display: none;
  padding: calc(0.5 * var(--ciu-spacing));
  position: absolute;
  top: 3rem;
}

.ciu-navbar.ciu-responsive > .ciu-menu > .ciu-links.ciu-opened {
  display: flex;
}

.ciu-navbar > .ciu-end {
  flex-grow: 0;
  margin-left: var(--ciu-spacing);
  margin-right: var(--ciu-spacing);
}

.ciu-navbar.ciu-responsive > .ciu-end {
  order: 2;
}

.ciu-navbar a {
  align-items: center;
  padding: var(--ciu-spacing);
  text-transform: uppercase;
}

.ciu-navbar a:hover {
  background-color: var(--ciu-primary-light);
  text-decoration: none;
}

.ciu-navbar a.router-link-active {
  background-color: var(--ciu-primary-dark);
  text-transform: uppercase;
}
</style>
