<template>
  <span :class="['atom-text', $attrs.class, type ? `atom-text-${type}` : '']" v-bind="$attrs">
    <slot />
  </span>
</template>

<script setup lang="ts">
defineOptions({ inheritAttrs: false })
withDefaults(defineProps<{
  type?: 'primary' | 'muted' | 'data' | 'total'
}>(), { type: undefined })
</script>

<style scoped>
.atom-text { color: var(--theme-text-white); }
.atom-text-primary { color: var(--theme-text-white); font-weight: 700; }
.atom-text-muted { color: var(--theme-text-gray); }
.atom-text-data { color: var(--theme-text-yellow); font-weight: 700; }
.atom-text-total { color: var(--theme-text-red-total); font-weight: 700; font-size: 1.25rem; }
</style>
