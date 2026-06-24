<script setup lang="ts">
interface TocItem {
  /** 序号，如 "①" */
  number: string
  /** 图标 emoji */
  icon?: string
  /** 标题 */
  title: string
  /** 补充说明 */
  desc?: string
  /** 谁应该看，如 "🌟 所有人"、"🟡 技术参考" */
  tag?: string
}

defineProps<{
  items: TocItem[]
}>()
</script>

<template>
  <div class="toc w-full">
    <div v-for="item in items" :key="item.number" class="toc-row">
      <span class="toc-number">{{ item.icon }}{{ item.number }}</span>
      <div class="toc-body">
        <span class="toc-title">{{ item.title }}</span>
        <span v-if="item.desc" class="toc-desc"> — {{ item.desc }}</span>
      </div>
      <span v-if="item.tag" class="toc-tag">{{ item.tag }}</span>
    </div>
  </div>
</template>

<style scoped>
.toc-row {
  @apply flex items-center gap-4 py-3;
  border-bottom: 1px solid var(--theme-divider-line);
}
.toc-row:last-child {
  border-bottom: none;
}
.toc-number {
  @apply text-xl whitespace-nowrap;
}
.toc-body {
  @apply flex-1 min-w-0;
}
.toc-title {
  @apply font-semibold;
  color: var(--theme-text-white);
}
.toc-desc {
  color: var(--theme-text-gray);
}
.toc-tag {
  @apply px-3 py-1 text-xs rounded whitespace-nowrap;
  background-color: var(--theme-card-bg);
  color: var(--theme-text-gray);
}
</style>
