<template lang="pug">
div(class="ciu-primary ciu-navbar ciu-responsive")
  div(class="ciu-brand")
    slot(name="brand")
  div(class="ciu-menu")
    a(href="#")
      ciu-icon(icon="bars")
    div(class="ciu-links")
      slot
  div(class="ciu-end")
    slot(name="end")
</template>

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
  padding: calc(0.5 * var(--ciu-spacing));
  position: absolute;
  top: 3rem;
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
}

.ciu-navbar a.router-link-active {
  background-color: var(--ciu-primary-dark);
  text-transform: uppercase;
}
</style>
