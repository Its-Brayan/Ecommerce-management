
<template>
  <v-card class="w-100">
    <v-card-title>
     Users
     <v-btn class="float-right bg-blue-darken-3" @click="opendialog">add User</v-btn>
     <div class="pa-4 text-center">
    <v-dialog
      v-model="dialog"
      max-width="600"
    >
      
   
      <v-card
        

      >
         <v-card-title prepend-icon="mdi-account"
      >User Profile
          
           <v-btn
            icon="mdi-close-circle-outline"
            variant="plain"
            @click="dialog = false"
            class="float-right"
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
                label="First name*"
                v-model="firstname"
                required
              ></v-text-field>
            </v-col>

            <v-col
              cols="12"
              md="4"
              sm="6"
            >
              <v-text-field
                hint="example of helper text only on focus"
                label="Middle name"
                v-model="middlename"
              ></v-text-field>
            </v-col>

            <v-col
              cols="12"
              md="4"
              sm="6"
            >
              <v-text-field
                hint="example of persistent helper text"
                label="Last name*"
                v-model="lastname"
                persistent-hint
                required
              ></v-text-field>
            </v-col>

            <v-col
              cols="12"
              md="4"
              sm="6"
            >
              <v-text-field
                label="Email*"
                v-model="email"
                required
              ></v-text-field>
            </v-col>

            <v-col
              cols="12"
              md="4"
              sm="6"
            >
              <v-text-field
                label="Password*"
                type="password"
                v-model="password"
                required
              ></v-text-field>
            </v-col>

            <v-col
              cols="12"
              md="4"
              sm="6"
            >
              <v-text-field
                label="Confirm Password*"
                type="password"
                v-model="confirmPassword"
                required
              ></v-text-field>
            
            </v-col>

         
          
          </v-row>
          <v-row>
            <v-col>
                <v-select
                label="User Type"
                :items="['Admin', 'User']"
                v-model="usertype"
                required
                ></v-select>
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
            @click="dialog = false"
          ></v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>

    </v-card-title>
   <v-card-text class="w-25 pt-4">
    <v-text-field
     v-model="search"
     label ="Search"
     prepend-inner-icon="mdi-magnify"
     variant="outlined" 
        placeholder="Search anything"
     density="compact"
     witdth="100px"
     

     
    
   
   
     ></v-text-field>
    
   
</v-card-text>
   


  <v-data-table :headers="headers" :items="users" :search="search" class="elevation-1" height="300px">
    <template v-slot:item.actions="{ item }">
    <v-icon icon="mdi-pencil" class="pr-6" @click="edit(item.id)"></v-icon>
   <v-icon icon="mdi-delete" @click="remove(item.id)" ></v-icon>
    </template>
    
     
   
  </v-data-table>
  </v-card>
    
</template>



<script setup>
import { ref } from 'vue'
import { onMounted } from 'vue';
let dialog = ref(false)
const search = ref('')
const users=ref([])
const headers=[
  {title:'ID',value:'id'},
  {title:'FirstName',value:'firstname'},
  {title:'MiddleName',value:'middilename'},
  {title:'LastName',value:'lastname'},
  {title:'Email',value:'email'},
  {title:'Password',value:'password'},
  {title:'Actions',value:'actions',sortable:false,align:'center',width:150}



]
const fetchusers= async () =>
  {
  try{
   const res= await fetch('http://localhost:8000/api/settings/')
   const data = await res.json()
   users.value = data.map(u=> ({
    id:u.id,
    fullname : u.name,
    email : u.regemail,
   
   }))
    }catch(error){
      console.error('Failed to fetch users:',error)
    }
  }
  onMounted(()=>{
    fetchusers()
  }

  )
  function edit (id) {
    isEditing.value = true

    const found = users.value.find(user=> user.id === id)

    record.value = {
      id: found.id,
      fullname: found.name,
      email: found.regemail,
     
    }

    dialog.value = true
  }

  function remove (id) {
    const index = users.value.findIndex(user => user.id === id)
    users.value.splice(index, 1)
  }

function opendialog() {
  dialog.value = true
} 

 
</script>