<script setup lang="ts">
interface OutlineItem {
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
  items: OutlineItem[]
}>()
</script>

<template>
  <div class="outline w-full">
    <div v-for="item in items" :key="item.number" class="outline-row">
      <span class="outline-number">{{ item.icon }}{{ item.number }}</span>
      <div class="outline-body">
        <span class="outline-title">{{ item.title }}</span>
        <span v-if="item.desc" class="outline-desc"> — {{ item.desc }}</span>
      </div>
      <span v-if="item.tag" class="outline-tag">{{ item.tag }}</span>
    </div>
  </div>
</template>

<style scoped>
.outline-row {
  @apply flex items-center gap-4 py-3;
  border-bottom: 1px solid var(--theme-divider-line);
}
.outline-row:last-child {
  border-bottom: none;
}
.outline-number {
  @apply text-xl whitespace-nowrap;
}
.outline-body {
  @apply flex-1 min-w-0;
}
.outline-title {
  @apply font-semibold;
  color: var(--theme-text-white);
}
.outline-desc {
  color: var(--theme-text-gray);
}
.outline-tag {
  @apply px-3 py-1 text-xs rounded whitespace-nowrap;
  background-color: var(--theme-card-bg);
  color: var(--theme-text-gray);
}
</style>
