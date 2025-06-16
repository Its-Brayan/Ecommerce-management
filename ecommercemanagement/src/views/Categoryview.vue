
<template>
    <v-card>
        <v-card-title>
            Category
            <div class="float-right">
                <v-btn variant="outline" elevation="4" rounded="xl" style="text-transform: capitalize;"  @click="openDialog"><span class="mr-2" ><v-icon>mdi-plus</v-icon></span>add category</v-btn>
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
       loading-text="Loading... Please wait"
    
       v-model:items-per-page="itemsPerPage"  :headers="headers" :items="serverItems"
        :items-length="totalItems" :loading="loading" :search="search" item-value="name" @update:options="fetchcategories"
     ></v-data-table-server>
        </v-card-text>
    </v-card>
    
<v-dialog
      v-model="dialog"
      max-width="600"
    >
    
<v-form @submit.prevent="submitcategory">
      <v-card>
      <v-card-title    prepend-icon="mdi-registered-trademark"
       >Add category
        
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
              cols="6"
              md="4"
              sm="6"
            >
              <v-text-field
                label="Category Name*"
                v-model="form.category_name"
                 width="230px"
                required
              ></v-text-field>
            </v-col>
            <v-col cols="6"   md="4"
             >
                <v-text-field 
                label="Description*"
                v-model="form.category_description"
                  width="310px"
                  class="pl-15"
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
            @click="submitcategory"
          ></v-btn>
        </v-card-actions>
      </v-card>
    </v-form>
    </v-dialog>

</template>
<script setup>
import { onMounted, ref } from 'vue'

import axiosInst from "@/services/apis"
  import { toast } from 'vue3-toastify';
  
const search = ref('')
let dialog = ref(false)

const FakeAPI = {
  async fetch({ page, itemsPerPage, sortBy }) {
    return new Promise(resolve => {
      setTimeout(() => {
        const start = (page - 1) * itemsPerPage
        const end = start + itemsPerPage
        const items = desserts.slice()
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

let headers = ref([
  {
    title: 'ID',
    value: 'id',
    sortable: true,
  },
  {
    title: 'Name',
    value: 'category_name',
    sortable: true,
  },
  {
    title: 'Description',
    value: 'category_description',
    sortable: true,
  },
])


const serverItems = ref([])
const loading = ref(true)
const totalItems = ref(0)
const categories = ref([])

async function fetchcategories ({ page, itemsPerPage, sortBy }) {
   try{
    loading.value = true
    const response = await axiosInst.get('apis/category',{
      params:{
        page,
        itemsPerPage,
      }
    })
    console.log(response.data)
    categories.value = response.data.results || response.data
      serverItems.value = response.data.results || response.data.items || response.data
    totalItems.value = response.data.count || response.data.total || serverItems.value.length
   loading.value = true
  }catch(error){

     serverItems.value = []
    totalItems.value = 0
    toast.error("Failed to fetch categories")
    
  }finally{
    loading.value = false
  }
}

function openDialog() {
    dialog.value = true
}
function closeDialog(){
  dialog.value= false
}
let form = ref({
  category_name:null,
  category_description:null,
})

async function submitcategory(){
  const formdata={
    ...form.value
  }
  let url = 'apis/category'

axiosInst.post(url, formdata)
.then(()=>{
  toast.success("Category added successfully")
  loadItems({page: 1, itemsPerPage: itemsPerPage.value })

}
).catch((error)=>{
  console.error(error)
  if (error.response && error.response.data && error.response.data.error) {
    toast.error(error.response.data.error);
  } else {
    toast.error("Failed to add category");
  }
}

).finally(()=>{
closeDialog()
}

)
}
onMounted(() => {
  fetchcategories()
})
</script>

