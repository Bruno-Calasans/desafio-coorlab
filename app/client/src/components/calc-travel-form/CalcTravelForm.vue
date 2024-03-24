<template>
  <div class="flex flex-col justify-center bg-slate-200 p-3 rounded-md w-[60%]">
    <!-- Form -->
    <div>
      <div class="flex gap-1 items-center mb-5">
        <!-- todo Icon Here -->
        <HandCoins :size="25" />
        <p class="text-lg text-zinc-600 font-bold">Calcule o valor da viagem</p>
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
import DatePicker from '@/components/ui/date-picker'
import { Button } from '@/components/ui/button'
import InvalidDataDialog from '@/components/calc-travel-form/InvalidDataDialog.vue'
import type { BestTravels } from '@/components/calc-travel-form/Travel'
import { useFetch } from '@vueuse/core'
import { HandCoins } from 'lucide-vue-next'
import type { DatePickerModel } from 'v-calendar/dist/types/src/use/datePicker.js'

const travelCity = ref('')
const travelDate = ref<DatePickerModel | undefined>()
const showInvalidDataDialog = ref(false)

const selectDateHandler = (date?: DatePickerModel) => (travelDate.value = date)
const selectCityHandler = (city: string) => (travelCity.value = city)
const closeDialog = () => (showInvalidDataDialog.value = false)
const openDialog = () => (showInvalidDataDialog.value = true)

type CalcTravelFormProps = {
  onSucessSubmit: (travels: BestTravels | null) => void
}

const props = defineProps<CalcTravelFormProps>()

const getBestTravels = async () => {
  try {
    const { data } = await useFetch(
      `http://localhost:3000/best-travels/${travelCity.value}`
    ).json<BestTravels>()
    props.onSucessSubmit(data.value)
  } catch (error) {
    props.onSucessSubmit(null)
  }
}

const submitHandler = async (e: Event) => {
  e.preventDefault()

  if (!travelCity.value || !travelDate.value) {
    return openDialog()
  }

  await getBestTravels()
}
</script>
