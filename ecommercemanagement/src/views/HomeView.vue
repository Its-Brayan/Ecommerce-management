

<template >
<v-card>
     <v-card-title>
        Products
        <div class="float-right">
           <v-btn variant="outline"  rounded="xl" elevation="8" append-icon="mdi-plus-circle" to="/addingproduct">Add product</v-btn>

        </div>
      </v-card-title>
    
   
      <v-card-text class="w-25 pt-6">
       
  <v-text-field
  
     v-model="search"
   
     prepend-inner-icon="mdi-magnify"
     variant="solo" 
        placeholder="Search anything"
     density="compact"
     witdth="10px"
         ></v-text-field>
     
     </v-card-text>
    
   
   



 
    <v-data-table-server
    v-model:items-per-page="itemsPerPage"
    :headers="headers"
    :items="serverItems"
    
    :items-length="totalItems"
    :loading="loading"
    :search="search"
    item-value="name"
    @update:options="loadItems"
  >
<template v-slot:item.product_image="{item,value}">
  <v-img :src=resolveUrl(item.product_image) max-height="50" max-width="50" contain></v-img>
</template></v-data-table-server>

  </v-card>
</template>

  


<script setup>
import { ref } from 'vue'
  import { toast } from 'vue3-toastify';
  import axiosInst from "@/services/apis"
const FakeAPI = {
    async fetch ({ page, itemsPerPage, sortBy }) {
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
  const headers = ref([
    {
      title:'Product Image',
      value:'product_image',
    },
    {
      title: 'Product name',
      align: 'start',
      sortable: false,
      value:'product_name',
    },
    { title: 'Serial No', value: 'serial_number', align: 'end' },
    { title: 'Category', value: 'product_category', align: 'end' },
    { title: 'Brand', value: 'product_brand', align: 'end' },
    { title: 'Buying price', value:'product_Bprice', align: 'end' },
    { title: 'Selling price', value:'product_Sprice', align: 'end' },
  ])
  const search = ref('')
  const serverItems = ref([])
  const loading = ref(true)
  const totalItems = ref(0)
  async function loadItems ({ page, itemsPerPage, sortBy }) {
    try{
    loading.value = true
    const response = await axiosInst.get('apis/addproduct',{
      params:{
        page,
        itemsPerPage
      }
    })
   console.log(response.data)
     serverItems.value = response.data.results || response.data.items || response.data
     totalItems.value = response.data.count || response.data.total || serverItems.value.length
       
    }catch(error){
      toast.error("failed to load products")
      serverItems.value = []
      totalItems.value = 0
    }finally{
      loading.value = false
    }
  }

  function resolveUrl(path) {
  if (!path) return ''
  return path.startsWith('http')
    ? path
    : `http://127.0.0.1:8000${path}`  // Replace with your backend address if different
}
 

</script>
