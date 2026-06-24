<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  /** 装饰条颜色，不传则不显示装饰条 */
  accent?: string
  /** 装饰条位置 */
  accentSide?: 'left' | 'right' | 'top' | 'bottom'
  /** 内边距 (p-X)，默认 6 */
  padding?: number
  /** 底部外边距 */
  mb?: number
  /** 磨砂背景，默认 true */
  matte?: boolean
  /** 标题（可选） */
  title?: string
}>(), {
  accentSide: 'left',
  padding: 6,
  mb: 0,
  matte: true,
})

const cardClass = computed(() => [
  props.matte ? 'card-matte' : '',
  props.mb ? `mb-${props.mb}` : '',
  `p-${props.padding}`,
].filter(Boolean).join(' '))
</script>

<template>
  <div :class="cardClass" class="card-base" :style="{ '--card-accent': accent } as any">
    <div v-if="accent" class="card-accent" :class="`card-accent-${accentSide}`" />
    <div v-if="title" class="card-title">{{ title }}</div>
    <slot />
  </div>
</template>

<style scoped>
.card-base {
  @apply w-full;
  position: relative;
}
.card-matte {
  background-color: #532B73;
  filter: opacity(0.96);
  box-shadow: none;
}

/* 装饰条 */
.card-accent {
  position: absolute;
  background-color: var(--card-accent, #F9D240);
}
.card-accent-left {
  left: 0;
  top: 0;
  bottom: 0;
  width: 4px;
}
.card-accent-right {
  right: 0;
  top: 0;
  bottom: 0;
  width: 4px;
}
.card-accent-top {
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
}
.card-accent-bottom {
  bottom: 0;
  left: 0;
  right: 0;
  height: 4px;
}

/* 标题（带底部分割线） */
.card-title {
  @apply mb-3 pb-3 text-lg font-bold;
  color: #FFFFFF;
  border-bottom: 1px solid #9D78C2;
}

/* 消除 Markdown 空行产生的 p 标签间距 */
.card-base :deep(p) {
  margin: 0.15em 0;
}
.card-base :deep(p:first-child) {
  margin-top: 0;
}
.card-base :deep(p:last-child) {
  margin-bottom: 0;
}
</style>
