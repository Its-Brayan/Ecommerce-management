<template>

      <v-navigation-drawer
        v-model="drawer"
        :rail="rail"
        permanent
        @click="rail = false"
      >
        <v-list>
          <v-list-item
            prepend-icon="mdi-cart"
            subtitle="product management"
            title="Ecommerce"
          ></v-list-item>
        </v-list>

       

        <v-list density="compact" nav>
          <v-list-item prepend-icon="mdi-home-outline" title="Products" value="products" to="/"></v-list-item>
         
          <v-list-group  prepend-icon="mdi-cog"  to="/settings"><template v-slot:activator="{ props }">
              <v-list-item
                v-bind="props"
                title="Settings"
              ></v-list-item>
            </template>
            <v-list-item  title="Brands" prepend-icon="mdi-registered-trademark" value="brands" to="/brands" ></v-list-item>
            <v-list-item title="Categories" prepend-icon="mdi-shape-plus" value="categories" to="/category"></v-list-item>
            <v-list-item title="Manage Users" prepend-icon="mdi-account" value ='users' to="/settings"></v-list-item>
          </v-list-group>
          

   
     
    
          <v-list-item  prepend-icon="mdi-logout" title="Logout" value="logout" to="/login" ></v-list-item>
        </v-list>
      </v-navigation-drawer>
</template>
<script setup>
  import { ref } from 'vue'

  const drawer = ref(true)
  const rail = ref(true)
  // This should be set based on your authentication logic
  
</script>