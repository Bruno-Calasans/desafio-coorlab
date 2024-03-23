<template>
  <!-- Navegation Menu -->
  <section class="flex flex-col w-56 h-full bg-slate-800 p-2">
    <!-- Logo -->
    <a href="/" class="p-2 w-fit">
      <img class="h-5" src="/images/logo.png" />
    </a>
    <!-- Menu -->
    <nav class="mt-5 p-2 hover:bg-slate-900 rounded-sm cursor-pointer">
      <ul>
        <li class="flex items-center gap-1 transition">
          <Calculator :size="20" />
          <p class="text-sm font-semibold">Calculadora de Viagem</p>
        </li>
      </ul>
    </nav>
  </section>
</template>

<script setup lang="ts">
import { Calculator } from 'lucide-vue-next'
</script>
