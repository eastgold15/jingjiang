<template>
  <div :class="['atom-box', $attrs.class, { 'atom-box-bordered': bordered }]" v-bind="$attrs">
    <slot />
  </div>
</template>

<script setup lang="ts">
defineOptions({ inheritAttrs: false })
withDefaults(defineProps<{ bordered?: boolean }>(), { bordered: false })
</script>

<style scoped>
.atom-box {
  background: transparent;
  color: var(--text-primary);
}
.atom-box-bordered {
  border: 1px solid var(--border);
}
</style>
