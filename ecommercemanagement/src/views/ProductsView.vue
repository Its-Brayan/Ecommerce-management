<template>
  <v-card>
    <v-card-title>
   Add product Below
    </v-card-title>
    <v-card-text>
       <v-form  @submit.prevent="submitproduct">
        <v-container>
        <v-row>
            <v-col cols="6"   md="6" sm="6">
    <label  >Product Name
    <v-text-field
      v-model="form.product_name"
   
      
      style="width:350px"
      required
      label="name"
      variant="outlined"
      density="compact"
     
    ></v-text-field></label>
    </v-col>
    <v-col cols="6" md="6" sm="6">
    <label  >SKU
    <v-text-field
      v-model="form.serial_number"
      
      label="Serial no"
       style="width:350px; "
      required
      
       variant="outlined"
      density="compact"
     
    
    ></v-text-field></label>
    </v-col>
    </v-row>
    <v-row>
        <v-col cols="6" md="6" sm="6">
    <label  >Category
  
    <v-select
      v-model="form.product_category"
      
      :items="categories"
      item-title="category_name"
      item-value="id"
      style="width:350px"
      label="Category"

      required
       variant="outlined"
      density="compact"
   
    ></v-select></label>
    </v-col>
    <v-col cols="6" md="6" sm="6">
    <label  >Brand
     <v-autocomplete
      v-model="form.product_brand"
     
      :items="brands"
      item-title="brand_name"
      item-value="id"
      style="width:350px"
    
      label="Brand Name"
      required
       autocomplete
    
      variant="outlined"
      density="compact"
 
    ></v-autocomplete></label>
    </v-col>
    </v-row>
    <v-row>
        <v-col cols="6">
    <label  >Buying
     <v-text-field
      v-model="form.product_Bprice"
    
      style="width:350px"
     
      label="buying price"
      required
      variant="outlined"
      density="compact"
    
    ></v-text-field></label>
    </v-col>
    <v-col cols="6">
    <label  >Selling
     <v-text-field
      v-model="form.product_Sprice"
      
      style="width:350px"
     
      label="selling price"
      required
     
      variant="outlined"
      density="compact"
 
    ></v-text-field></label>
    </v-col>
    </v-row>
    <v-row>
        <v-col cols="6">
             <v-file-upload
             v-model="form.product_image"
              accept="image/*"
             width="930px"
             clearable
             density="compact"
    browse-text="Local Filesystem"
    divider-text="or choose locally"
    icon="mdi-upload"
    title="Product Image"
  ></v-file-upload>
 </v-col>
  </v-row>
 <div class="mt-8 float-right">
    <v-btn
      class="me-4 bg-blue-darken-3"
     
      
      @click="submitproduct"
      
    >
      submit
    </v-btn>
  
    <v-btn  class="bg-red-darken-3">
      clear
    </v-btn>
    </div>
    </v-container>
  </v-form>
  </v-card-text>
   </v-card>
</template>
<script setup>
 
  import { onMounted, ref } from 'vue'

  import { email, required } from '@vuelidate/validators'
  import axiosInst from "@/services/apis"
  import { toast } from 'vue3-toastify';
 


  

  let categories = ref([''])
  let brands = ref([''])


  const rules = {
    product_name: { required },
    serial_number: { required},
    product_category: { required },
    product_brand: { required },
    product_Bprice: { required },
    product_Sprice: { required },
    product_image: { required },

  }

  
   
  
  let form = ref({
 product_name:null,
 serial_number:null,
 product_category:null,
 product_brand:null,

 product_Bprice:null,
 product_Sprice:null,
 product_image:null,

  })

function  submitproduct(){
const formdata = new FormData();
formdata.append('product_name', form.value.product_name)
formdata.append('serial_number', form.value.serial_number)
formdata.append('product_category', form.value.product_category)
formdata.append('product_brand', form.value.product_brand)
formdata.append('product_Bprice', form.value.product_Bprice)  
formdata.append('product_Sprice', form.value.product_Sprice)
formdata.append('product_image', form.value.product_image)
  console.log(form.value.product_image)
axiosInst.post(`apis/addproduct`,formdata,{
  headers:{
    'content-type': 'multipart/form-data'
  },
})
  .then(()=>{
    toast.success("Product added successfully")
     loadItems({page: 1, itemsPerPage: itemsPerPage.value })

  }).catch(()=>{
     console.log(error)
   if (error.response.data && error.response.data.error)
                toast.error(error.response.data.error);
            else
                toast.error("failed to add product")
  }

  ).finally(()=>{
   
    closeDialog()
  }

  )

  
}
async function fetchcategories(){
  try{
    const response = await axiosInst.get('apis/category')
    categories.value = response.data.results || response.data

  }catch(error){
    console.log(error)
    if (error.response.data && error.response.data.error)
      toast.error(error.response.data.error);
    else
      toast.error("failed to fetch categories")
  }
  
}
async function fetchbrands(){
  try{
    const response = await axiosInst.get('apis/brand')
    brands.value = response.data.results || response.data  
  }catch(error){  
    console.log(error)
    if (error.response.data && error.response.data.error)
      toast.error(error.response.data.error);
    else
      toast.error("failed to fetch brands")
  }
}
onMounted(() => {
  fetchcategories()
  fetchbrands()
})
</script>

