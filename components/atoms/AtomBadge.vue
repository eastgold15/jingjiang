<template>
  <span :class="['atom-badge', $attrs.class, `atom-badge-${type}`]" v-bind="$attrs">
    <slot />
  </span>
</template>

<script setup lang="ts">
defineOptions({ inheritAttrs: false })
withDefaults(defineProps<{
  type?: 'primary' | 'success' | 'warning' | 'info' | 'default'
}>(), { type: 'default' })
</script>

<style scoped>
.atom-badge {
  display: inline-block;
  padding: 0.125rem 0.5rem;
  font-size: 0.75rem;
  background: var(--bg-card);
  color: var(--text-muted);
}
.atom-badge-primary { background: var(--text-emphasis); color: #42205C; }
.atom-badge-success { background: #6BCB9C; color: #fff; }
.atom-badge-warning { background: #FFB74D; color: #fff; }
.atom-badge-info { background: #7EC8E3; color: #fff; }
.atom-badge-default { background: var(--bg-card); color: var(--text-muted); }
</style>
