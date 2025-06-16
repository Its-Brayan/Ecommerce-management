
<template>
    <v-card>
        <v-card-title>
            Brands
            <div class="float-right">
                <v-btn variant="outline" elevation="4" rounded="xl" style="text-transform: capitalize;"  @click="openDialog"><span class="mr-2" ><v-icon>mdi-plus</v-icon></span>Add Brands</v-btn>
            </div>
        </v-card-title>
        <v-card-text>
            <v-text-field
     v-model="search"
    
     prepend-inner-icon="mdi-magnify"
     variant="outlined" 
        placeholder="Search anything"
     density="compact"
     width="250px"
     class="float-left mt-5"
     ></v-text-field>

     <v-data-table-server
        v-model:items-per-page="itemsPerPage"
    :headers="headers"
    :items="serverItems"
    :items-length="totalItems"
    :loading="loading"
    :search="search"
    item-value="name"
 
        @update:options="fetchBrands"
     ></v-data-table-server>
        </v-card-text>
    </v-card>
<v-dialog
      v-model="dialog"
      max-width="600"
    >
    

      <v-card>
      <v-card-title    prepend-icon="mdi-registered-trademark"
       >Add Brands
        
       <v-btn
           
            variant="plain"
            class="float-right"
            @click="dialog = false"
            title="close"
            icon="mdi-close-circle-outline"
          ></v-btn>
         
          </v-card-title>
        <v-card-text>
         
          <v-row dense>
            <v-col
              cols="12"
              md="4"
              sm="6"
            >
              <v-text-field
                label="Brand Name*"
                v-model="form.brand_name"
                width="550px"
                required
              ></v-text-field>
            </v-col>
            </v-row>

          
         
          
            
        

           

          <small class="text-caption text-medium-emphasis">*indicates required field</small>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>

         

          <v-btn
            color="primary"
            text="Save"
            variant="tonal"
            @click="submitbrand"
          ></v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

</template>
<script setup>
import { ref } from 'vue'

import axiosInst from "@/services/apis"
  import { toast } from 'vue3-toastify';
  
const search = ref('')
let dialog = ref(false)

let name = ref('')
let headers = ref([
  {
    title: 'ID',
    value: 'id',
    sortable: true,
  },
  {
    title: 'Name',
    value: 'brand_name',
    sortable: true,
  },
 
])

 const FakeAPI = {
    async fetch ({ page, itemsPerPage, sortBy, search }) {
      return new Promise(resolve => {
        setTimeout(() => {
          const start = (page - 1) * itemsPerPage
          const end = start + itemsPerPage
          const items = desserts.slice().filter(item => {
            if (search.name && !item.name.toLowerCase().includes(search.name.toLowerCase())) {
              return false
            }
            // eslint-disable-next-line sonarjs/prefer-single-boolean-return
            if (search.calories && !(item.calories >= Number(search.calories))) {
              return false
            }
            return true
          })
          if (sortBy.length) {
            const sortKey = sortBy[0].key
            const sortOrder = sortBy[0].order
            items.sort((a, b) => {
              const aValue = a[sortKey]
              const bValue = b[sortKey]
              return sortOrder === 'desc' ? bValue - aValue : aValue - bValue
            })
          }
          const paginated = items.slice(start, end === -1 ? undefined : end)
          resolve({ items: paginated, total: items.length })
        }, 500)
      })
    },
  }
  const itemsPerPage = ref(5)
    const serverItems = ref([])
  const loading = ref(true)
  const totalItems = ref(0)
  const brands = ref([])

  async function fetchBrands ({ page, itemsPerPage, sortBy }) {
    try{
    loading.value = true
    const response = await axiosInst.get('apis/brand',{
      params:{
        page,
        itemsPerPage,
      }
    })
    console.log(response.data)
    brands.value = response.data.results || response.data
  
      serverItems.value = response.data.results || response.data
      totalItems.value = response.data.count || response.data.length
      loading.value = false
    }catch(error){
      console.log(error)
      loading.value = false
      if (error.response.data && error.response.data.error)
        toast.error(error.response.data.error);
      else
        toast.error("failed to fetch Brands")
    }
  }

function openDialog() {
    dialog.value = true
}
function closeDialog() {
    dialog.value = false
    form.value = {
      brand_name : null
    }
  }
  let form = ref({
    brand_name : null
  })
async function submitbrand(){
const formdata ={
  ...form.value
}
let url = 'apis/brand'
axiosInst.post(url,formdata)
.then(()=>{
  toast.success("Brand added succesfully")
  loadItems({page: 1, itemsPerPage: itemsPerPage.value })
}

).catch((error)=>{
  console.log(error)
  if (error.response.data && error.response.data.error)
    toast.error(error.response.data.error);
  else
    toast.error("failed to add Brand")
}).finally(()=>{
  closeDialog()
  
})
}
</script>
