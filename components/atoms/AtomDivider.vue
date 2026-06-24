<template>
  <div :class="['atom-divider', $attrs.class]" v-bind="$attrs" />
</template>

<script setup lang="ts">
defineOptions({ inheritAttrs: false })
</script>

<style scoped>
.atom-divider {
  width: 100%;
  height: 1px;
  background: var(--theme-divider-line);
}
</style>
