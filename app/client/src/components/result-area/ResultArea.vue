<template>
  <div class="flex grow-2 w-full items-center p-2">
    <!-- No Travels -->
    <div
      class="flex text-zinc-800 text-2xl font-semibold flex-1 justify-center"
      v-if="!travels.length"
    >
      Nenhum dado selecionado
    </div>
    <!-- Travels -->
    <div class="flex flex-col gap-4 self-center flex-1" v-if="travels.length">
      <div class="text-lg text-zinc-800">
        Estas são as melhores alternativas de viagem para a data selecionada.
      </div>
      <div class="flex flex-col gap-3">
        <TravelResult travelType="confort" :travel="travels[0]" />
        <TravelResult travelType="economic" :travel="travels[0]" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Travel } from '@/components/calc-travel-form/Travel'
import TravelResult from '@/components/result-area/TravelResult.vue'

type ResultAreaProps = {
  travels: Travel[]
}

defineProps<ResultAreaProps>()
</script>
