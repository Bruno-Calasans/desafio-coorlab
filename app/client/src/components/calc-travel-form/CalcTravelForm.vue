<template>
  <div class="flex flex-col justify-center bg-slate-200 p-3 rounded-md w-[60%]">
    <!-- Form -->
    <div>
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
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import CitySelector from './CitySelector.vue'
import DatePicker from '@/components/ui/data-picker'
import { Button } from '@/components/ui/button'
import InvalidDataDialog from '@/components/calc-travel-form/InvalidDataDialog.vue'
import type { Travel } from '@/components/calc-travel-form/Travel'

const travelCity = ref('')
const travelDate = ref<null | Date>(null)
const showInvalidDataDialog = ref(false)

const selectDateHandler = (date: Date) => (travelDate.value = date)
const selectCityHandler = (city: string) => (travelCity.value = city)
const closeDialog = () => (showInvalidDataDialog.value = false)
const openDialog = () => (showInvalidDataDialog.value = true)

type CalcTravelFormProps = {
  onSucessSubmit: (travels: Travel[]) => void
}

const props = defineProps<CalcTravelFormProps>()

const submitHandler = (e: Event) => {
  e.preventDefault()

  if (!travelCity.value || !travelDate.value) {
    return openDialog()
  }

  // todo get travels from api
  const travel = {
    id: 1,
    name: 'Expresso Oriente',
    price_confort: 'R$ 52.10',
    price_econ: 'R$ 21.50',
    city: 'São Paulo',
    duration: '12h',
    seat: '12C',
    bed: '5A'
  }
  const travels = [travel, travel]
  props.onSucessSubmit(travels)
}
</script>
