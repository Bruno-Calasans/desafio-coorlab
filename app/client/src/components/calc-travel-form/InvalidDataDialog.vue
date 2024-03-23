<template>
  <Dialog :open="isOpen">
    <DialogContent class="bg-white">
      <DialogHeader>
        <VisuallyHidden asChild>
          <DialogTitle class="text-zinc-900 text-2xl">Dados Inválidos</DialogTitle>
        </VisuallyHidden>
        <DialogDescription class="flex flex-col justify-center items-center text-zinc-800 text-2xl">
          <CircleAlert class="text-cyan-500" :size="62" />
          Insira os valores para realizar a cotação.
        </DialogDescription>
      </DialogHeader>

      <DialogFooter>
        <div class="flex justify-center w-full">
          <Button
            @click="onClose"
            size="sm"
            type="submit"
            class="font-bold bg-cyan-500 hover:bg-cyan-400 mt-8 w-32 p-2"
          >
            Fechar
          </Button>
        </div>
      </DialogFooter>
    </DialogContent>
  </Dialog>
</template>

<script setup lang="ts">
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader
} from '@/components/ui/dialog'
import { Button } from '@/components/ui/button'
import { VisuallyHidden } from 'radix-vue'
import { CircleAlert } from 'lucide-vue-next'

type InvalidDataDialogProps = {
  isOpen: boolean
  onClose: (e: Event) => void
}

defineProps<InvalidDataDialogProps>()
</script>
