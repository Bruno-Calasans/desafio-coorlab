<template>
  <div class="flex gap-2 flex-1">
    <!-- Form Area -->
    <div class="flex flex-col justify-center bg-slate-200 p-3 w-[60%] rounded-md">
      <div>
        <!-- todo Icon Here -->
        <p class="text-lg text-zinc-600 font-bold mb-5">Calcule o valor da viagem</p>
      </div>

      <Form class="flex flex-col gap-3">
        <FormField name="city" v-slot="{}">
          <FormItem>
            <FormLabel class="font-bold">Destino</FormLabel>
            <FormControl>
              <Select>
                <SelectTrigger class="bg-white text-zinc-600 rounded-none">
                  <SelectValue placeholder="Selecione o destino" />
                </SelectTrigger>
                <SelectContent class="bg-white text-zinc-600">
                  <SelectItem value="São Paulo">São Paulo </SelectItem>
                  <SelectItem value="Belo Horizonte">Belo Horizonte</SelectItem>
                  <SelectItem value="Fortaleza"> Fortaleza </SelectItem>
                </SelectContent>
              </Select>
            </FormControl>
          </FormItem>
        </FormField>

        <FormField name="date" v-slot="{}">
          <FormItem>
            <FormLabel class="font-bold">Data</FormLabel>
            <FormControl>
              <!-- Date Picker Here -->
              <Select>
                <SelectTrigger class="bg-white text-zinc-600 rounded-none">
                  <SelectValue placeholder="Selecione o destino" />
                </SelectTrigger>
                <SelectContent class="bg-white text-zinc-600">
                  <SelectItem value="São Paulo">São Paulo </SelectItem>
                  <SelectItem value="Belo Horizonte">Belo Horizonte</SelectItem>
                  <SelectItem value="Fortaleza"> Fortaleza </SelectItem>
                </SelectContent>
              </Select>
            </FormControl>
          </FormItem>
        </FormField>
      </Form>

      <Button
        size="sm"
        type="submit"
        class="font-bold bg-cyan-500 hover:bg-cyan-400 place-self-center mt-8"
        >Buscar</Button
      >
    </div>

    <!-- todo Result Area -->
    <div class="flex text-xl grow-2 w-full justify-center items-center">
      Nenhum dado selecionado
    </div>
  </div>
</template>

<script setup lang="ts">
import {
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage
} from '@/components/ui/form'
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue
} from '@/components/ui/select'
import { Input } from '@/components/ui/input'
import Button from './ui/button/Button.vue'
</script>
