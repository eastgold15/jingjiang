<script setup lang="ts">
const props = defineProps({
  background: {
    type: String,
    default: undefined,
  },
})
</script>

<template>
  <div class="slidev-layout circle-tl-br">
    <slot />
  </div>
</template>
