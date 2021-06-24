<template lang="pug">
div(class="ciu-flex-row ciu-primary ciu-navbar")
  div(class="ciu-brand")
    slot(name="brand")
  div(class="ciu-links")
    slot
  div(class="ciu-end")
    slot(name="end")
</template>

<style>
.ciu-navbar {
  align-items: stretch;
}

.ciu-navbar > div {
  display: flex;
  align-items: center;
}

.ciu-navbar > .ciu-brand {
  flex-grow: 0;
  margin-left: var(--ciu-spacing);
  margin-right: var(--ciu-spacing);
}

.ciu-navbar > .ciu-end {
  flex-grow: 0;
  margin-left: var(--ciu-spacing);
  margin-right: var(--ciu-spacing);
}

.ciu-navbar > .ciu-links {
  flex-grow: 1;
}

.ciu-navbar > .ciu-links > a {
  text-transform: uppercase;
  align-items: center;
  padding: var(--ciu-spacing);
}

.ciu-navbar a:hover {
  background-color: var(--ciu-primary-light);
}

.ciu-navbar a.router-link-active {
  background-color: var(--ciu-primary-dark);
  text-transform: uppercase;
}

</style>

