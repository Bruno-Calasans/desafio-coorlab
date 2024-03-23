<template>
  <div class="flex gap-2">
    <div class="flex gap-2 items-center bg-zinc-300 rounded-sm w-[70%]">
      <!-- Icon -->
      <div class="flex justify-center items-center bg-cyan-500 h-full w-[20%] rounded-l-md">
        <HandCoins v-if="travelType === 'confort'" color="white" :size="40" />
        <TimerReset v-if="travelType === 'economic'" color="white" :size="40" />
      </div>

      <!-- Travel Info -->
      <div class="p-3">
        <p class="text-md text-zinc-800 font-semibold uppercase">
          {{ travel.name }}
        </p>
        <!-- Confort -->
        <p v-if="travelType === 'confort'" class="text-zinc-800">
          Leito: {{ travel.bed }} (completo)
        </p>
        <!-- Economic -->
        <p v-if="travelType === 'economic'" class="text-zinc-800">
          Poltrona: {{ travel.seat }} (convencional)
        </p>
        <p class="text-zinc-800">Tempo Estimado: {{ travel.duration }}</p>
      </div>
    </div>
    <!-- Travel Price -->
    <div class="flex flex-col justify-center bg-zinc-300 p-3 rounded-sm w-[30%]">
      <p class="text-zinc-800 text-lg font-semibold">Preço</p>
      <!-- Confort -->
      <p v-if="travelType === 'confort'" class="text-zinc-800">{{ travel.price_confort }}</p>
      <!-- Economic -->
      <p v-if="travelType === 'economic'" class="text-zinc-800">{{ travel.price_econ }}</p>
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
