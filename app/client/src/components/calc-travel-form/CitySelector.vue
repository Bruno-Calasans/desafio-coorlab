<template>
  <Select :modelValue="value" :onUpdate:modelValue="onSelect">
    <SelectTrigger
      :class="
        cn(
          'bg-white text-zinc-600 hover:text-zinc-800 px-4 py-2 transition',
          !value && 'text-muted-foreground'
        )
      "
    >
      <SelectValue class="text-red" placeholder="Selecione o destino" />
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
import { cn } from '@/lib/utils'

type CitySelectorProps = {
  value: string
  onSelect: (city: string) => void
}
defineProps<CitySelectorProps>()

const cities = ref<string[]>([])

const loadCities = async () => {
  try {
    const { data } = await useFetch('http://localhost:3000/city').json<string[]>()
    if (!data.value) return
    cities.value = data.value
  } catch (error) {
    cities.value = []
  }
}

onBeforeMount(async () => {
  await loadCities()
})
</script>
