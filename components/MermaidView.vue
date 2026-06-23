<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps<{
  maxHeight?: string
}>()

const scale = ref(1)
let tx = 0, ty = 0
const dragging = ref(false)
let dragStartX = 0, dragStartY = 0
let dragTx = 0, dragTy = 0

const wrapRef = ref<HTMLDivElement>()
const contentRef = ref<HTMLDivElement>()

function apply() {
  if (!contentRef.value) return
  contentRef.value.style.transform = `translate(${tx}px, ${ty}px) scale(${scale.value})`
}

function zoomIn() {
  centerZoom(scale.value + 0.25)
}

function zoomOut() {
  centerZoom(scale.value - 0.25)
}

function reset() {
  scale.value = 1; tx = 0; ty = 0; apply()
}

function centerZoom(newScale: number) {
  const wrap = wrapRef.value
  if (!wrap) return
  const cx = wrap.clientWidth / 2
  const cy = wrap.clientHeight / 2
  const mc = (cx - tx) / scale.value
  const my = (cy - ty) / scale.value
  newScale = Math.max(0.25, Math.min(3, newScale))
  tx = cx - mc * newScale
  ty = cy - my * newScale
  scale.value = newScale
  apply()
}

function onMouseDown(e: MouseEvent) {
  if (e.button !== 0) return
  dragging.value = true
  dragStartX = e.clientX
  dragStartY = e.clientY
  dragTx = tx
  dragTy = ty
  window.addEventListener('mousemove', onMouseMove)
  window.addEventListener('mouseup', onMouseUp)
}

function onMouseMove(e: MouseEvent) {
  if (!dragging.value) return
  tx = dragTx + (e.clientX - dragStartX)
  ty = dragTy + (e.clientY - dragStartY)
  apply()
}

function onMouseUp() {
  dragging.value = false
  window.removeEventListener('mousemove', onMouseMove)
  window.removeEventListener('mouseup', onMouseUp)
}

function onWheel(e: WheelEvent) {
  e.preventDefault()
  const wrap = wrapRef.value
  if (!wrap) return
  const rect = wrap.getBoundingClientRect()
  const mx = e.clientX - rect.left
  const my = e.clientY - rect.top
  // 鼠标在内容坐标系中的位置
  const mc = (mx - tx) / scale.value
  const myc = (my - ty) / scale.value
  // 计算新缩放
  const delta = e.deltaY > 0 ? -0.12 : 0.12
  const ns = Math.max(0.25, Math.min(3, scale.value + delta))
  // 调整 translate 使鼠标位置不动
  tx = mx - mc * ns
  ty = my - myc * ns
  scale.value = ns
  apply()
}
</script>

<template>
  <div class="mermaid-wrap" :style="{ maxHeight: maxHeight || '400px' }">
    <div class="mermaid-toolbar">
      <span class="mermaid-zoom-label">{{ Math.round(scale * 100) }}%</span>
      <button class="mermaid-btn" title="缩小" @click="zoomOut">−</button>
      <button class="mermaid-btn" title="重置" @click="reset">⟲</button>
      <button class="mermaid-btn" title="放大" @click="zoomIn">+</button>
    </div>
    <div ref="wrapRef" class="mermaid-view" :class="{ grabbing: dragging }" @wheel="onWheel" @mousedown="onMouseDown">
      <div ref="contentRef" class="mermaid-content">
        <slot />
      </div>
    </div>
  </div>
</template>

<style scoped>
.mermaid-wrap {
  @apply relative overflow-hidden rounded-lg border border-white/10;
  background: rgba(0,0,0,.15);
}
.mermaid-toolbar {
  @apply flex items-center gap-1 absolute top-2 right-2 z-10 px-2 py-1 rounded-lg;
  background: rgba(0,0,0,.55);
  backdrop-filter: blur(4px);
}
.mermaid-zoom-label {
  @apply text-xs text-white/70 min-w-[3rem] text-right mr-1;
  font-variant-numeric: tabular-nums;
}
.mermaid-btn {
  @apply w-6 h-6 flex items-center justify-center rounded text-sm text-white/80 border border-white/20 cursor-pointer select-none;
  background: rgba(255,255,255,.1);
}
.mermaid-btn:hover { background: rgba(255,255,255,.25); }
.mermaid-view {
  @apply w-full overflow-hidden cursor-grab;
  height: inherit;
}
.mermaid-view.grabbing { @apply cursor-grabbing; }
.mermaid-content { transform-origin: 0 0; }
</style>
