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

const cities = ['São paulo', 'Fortaleza', 'Belo Horizonte']

defineProps({
  value: String,
  onSelect: {
    type: Function,
    default(city: string) {
      return city
    }
  }
})
</script>
