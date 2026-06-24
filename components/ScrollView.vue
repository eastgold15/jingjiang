<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps<{
  maxHeight?: string
  maxWidth?: string
}>()

const elRef = ref<HTMLDivElement>()

function onWheel(e: WheelEvent) {
  if (!elRef.value) return
  const el = elRef.value
  if (e.shiftKey) {
    e.preventDefault()
    el.scrollLeft += e.deltaY
  }
}
</script>

<template>
  <!-- 外层滚动容器，只负责滚动、隐藏滚动条 -->
  <div
    ref="elRef"
    class="scroll-view"
    :style="{
      maxHeight: maxHeight || '100%',
      maxWidth: maxWidth || '100%',
    }"
    @wheel="onWheel"
  >
    <!-- 内层包装器：一劳永逸处理margin、底部缓冲 -->
    <div class="scroll-inner">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.scroll-view {
  @apply overflow-auto;
  scrollbar-width: none;
  -ms-overflow-style: none;
}
.scroll-view::-webkit-scrollbar {
  display: none;
}

/* 内层包装器永久修复配置 */
.scroll-inner {
  /* 底部内边距缓冲，留白永远在容器内部，不会溢出 */
  padding-bottom: 1.5rem;
}

/* 清空所有子元素底部外边距，从根源消除多余scrollHeight增量 */
.scroll-inner :deep(p),
.scroll-inner :deep(h1),
.scroll-inner :deep(h2),
.scroll-inner :deep(h3),
.scroll-inner :deep(div) {
  margin-bottom: 0;
}
</style>