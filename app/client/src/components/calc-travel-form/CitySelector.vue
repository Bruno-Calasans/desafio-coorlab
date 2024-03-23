<template>
  <Select :modelValue="value" :onUpdate:modelValue="onSelect">
    <SelectTrigger class="bg-white text-zinc-600">
      <SelectValue placeholder="Selecione o destino" />
    </SelectTrigger>
    <SelectContent class="bg-white text-zinc-600">
      <SelectItem v-for="city of cities" :value="city" :key="city">{{ city }}</SelectItem>
    </SelectContent>
  </Select>
</template>

<script setup lang="ts">
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue
} from '@/components/ui/select'
import { useFetch } from '@vueuse/core'
import { onBeforeMount, ref } from 'vue'

type CitySelectorProps = {
  value: string
  onSelect: (city: string) => void
}
defineProps<CitySelectorProps>()

const cities = ref<string[]>([])

const loadCities = async () => {
  const { data } = await useFetch('http://localhost:3000/city').json()
  cities.value = data.value
}

onBeforeMount(async () => {
  await loadCities()
})
</script>
