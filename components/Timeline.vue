<script setup lang="ts">
interface TimelineStep {
  /** 图标 emoji */
  icon?: string
  /** 阶段名称 */
  label: string
  /** 时间周期 */
  period?: string
  /** 补充描述 */
  desc?: string
  /** 左侧装饰条色 */
  accent?: string
}

defineProps<{
  steps: TimelineStep[]
}>()
</script>

<template>
  <div class="timeline">
    <div v-for="(step, i) in steps" :key="i" class="timeline-step" :style="step.accent ? { '--step-accent': step.accent } as any : {}">
      <div class="step-accent-bar" />
      <div class="step-icon">{{ step.icon || '📌' }}</div>
      <div class="step-label">{{ step.label }}</div>
      <div v-if="step.period" class="step-period">{{ step.period }}</div>
      <div v-if="step.desc" class="step-desc">{{ step.desc }}</div>
    </div>
  </div>
</template>

<style scoped>
.timeline {
  @apply grid w-full gap-3;
  grid-template-columns: repeat(auto-fit, minmax(0, 1fr));
}
.timeline-step {
  @apply relative p-4 pt-6 text-center;
  background-color: var(--bg-card);
  filter: opacity(0.96);
}
.step-accent-bar {
  @apply absolute top-0 left-0 right-0 h-1;
  background-color: var(--step-accent, var(--accent));
}
.step-icon {
  @apply text-2xl mb-2;
}
.step-label {
  @apply text-sm font-bold;
  color: var(--text-primary);
}
.step-period {
  @apply text-xs mt-1;
  color: var(--text-emphasis);
}
.step-desc {
  @apply text-xs mt-1;
  color: var(--text-muted);
}
</style>
