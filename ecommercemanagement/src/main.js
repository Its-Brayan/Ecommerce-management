
import '@mdi/font/css/materialdesignicons.css'
import { VFileUpload } from 'vuetify/labs/VFileUpload'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import Vue3Toasity from 'vue3-toastify';
import 'vue3-toastify/dist/index.css';
// Vuetify

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import App from './App.vue'
import router from './router'
const vuetify = createVuetify({
  components:{
    ...components,
    VFileUpload,
  },
  directives,
})

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(vuetify)

app.mount('#app')
