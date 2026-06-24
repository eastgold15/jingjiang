<template>
  <button :class="['atom-btn', $attrs.class, `atom-btn-${type}`]" v-bind="$attrs" @click="handleClick">
    <slot />
  </button>
</template>

<script setup lang="ts">
defineOptions({ inheritAttrs: false })
withDefaults(defineProps<{
  type?: 'primary' | 'default'
}>(), { type: 'default' })

const emit = defineEmits<{ click: [e: MouseEvent] }>()
const handleClick = (e: MouseEvent) => emit('click', e)
</script>

<style scoped>
.atom-btn {
  padding: 0.375rem 1rem;
  border: none;
  cursor: pointer;
  font-size: 0.875rem;
  background: var(--bg-card);
  color: var(--text-primary);
}
.atom-btn-primary {
  background: var(--text-emphasis);
  color: #42205C;
  font-weight: 700;
}
.atom-btn:hover {
  filter: brightness(1.1);
}
</style>
