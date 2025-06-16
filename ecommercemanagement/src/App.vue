<template>
  <v-layout>
    <v-card class="w-100">

      <v-app>
        <v-sheet style="">
          <Menu v-if="showsidebar"/>
        </v-sheet>
      <!-- <RouterView/> -->
       <v-main id="content">
        <v-container class="cont" fluid>
          <v-row>
            <v-col>
              <RouterView/>
            </v-col>
          </v-row>
        </v-container>
        </v-main>
      </v-app>
    </v-card>
  </v-layout>
</template>
<script setup>
import { ref } from 'vue'
import Menu from './components/menu.vue'
import { useRoute } from 'vue-router'
import {computed}  from 'vue'
import { toast } from 'vue3-toastify';


const route = useRoute()
const showsidebar = computed(()=>{
 return !route.path.startsWith('/login')
 }

 )
</script>