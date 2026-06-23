<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  /** 左侧装饰条颜色，默认金黄 */
  accent?: string
  /** 是否显示装饰条 */
  showAccent?: boolean
  /** 内边距 (p-X)，默认 6 */
  padding?: number
  /** 卡片底部外边距 */
  mb?: number
  /** 尺寸: normal | full | sm */
  size?: 'normal' | 'full' | 'sm'
  /** 标题（可选） */
  title?: string
}>(), {
  accent: '#F9D240',
  showAccent: true,
  padding: 6,
  mb: 0,
  size: 'normal',
})

const cardClass = computed(() => [
  'card-matte',
  `p-${props.padding}`,
  props.mb ? `mb-${props.mb}` : '',
  props.showAccent ? 'card-accent-left' : '',
  props.size === 'full' ? 'card-full-width' : '',
  props.size === 'sm' ? 'card-sm' : '',
].filter(Boolean).join(' '))
</script>

<template>
  <div
    :class="cardClass"
    :style="{
      '--card-accent': accent,
    } as any"
  >
    <div v-if="title" class="card-title">{{ title }}</div>
    <slot />
  </div>
</template>

<style scoped>
.card-matte {
  background-color: #532B73;
  filter: opacity(0.96);
  box-shadow: none;
}
.card-full-width {
  @apply mt-6 w-full;
  background-color: #4C2668;
}
.card-sm {
  @apply p-4;
}
.card-accent-left {
  @apply relative;
}
.card-accent-left::before {
  content: '';
  @apply absolute left-0 top-0 bottom-0 w-1;
  background-color: var(--card-accent, #F9D240);
}
.card-title {
  @apply mb-3 pb-3 text-lg font-bold;
  color: #FFFFFF;
  border-bottom: 1px solid #9D78C2;
}
</style>
