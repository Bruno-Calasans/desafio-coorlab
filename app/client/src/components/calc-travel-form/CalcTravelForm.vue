<template>
  <div class="flex gap-2 flex-1">
    <!-- Form Area -->
    <div class="flex flex-col justify-center bg-slate-200 p-3 w-[60%] rounded-md">
      <div>
        <!-- todo Icon Here -->
        <p class="text-lg text-zinc-600 font-bold mb-5">Calcule o valor da viagem</p>
      </div>

      <form class="flex flex-col gap-3" @submit="submitHandler">
        <!-- City field -->
        <div class="flex flex-col gap-1">
          <div class="text-zinc-600 font-bold">Destino</div>
          <CitySelector :value="travelCity" :onSelect="selectCityHandler" />
        </div>

        <!-- Date Picker Here -->
        <div>
          <div class="text-zinc-600 font-bold">Data</div>
          <DatePicker text="Escolha a data da viagem" :onSelect="selectDateHandler" />
        </div>

        <Button
          size="sm"
          type="submit"
          class="font-bold bg-cyan-500 hover:bg-cyan-400 place-self-center mt-8"
        >
          Buscar
        </Button>
      </form>
    </div>

    <!-- Invalid Data -->
    <InvalidDataDialog :isOpen="showInvalidDataDialog" :onClose="closeDialog" />

    <!-- todo Result Area -->
    <div class="flex text-xl grow-2 w-full justify-center items-center">
      Nenhum dado selecionado
    </div>
  </div>
</template>

<script setup lang="ts">
import CitySelector from './CitySelector.vue'
import DatePicker from '@/components/ui/data-picker'
import { Button } from '@/components/ui/button'
import InvalidDataDialog from '@/components/calc-travel-form/InvalidDataDialog.vue'
import { ref } from 'vue'

const travelCity = ref('')
const travelDate = ref<null | Date>(null)
const showInvalidDataDialog = ref(false)

const selectDateHandler = (date: Date) => (travelDate.value = date)
const selectCityHandler = (city: string) => (travelCity.value = city)
const closeDialog = () => (showInvalidDataDialog.value = false)
const openDialog = () => (showInvalidDataDialog.value = true)

const props = defineProps({
  onSucessSubmit: Function
})

const submitHandler = (e: Event) => {
  e.preventDefault()

  const city = travelCity.value
  const date = travelDate.value

  if (!city || !date) {
    openDialog()
  }

  if (props.onSucessSubmit) {
    props.onSucessSubmit({ city, date })
  }
}
</script>
