<script setup lang="ts">
import { computed, ref } from 'vue'

defineOptions({ inheritAttrs: false })

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
  /** 最大高度，传了则内容超出后滚动 */
  maxHeight?: string
  /** 最大宽度 */
  maxWidth?: string
}>(), {
  accentSide: 'left',
  padding: 1,
  mb: 2,
  matte: true,
})

const isScrollable = computed(() => !!props.maxHeight)

const wrapClass = computed(() => [
  props.matte ? 'card-matte' : '',
  props.mb ? `mb-${props.mb}` : '',
  isScrollable.value ? 'card-scrollable' : '',
].filter(Boolean).join(' '))

const contentClass = computed(() => `p-${props.padding}`)

// 判断是否是左右竖向线条
const isVerticalBar = computed(() => ['left', 'right'].includes(props.accentSide!))

// shift+滚轮横向滚动
const elRef = ref<HTMLDivElement>()
function onWheel(e: WheelEvent) {
  if (!isScrollable.value || !elRef.value) return
  if (e.shiftKey) {
    e.preventDefault()
    elRef.value.scrollLeft += e.deltaY
  }
}
</script>

<template>
  <!-- 外层外壳：布局约束层 -->
  <div
    :class="[wrapClass, 'card-wrap', $attrs.class]"
    :style="(isScrollable ? { maxHeight: maxHeight, maxWidth: maxWidth || '100%' } : {}) as any"
    v-bind="$attrs"
    ref="elRef"
    @wheel="onWheel"
  >
    <!-- 内层内容区 -->
    <div
      :class="['card-content', contentClass]"
      :style="{ '--card-accent': accent } as any"
    >
      <!-- 顶部横向装饰条 -->
      <div v-if="accent && accentSide === 'top'" class="card-bar card-bar-top" />

      <!-- 左右竖向条 + 内容flex容器 -->
      <div v-if="accent && isVerticalBar" class="card-flex-row" :class="`flex-${accentSide}`">
        <div class="card-bar card-bar-vertical" />
        <div v-if="isScrollable" class="scroll-inner card-inner-text">
          <div v-if="title" class="card-title">{{ title }}</div>
          <slot />
        </div>
        <div v-else class="card-inner-text">
          <div v-if="title" class="card-title">{{ title }}</div>
          <slot />
        </div>
      </div>

      <!-- 无竖向条 / 底部条普通内容 -->
      <div v-else>
        <div v-if="title" class="card-title">{{ title }}</div>
        <slot />
      </div>

      <!-- 底部横向装饰条 -->
      <div v-if="accent && accentSide === 'bottom'" class="card-bar card-bar-bottom" />
    </div>
  </div>
</template>

<style scoped>
.card-wrap {
  @apply w-full;
 
}
.card-matte {
  background-color: #532B73;
  filter: none;              /* 覆盖全局 layout.css 的 filter，避免与 overflow 冲突 */
  box-shadow: none;
}
/* 磨砂滤色移到内容层 */
.card-matte .card-content {
  filter: opacity(0.96);
}
.card-scrollable {
  @apply overflow-auto;
  scrollbar-width: none;
  -ms-overflow-style: none;
}
.card-scrollable::-webkit-scrollbar {
  display: none;
}

.card-content {
  width: 100%;
}

/* flex横向布局，竖向线条专用 */
.card-flex-row {
  display: flex;
  gap: 12px;
  align-items: stretch;
}
.flex-right {
  flex-direction: row-reverse;
}
.card-inner-text {
  flex: 1;
}

/* 装饰条基础样式 */
.card-bar {
  background-color: var(--card-accent, #F9D240);
}
.card-bar-vertical {
  width: 4px;
  flex-shrink: 0;
}
.card-bar-top,
.card-bar-bottom {
  height: 4px;
  width: 100%;
}
.card-bar-top {
  margin-bottom: 12px;
}
.card-bar-bottom {
  margin-top: 12px;
}

/* 标题 */
.card-title {
  @apply mb-3 pb-3 text-lg font-bold;
  color: #FFFFFF;
  border-bottom: 1px solid #9D78C2;
}

/* 滚动内容内层包装 */
.scroll-inner {
  padding-bottom: 1.5rem;
}
.scroll-inner :deep(p),
.scroll-inner :deep(h1),
.scroll-inner :deep(h2),
.scroll-inner :deep(h3),
.scroll-inner :deep(div) {
  margin-bottom: 0;
}

/* 文本段落重置 */
.card-content :deep(p) {
  margin: 0.15em 0;
}
.card-content :deep(p:first-child) {
  margin-top: 0;
}
.card-content :deep(p:last-child) {
  margin-bottom: 0;
}
</style>
