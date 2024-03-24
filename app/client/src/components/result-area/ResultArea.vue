<template>
  <div class="flex flex-col grow-2 w-full p-3">
    <!-- No Travels -->
    <div
      class="flex text-zinc-800 text-2xl font-semibold flex-1 items-center justify-center"
      v-if="!travels"
    >
      Nenhum dado selecionado
    </div>
    <!-- Travels -->
    <div class="flex flex-col gap-4 flex-1 justify-center" v-if="travels">
      <div class="text-lg text-zinc-600 font-semibold">
        Estas são as melhores alternativas de viagem para a data selecionada.
      </div>
      <div class="flex flex-col gap-3">
        <TravelResult travelType="confort" :travel="travels.confort" />
        <TravelResult travelType="economic" :travel="travels.economic" />
      </div>
    </div>

    <!-- Clear Btn -->
    <div v-if="travels" class="flex items-center justify-end">
      <Button
        @click="onClear"
        size="sm"
        class="font-semibold bg-amber-500 hover:bg-amber-400 h-7 w-32"
      >
        Limpar
      </Button>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { BestTravels } from '@/components/calc-travel-form/Travel'
import TravelResult from '@/components/result-area/TravelResult.vue'
import Button from '../ui/button/Button.vue'

type ResultAreaProps = {
  travels: BestTravels | null
  onClear: () => void
}

defineProps<ResultAreaProps>()
</script>
