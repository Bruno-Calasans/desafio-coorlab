<template>
  <main class="flex-1">
    <!--Main Header -->
    <header class="h-14 p-2 text-black shadow-md flex justify-end items-center">
      <p class="text-lg text-zinc-700">Bem-vindo, <span class="font-bold italic">usuário</span></p>
    </header>

    <div class="text-black flex gap-2 flex-col h-[60%] w-full p-3 shadow-md">
      <!-- Form Title -->
      <header
        class="rounded-t-sm p-3 h-14 bg-slate-900 w-full text-white flex items-center font-bold mb-3"
      >
        Calculadora de Viagem
      </header>
      <div class="flex flex-1">
        <!-- Form -->
        <CalcFormTravel :onSucessSubmit="updateTravels" />

        <!-- Result Area -->
        <ResultArea :travels="travels" :onClear="clearTravels" />
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import CalcFormTravel from '@/components/calc-travel-form/CalcTravelForm.vue'
import ResultArea from '@/components/result-area/ResultArea.vue'
import type { Travel } from '@/components/calc-travel-form/Travel'

const travels = ref<Travel[]>([])
const updateTravels = (updatedTravels: Travel[]) => (travels.value = updatedTravels)
const clearTravels = () => {
  travels.value = []
}
</script>
