<template >
    <v-app>
        <v-card 
        
        variant = "elevated"
        class=" mx-auto mt-15"

        color="white"
        max-width="1500">
         <v-overlay :model-value="loading" class="align-center justify-center">
         <v-progress-circular indeterminate color="white" v-if="loading"></v-progress-circular>
      
    </v-overlay>
        <v-container>
            <v-row>
                <v-col cols="6">
                    <v-img
        :aspect-ratio="1/1"
        class="bg-white fill-height"
        style="min-height: 500px"
        src="/187435b9-4f79-412e-afa3-3e2a28149d7f (1).png"
        width="500"
        cover
      ></v-img>
                </v-col>
                <v-col cols="6">
                  <v-btn-toggle v-model="activetab">
          <v-btn variant="plain" value="login" v-model="activetab" >Login</v-btn><v-btn value="register" variant="plain" >Register</v-btn>
          </v-btn-toggle>
        
          <v-form @submit.prevent="handlelogin" v-if="activetab==='login'" >
             <v-text-field
          v-model="email"
          
          :readonly="loading"
          :rules="[rules.required]"
          class="mb-2"
          label="Email"
          placeholder ="Enter your email"
          density="compact"
          variant = "outlined"
          
          clearable
        ></v-text-field>

        <v-text-field
          v-model="password"
          :readonly="loading"
           :append-inner-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
         :rules="[rules.required, rules.min]"
          :type="show1 ? 'text' : 'password'"
          @click:append-inner="show1 = !show1"
          label="Password"
          variant = "outlined"
          placeholder="Enter your password"
          density="compact"
          
          clearable
        ></v-text-field>
        <v-btn
          
          :loading="loading"
          color="success"
          size="large"
          type="submit"
          variant="elevated"
         
          block
        
          
        >
          Login
        </v-btn>
          </v-form>
           
          <v-form v-else @submit.prevent="handleRegister">
          
           <v-text-field
          v-model="form.Firstname"
          :readonly="loading"
          :rules="[rules.required]"
          class="mb-2"
          label="First Name"
           density="compact"
          variant = "outlined"
          placeholder ="Enter your Full name"
          
          clearable
        ></v-text-field>
             <v-text-field
          v-model="form.Lastname"
          :readonly="loading"
          :rules="[rules.required]"
          class="mb-2"
          label="Last Name"
           density="compact"
          variant = "outlined"
          placeholder ="Enter your Full name"
          
          clearable
        ></v-text-field>
         <v-text-field
          v-model="form.regemail"
          :readonly="loading"
          :rules="[rules.required]"
          class="mb-2"
          label="Email"
           density="compact"
          variant = "outlined"
          placeholder ="Enter your email"
           
          clearable
        ></v-text-field>
        <v-text-field
          v-model="form.regpassword"
          :readonly="loading"
          :rules="[rules.required]"
          label="Password"
           density="compact"
          variant = "outlined"
          placeholder="Enter your password"
          
          clearable
          
        ></v-text-field>
 <v-btn
        
          :loading="loading"
          color="success"
          size="large"
          type="submit"
          pointer = "cursor"
          variant="elevated"
          authtab = 'register'
        
       
          block
          
        >Register</v-btn>
          </v-form>
     

       
                </v-col>
            </v-row>
        </v-container>
        </v-card>
    </v-app>
    
</template>

<script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import { toast } from 'vue3-toastify';
 import axiosInst from '@/services/apis'

 const loading=ref(false)
 const activetab = ref('login')

const error = ref(null)
  let form = ref({
    Firstname : null,
    Lastname:null,
    regemail:null,
    regpassword:null
  })
  async function handleRegister(){
  const formdata = {
      ...form.value
  }
  let url = `apis/register`
  axiosInst.post(url,formdata)
  .then(()=>{
  toast.success("User Registered Sucessfully")
  }).catch((error)=>{
     console.log(error)
       if (error.response.data && error.response.data.error)
                toast.error(error.response.data.error);
            else
                toast.error("failed to add User")
  })
  
}
async function handlelogin(){
 const formdata = ref({
  email:null,
  password:null
 }) 
 try{
 const response=await axiosInst.post('apis/token',formdata)
  const data = response.data
  if(!response.ok){
    toast.error("login failed")
    return
  }
  localStorage.getItem('access', data.access)
  localStorage.getItem('refresh', data.refresh)
  toast.success("login successful")
  
}catch(error){
  error.value = "network error"
}
}
 
 
   const rules = {
    required: value => !!value || 'Required.',
    
    email: value => {
      const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      return pattern.test(value) || 'Invalid e-mail.'
    },
  }
</script>
