

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
  ></v-data-table-server>

  </v-card>
</template>

  


<script setup>
import { ref } from 'vue'

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
      title: 'Product name',
      align: 'start',
      sortable: false,
      key: 'name',
    },
    { title: 'Serial No', key: 'calories', align: 'end' },
    { title: 'Category', key: 'cat', align: 'end' },
    { title: 'Brand', key: 'carbs', align: 'end' },
    { title: 'Buying price', key: 'bp', align: 'end' },
    { title: 'Selling price', key: 'sp', align: 'end' },
  ])
  const search = ref('')
  const serverItems = ref([])
  const loading = ref(true)
  const totalItems = ref(0)
  function loadItems ({ page, itemsPerPage, sortBy }) {
    loading.value = true
    FakeAPI.fetch({ page, itemsPerPage, sortBy }).then(({ items, total }) => {
      serverItems.value = items
      totalItems.value = total
      loading.value = false
    })
  }
 

</script>
