<script setup lang="ts">
import { computed } from 'vue'
import type { CSSProperties } from 'vue'

const props = defineProps({
  background: {
    type: String,
    default: undefined,
  },
})

function resolveAssetUrl(url: string) {
  return url.startsWith('/') ? import.meta.env.BASE_URL + url.slice(1) : url
}

function handleBackground(background?: string, dim = false, backgroundSize = 'cover'): CSSProperties {
  const isColor = background && (background[0] === '#' || background.startsWith('rgb'))
  const style: CSSProperties = {
    background: isColor ? background : undefined,
    color: background && !isColor ? 'white' : undefined,
    backgroundImage: isColor
      ? undefined
      : background
        ? dim
          ? `linear-gradient(#0005, #0008), url(${resolveAssetUrl(background)})`
          : `url("${resolveAssetUrl(background)}")`
        : undefined,
    backgroundRepeat: 'no-repeat',
    backgroundPosition: 'center',
    backgroundSize,
  }
  if (!style.background) delete style.background
  return style
}

const style = computed(() => handleBackground(props.background))
</script>

<template>
  <div class="slidev-layout intro" :style="style">
    <div class="my-auto">
      <slot />
    </div>
  </div>
</template>
