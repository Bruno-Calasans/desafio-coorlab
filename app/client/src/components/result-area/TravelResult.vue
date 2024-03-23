<template>
  <!-- Confort Travel -->
  <div v-if="travelType === 'confort'" class="flex gap-2">
    <!-- Confort Info -->
    <div class="flex gap-2 items-center bg-zinc-300 rounded-sm w-[70%]">
      <!-- Icon -->
      <div class="flex justify-center items-center bg-cyan-500 h-full w-[20%] rounded-l-md">
        <HandCoins color="white" :size="40" />
      </div>

      <div class="p-3">
        <p class="text-lg text-zinc-800 font-semibold uppercase">
          {{ travel.name }}
        </p>
        <p class="text-zinc-600">Leito: {{ travel.bed }} (completo)</p>
        <p class="text-zinc-600">Tempo Estimado: {{ travel.duration }}</p>
      </div>
    </div>
    <!-- Confort Price -->
    <div class="flex flex-col justify-center bg-zinc-300 p-3 rounded-sm w-[30%]">
      <p class="text-zinc-800 text-lg font-semibold">Preço</p>
      <p class="text-zinc-600">{{ travel.price_confort }}</p>
    </div>
  </div>

  <!-- Economic Travel -->
  <div v-if="travelType === 'economic'" class="flex gap-2">
    <!-- Confort Info -->
    <div class="flex gap-2 items-center bg-zinc-300 rounded-sm w-[70%]">
      <!-- Icon -->
      <div class="flex justify-center items-center bg-cyan-500 h-full w-[20%] rounded-l-md">
        <TimerReset color="white" :size="40" />
      </div>

      <div class="p-2">
        <p class="text-lg text-zinc-800 font-semibold uppercase">
          {{ travel.name }}
        </p>
        <p class="text-zinc-600">Leito: {{ travel.bed }} (convencional)</p>
        <p class="text-zinc-600">Tempo Estimado: {{ travel.duration }}</p>
      </div>
    </div>
    <!-- Confort Price -->
    <div class="flex flex-col justify-center bg-zinc-300 p-2 rounded-sm w-[30%]">
      <p class="text-zinc-800 text-lg font-semibold">Preço</p>
      <p class="text-zinc-600">{{ travel.price_confort }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Travel } from '@/components/calc-travel-form/Travel'
import { HandCoins, TimerReset } from 'lucide-vue-next'

type TravelType = 'confort' | 'economic'

type TravelResultProps = {
  travelType: TravelType
  travel: Travel
}

defineProps<TravelResultProps>()
</script>
