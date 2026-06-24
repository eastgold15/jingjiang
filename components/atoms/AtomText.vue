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
.atom-text { color: var(--text-primary); }
.atom-text-primary { color: var(--text-primary); font-weight: 700; }
.atom-text-muted { color: var(--text-muted); }
.atom-text-data { color: var(--text-emphasis); font-weight: 700; }
.atom-text-total { color: var(--text-danger); font-weight: 700; font-size: 1.25rem; }
</style>
