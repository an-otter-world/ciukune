<template>
  <svg width="24" height="24"
    xmlns="http://www.w3.org/2000/svg"
    :viewBox="`0 0 ${width} ${height}`"
  >
    <path fill="currentColor" :d="svgPath" />
  </svg>
</template>

<script>
import { defineComponent, computed } from "vue";
import { findIconDefinition } from "@fortawesome/fontawesome-svg-core";

export default defineComponent({
  props: {
    icon: {
      type: String,
      required: true
    },
    type: {
      type: String,
      default: "fas",
      required: false
    },
  },

  setup(props) {
    const definition = computed(() =>
      findIconDefinition({
        prefix: props.type,
        iconName: props.icon
      })
    );

    const width = computed(() => definition.value.icon[0]);
    const height = computed(() => definition.value.icon[1]);
    const svgPath = computed(() => definition.value.icon[4]);

    return { width, height, svgPath };
  }
});
</script>
