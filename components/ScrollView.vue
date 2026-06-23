<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps<{
  maxHeight?: string
  maxWidth?: string
}>()

const elRef = ref<HTMLDivElement>()

function onWheel(e: WheelEvent) {
  if (!elRef.value) return
  if (e.shiftKey) {
    e.preventDefault()
    elRef.value.scrollLeft += e.deltaY
  }
  // 默认行为就是垂直滚动，不做额外操作
}
</script>

<template>
  <div
    ref="elRef"
    class="scroll-view"
    :style="{
      maxHeight: maxHeight || '100%',
      maxWidth: maxWidth || '100%',
    }"
    @wheel="onWheel"
  >
    <slot />
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
</style>
