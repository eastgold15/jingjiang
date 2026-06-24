<template>
  <div :class="['atom-flex', $attrs.class]" v-bind="$attrs">
    <slot />
  </div>
</template>

<script setup lang="ts">
defineOptions({ inheritAttrs: false })
</script>

<style scoped>
.atom-flex {
  display: flex;
}
</style>
