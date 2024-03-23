<script setup lang="ts">
import { format } from 'date-fns'
import { Calendar as CalendarIcon } from 'lucide-vue-next'

import { ref } from 'vue'
import { cn } from '@/lib/utils'
import { Button } from '@/components/ui/button'
import { Calendar } from '@/components/ui/calendar'
import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover'

const date = ref<Date>()

defineProps({
  text: String,
  onSelect: {
    type: Function,
    default(date: Date) {
      return date
    }
  }
})
</script>

<template>
  <Popover>
    <PopoverTrigger as-child>
      <Button
        variant="outline"
        :class="
          cn(
            'w-full justify-start text-left font-normal bg-white text-zinc-600 hover:bg-white hover:text-zinc-600',
            !date && 'text-muted-foreground'
          )
        "
      >
        <CalendarIcon class="mr-2 h-4 w-4" />
        <span>{{ date ? format(date, 'd/M/y') : text ?? 'Pick a Date' }}</span>
      </Button>
    </PopoverTrigger>
    <PopoverContent class="w-full p-0">
      <Calendar v-model="date" @update:model-value="onSelect as any" />
    </PopoverContent>
  </Popover>
</template>
