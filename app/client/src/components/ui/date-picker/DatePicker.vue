<script setup lang="ts">
import { format } from 'date-fns'
import { Calendar as CalendarIcon } from 'lucide-vue-next'

import { ref } from 'vue'
import { cn } from '@/lib/utils'
import { Button } from '@/components/ui/button'
import { Calendar } from '@/components/ui/calendar'
import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover'
import type { DatePickerModel } from 'v-calendar/dist/types/src/use/datePicker.js'

const date = ref<Date>()

type DatePickerProps = {
  text: string
  onSelect: (date?: DatePickerModel) => void
}

defineProps<DatePickerProps>()
</script>

<template>
  <Popover>
    <PopoverTrigger as-child>
      <Button
        variant="outline"
        :class="
          cn(
            'w-full justify-between text-left font-normal bg-white text-zinc-600 hover:bg-white hover:text-zinc-800',
            !date && 'text-muted-foreground'
          )
        "
      >
        <span>{{ date ? format(date, 'd/M/y') : text ?? 'Pick a Date' }}</span>
        <CalendarIcon class="h-4 w-4" />
      </Button>
    </PopoverTrigger>
    <PopoverContent class="w-full p-0">
      <Calendar v-model="date" @update:model-value="onSelect" />
    </PopoverContent>
  </Popover>
</template>
