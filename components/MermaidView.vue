<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps<{
  maxHeight?: string
}>()

const scale = ref(1)
const contentRef = ref<HTMLDivElement>()

function zoomIn() { scale.value = Math.min(scale.value + 0.25, 3); apply() }
function zoomOut() { scale.value = Math.max(scale.value - 0.25, 0.25); apply() }
function reset() { scale.value = 1; apply() }
function apply() {
  if (!contentRef.value) return
  contentRef.value.style.transform = `scale(${scale.value})`
}

function onWheel(e: WheelEvent) {
  if (!e.ctrlKey && !e.metaKey) return
  e.preventDefault()
  const d = e.deltaY > 0 ? -0.1 : 0.1
  scale.value = Math.max(0.25, Math.min(3, scale.value + d))
  apply()
}
</script>

<template>
  <div class="mermaid-wrap">
    <div class="mermaid-toolbar">
      <span class="mermaid-zoom-label">{{ Math.round(scale * 100) }}%</span>
      <button class="mermaid-btn" title="缩小" @click="zoomOut">−</button>
      <button class="mermaid-btn" title="重置" @click="reset">⟲</button>
      <button class="mermaid-btn" title="放大" @click="zoomIn">+</button>
    </div>
    <div
      class="mermaid-scroll"
      :style="{ maxHeight: maxHeight || '400px' }"
      @wheel="onWheel"
    >
      <div ref="contentRef" class="mermaid-content">
        <slot />
      </div>
    </div>
  </div>
</template>

<style scoped>
.mermaid-wrap { @apply relative; }
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
.mermaid-scroll {
  @apply overflow-auto rounded-lg border border-white/10;
  background: rgba(0,0,0,.15);
}
.mermaid-content { @apply transition-transform duration-200; }
</style>
